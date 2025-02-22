s = input() 

index = s.find("WA")

while index != -1:
    s = s[0:index] + "AC" + s[index+2:]
    index = s.find("WA")

print("".join(s))