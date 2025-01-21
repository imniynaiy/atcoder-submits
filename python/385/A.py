A = input().split()

count_map = {}
 
for item in A:
    if item in count_map:
        count_map[item] += 1
    else:
        count_map[item] = 1

count = len(count_map.keys())

if count > 2 or count < 2:
    print("No")
    exit()

a, b = count_map.values()

if a == 2 and b == 2:
    print("Yes")
elif a == 1 and b == 3:
    print("Yes")
elif a == 3 and b == 1:
    print("Yes")
else:
    print("No")



