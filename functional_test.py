#!/usr/bin/env python

import unittest
import subprocess
import os


class BasicUsageTest(unittest.TestCase):
    def test(self):
    # John is a sysadmin. He has heard about a new tool called 
    # Replazer which he could easily use to insert variable names
    # in his configuration template files.
    
    # As he likes the idea he gives it a try and calls the program
        output = run('./replazer.py')
    # He gets a usage message as expected as he obviously gave too
    # few parameters to the program
        self.assertTrue(output.startswith('Usage'))

    # Ok, now that he knows how to use it, he creates a test template
    # file containing some variables
        johnstemplate = 'john.template'
        template_text = 'Hello dear {{ USER }},\ni want your {{ ITEM }}\n'
        
        with open(johnstemplate, 'w') as f:
            f.write(template_text)
            f.close()

    # As he has finished testing, he happily cleans up his current dir
    # and focuses on another task
        os.remove(johnstemplate)

def run(command):
    handle = subprocess.Popen(command, stdout=subprocess.PIPE)
    handle.wait()
    return handle.communicate()[0]

if __name__ == '__main__':
    unittest.main()
