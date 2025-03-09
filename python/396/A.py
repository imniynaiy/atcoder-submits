n = int(input())
a = list(map(int, input().split()))

last_i = -1
count = 0

for i in a:
    if last_i == i:
        count += 1
        if count == 2:
            print('Yes')
            exit()
    else:
        count = 0
    last_i = i

if count <= 1:
    print('No')