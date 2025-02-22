s = input()

last_ch = ''

i = 0

while i < len(s):
    ch = s[i]
    if ch == ">":
        if last_ch == "<":
            s = s[:i-1] + s[i+1:]
            if len(s) > 0:
                if i >= 2:
                    last_ch = s[i-2]
                    i -= 1
                else:
                    last_ch = ''
                    i = 0
            else:
                last_ch = ''
                print("Yes")
                exit()
        else:
            last_ch = ch
            i+=1
    elif ch == "]":
        if last_ch == "[":
            s = s[:i-1] + s[i+1:]
            if len(s) > 0:
                if i >= 2:
                    last_ch = s[i-2]
                    i -= 1
                else:
                    last_ch = ''
                    i=0
            else:
                last_ch = ''
                print("Yes")
                exit()
        else:
            last_ch = ch
            i+=1
    elif ch == ")":
        if last_ch == "(":
            s = s[:i-1] + s[i+1:]
            if len(s) > 0:
                if i >= 2:
                    last_ch = s[i-2]
                    i-=1
                else:
                    last_ch = ''
                    i = 0
            else:
                last_ch = ''
                print("Yes")
                exit()
        else:
            last_ch = ch
            i+=1
    else: 
        last_ch = ch
        i+=1

if len(s) == 0:
    print("Yes")
else:
    print("No")