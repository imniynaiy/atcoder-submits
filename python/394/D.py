s = input()

left_bracket = []
left_arrow = []
left_square_bracket = []

for i in range(len(s)):
    ch = s[i]
    if ch == "(":
        left_bracket.append(i)
    elif ch == "<":
        left_arrow.append(i)
    elif ch == "[":
        left_square_bracket.append(i)
    elif ch == ")":
        if len(left_bracket) > 0:
            left_bracket.pop()
        else:
            print("No")
    elif ch == ">":
        if len(left_arrow) > 0:
            left_arrow.pop()
        else:
            print("No")
    elif ch == "]":
        if len(left_square_bracket) > 0:
            left_square_bracket.pop()
        else:
            print("No")
if len(left_arrow) == 0 and len(left_bracket) == 0 and len(left_square_bracket) == 0:
    print("Yes")
else:
    print("No")