#\-original sybol value
#[]-set of value given
#^-start with given letter
#$ ending with given letter
#. is iser to sprit a string in single letter
#or is used any one  is there
# * 0 or more time is in  strig
#+ is aleast one time
#string{m,n}
#() grouping
import re
a='this is string.'
match=re.search('is',a)
print(match)
match=re.findall('\.',a)
print(match)
a='ab abca cef'
match=re.findall('[bcz]',a)
print(tuple(match))
match=re.search('^A',a)
print(match)
match=re.search('f$',a)
print(match)

match=re.search('a|b',a)
print(match)
a='12 34 567 89 0'
match=re.search('57?',a)
print(match)

str='new year is it\'s me.'
print(str)