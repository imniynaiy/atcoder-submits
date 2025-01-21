
def check(S,T):
    i = 0
    hasSkip = False
    while i < len(T):
        if not(hasSkip):
            if S[i] == T[i]:
                i += 1
                continue
            else:
                hasSkip = True
                continue
        else:
            if S[i+1] == T[i]:
                i +=1
                continue
            else:
                print("No")
                return
    print("Yes")

def check2(S,T):
    i = 0
    count = 0
    while i < len(S) and count < 2:
        if S[i] != T[i]:
            count += 1
        i+=1
    if count < 2:
        print("Yes")
    else:
        print("No")    
    

K = int(input())
S = input()
T = input()

if len(S) != len(T):
    if len(S) - len(T) == 1:
        check(S, T)
        exit()
    elif len(S) - len(T) == -1:
        check(T, S)
        exit()
    else:
        print("No")
else:
    check2(S, T)
    exit()

        