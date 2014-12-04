#!/usr/bin/env python

import unittest
from fill_template import get_variables_from, render_lines_with

class Test(unittest.TestCase):
    
    def testGetsVariablesFromList(self):
        my_list = [
                    "foo bar\n",
                    "{{VAR}}",
                    "fooo {{VAR2}}",
                    "safa {{VAR}} {{VAR3}} {{   VAR2   }}",
                  ]
        output = get_variables_from(my_list)
        expected = set(['VAR', 'VAR2', 'VAR3'])
        self.assertSetEqual(output, expected) 

    def testInsertsVariables(self):
        my_list = [
                    "foo bar\n",
                    "{{VAR}}",
                    "fooo {{VAR2}}",
                    "safa {{VAR}} {{VAR3}} {{   VAR2   }}",
                  ]

        output = render_lines_with({'VAR': 'VAR', 'VAR2' : 'VAR2', 'VAR3' : 'VAR3'}, my_list)
        expected = [
                    "foo bar\n",
                    "VAR",
                    "fooo VAR2",
                    "safa VAR VAR3 VAR2",
                  ]
        self.assertListEqual(output, expected)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
