"""
question no 1

str1 = "krishna"
str2 = "veni"

output = "kvreinsihna"
"""


str1 = "dha" # 7
str2 = "venit" # 4
output=""

i = 0
while i < len(str2):
    output += str1[i]+str2[i]
    i += 1

output += str1[i:]

print(output)


