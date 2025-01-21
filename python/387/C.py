def calc2(top, utter):
    # if utter == 9999:
    #     print()
    res = 1
    utter_limit = int(str(utter)[1:])
    while utter_limit != 0:
        res *= (top - utter_limit % 10)
        utter_limit //= 10
    return res

def isxx(num):
    top = int(str(num)[0])
    for i in range(1,len(str(num))):
        if top <= num % 10:
            return False
        num = num // 10
    return True

def calc(top, length, upper_limit, utter_limit):
    # print("calcing: ", top, length, upper_limit, utter_limit)
    res = 1
    if upper_limit != 0 and utter_limit == 0:
        ans = top ** (length - 1) - calc2(top, upper_limit)
        if isxx(upper_limit):
            ans += 1
        # print(ans)
        return ans
    elif utter_limit != 0 and upper_limit == 0:
        ans = calc2(top, utter_limit)
        # print(ans)
        return ans
    elif upper_limit != 0 and utter_limit != 0:
        a = calc2(top, utter_limit)
        b = calc2(top, upper_limit)
        ans = (a - b)
        # print(ans)
        return ans
    else:
        ans = top ** (length - 1)
        # print(ans)
        return ans


L, R = input().split()
# L, R= "97","210"

min_length = len(L)
max_length = len(R)
L_start = int(L[0])
R_start = int(R[0])
l = int(L)
r = int(R)

res = 0


for length in range(min_length, max_length+1):
    if min_length == max_length:
        for top in range(L_start, R_start+1):
            max = 0
            min = 0
            if length == min_length and top == L_start:
                min = l
            if length == max_length and top == R_start:
                max = r
            res += calc(top, length, max, min)
    else:
        if length == min_length:
            for top in range(L_start, 10):
                min = 0
                if top == L_start:
                    min = l
                res += calc(top, length, 0, min)
        elif length == max_length:
            for top in range(1, R_start+1):
                max = 0
                if top == R_start:
                    max = r
                res += calc(top, length, max, 0)
        else:
            for top in range(1, 10):
                res += calc(top, length, 0, 0)

print(res)