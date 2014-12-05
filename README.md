Replazer
========

Simple tool for inserting variables in plaintext documents

There was not yet much effort spent in developing this little tool, nevertheless i think it's useful, so have fun :)

Usage: ./replazer.py template_name output_name

Sample Scenario:
--------------
Contents of template.text:
*{{ Greeting }} {{ User }}!
Dear {{User }} this is a demo.
It shows that {{Greeting   }} is inserted.
You can also have {{ Variable with spaces }} in your text.
So, {{User}} what do you say?*

$ ./replazer.py template.text output.text
I found 3 variables in the template:
['Variable with spaces', 'Greeting', 'User']
Please give them a meaning:
Variable with spaces: 
**variables with spaces**
Greeting:
**Hello**
User:
**John**

Contents of newly created ouput.text:
*Hello John!
Dear John this is a demo.
It shows that Hello is inserted.
You can also have variables with spaces in your text.
So, John what do you say?*

