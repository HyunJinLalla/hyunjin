import re
p = re.compile("[a-z]+")
m = p.match("python is programming language")
print(m)                  # <re.Match object; span=(0, 6), match='python'>
print(m.group())   # python
m = p.match("3 python is programming language")
print("1234567")