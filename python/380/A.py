str = input()
count1 = 0
count2 = 0
count3 = 0

for ch in  str:
    if ch == '1':
        count1 += 1
    if ch == '2':
        count2 += 1
    if ch == '3':
        count3 += 1

if (count1 == 1) & (count2 == 2) & (count3 == 3):
    print("Yes")
else:
    print("No")