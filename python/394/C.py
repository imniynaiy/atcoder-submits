s = list(input())

i = 0

compareA = False

while i < len(s):
    if compareA == True:
        if s[i] == "A":
            s[i-1] = 'A'
            s[i] = 'C'
            compareA = False
            if i >= 2:
                if s[i-2] == "W":
                    compareA = True
                    i -= 1
                else:
                    i+=1
            else:
                i+=1
        elif s[i] == "W":
            compareA = True
            i += 1
        else:
            i += 1
            compareA = False
    else:
        if s[i] == "W":
            compareA = True
        i += 1

print("".join(s))