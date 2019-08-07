import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

matches1 = re.search(r'[a-z].*', text_to_search)
matches2 = re.search(r'[A-Z].*', text_to_search)
matches3 = re.search(r'\d{10}', text_to_search)
matches4 = re.search(r'[A-Z][a-z]\s[A-Z].*', text_to_search)
matches5 = re.search(r'[a-z].*\.[a-z].*', text_to_search)
matches6 = re.search(r'\d{3}-\d{3}-\d{4}', text_to_search)
matches7 = re.search(r'\d{3}\*\d{3}\*\d{4}', text_to_search)
matches8 = re.search(r'[A-Z][a-z]\s[A-z][a-z].*',text_to_search)

print(matches1.group())
print(matches2.group())
print(matches3.group())
print(matches4.group())
print(matches5.group())
print(matches6.group())
print(matches7.group())
print(matches8.group())


