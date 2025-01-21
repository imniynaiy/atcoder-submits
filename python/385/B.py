S=input()

count = 0

i= 0
while i < len(S):
    if S[i] != '0':
        count+=1
    else:
        if i < len(S) -1 and S[i+1] == '0':
            count+=1
            i+=1
        else:
            count+=1
    i+=1

print(count)