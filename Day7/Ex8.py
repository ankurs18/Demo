import re

s1='Sample input string'

result = re.match('Sample', s1)
print(result)

result = re.match('input', s1)
print(result)

result = re.search('input', s1)
print(result)

all = re.findall('\w{6}', s1)
print(result)

all = re.findall('\w{5}', s1)
print(result)

all = re.findall('\w{5,}', s1)
print(result)