
"""
Identifiers
\d = any digit
\D = anything but not a number
\s = space
\S = anything but not a space
\w = any character
\W = anything but not a chracter
.  = any character except newline
\b = whitespace around words
\. = matches .

Modifiers:
{1,3}  = length should be 1-3
+ = match one or more
? = match 0 or 1
* = match 0 or more
$ = match the end of the string
^ = match the beginning of the string
| = matches either or or \d{1-3] | \w{1-5}
[] = range of brackets
{x} = expecting x length


White Space characters
\n = newline
\s = space
\t = tab
\e = escape
\f = form feed
\r = return

Specials
. + * ? [] $ ^ () {} | \

"""

import re

ex = '''
Jessica is 15 years old, Daniel is 27 years old.
Edward is 97 years old and his grandfather. Oscar is 102
'''

ages = re.findall(r'\d{1,3}', ex)
names = re.findall(r'[A-Z][a-z]*', ex)

print('names:',names)
print('ages', ages)

dict = {}

index = 0
for each in names:
    dict[each] = ages[index]
    index += 1

print(dict)
