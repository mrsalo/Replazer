#!/usr/bin/env python

import unittest
from fill_template import get_variables_from, render_lines_with, VariableNotDefinedError

class Test(unittest.TestCase):
    def testGetsNoVariablesFromListWithNone(self):
        my_list = [
                    "Hello World",
                    "I am a text",
                    "with no variables"
                  ]
        output = get_variables_from(my_list)
        expected = set()
        self.assertSetEqual(expected, output);

    def testTextIsUnalteredWhenNoVariablesAreIncludedAfterRendering(self):
        my_list = [
                    "Hello World",
                    "I am a text",
                    "with no variables"
                  ]
        output = render_lines_with(set(), my_list)
        expected = my_list
        self.assertListEqual(output, expected)

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

    def testRaisesExceptionWhenAskedToRenderButNotAllVariablesAreDefined(self):
        my_list = [
                    "foo bar\n",
                    "{{VAR}}",
                    "fooo {{VAR2}}",
                    "safa {{VAR}} {{VAR3}} {{   VAR2   }}",
                  ]
        try:
            render_lines_with({'VAR2' : 'VAR2', 'VAR3' : 'VAR3'}, my_list)
        except VariableNotDefinedError as e:
            self.assertEqual(e.message, 'Variable {{VAR}} was found, but not defined!')
            self.assertEqual(e.variable, '{{VAR}}')
            return
        self.fail('VariableNotDefinedError not thrown')
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
