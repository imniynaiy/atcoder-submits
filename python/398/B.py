A = list(map(int, input().split()))

m = {}

for a in A:
    if a in m:
        m[a] += 1
    else:
        m[a] = 1

count3 = 0
count2 = 0

for k in m:
    if m[k] >= 3:
        count3 += 1
    elif m[k] == 2:
        count2 += 1

if count3 > 0 and count2 > 0:
    print("Yes")
elif count3 > 1:
    print("Yes")
else:
    print("No")