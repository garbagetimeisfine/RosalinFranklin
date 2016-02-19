import re

my_string = "a given string"

m = re.search(r'\s\w*', my_string)
print(m)
n = re.search(r'\d', my_string)
print(n)
