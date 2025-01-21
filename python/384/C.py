abcde = [int(num) for num in input().split()]

result = []

for i in range(1,32):
    k = i
    sum = 0
    string = ""
    for j in range(5):
        if k % 2 == 1:
            sum += abcde[j]
            string += "ABCDE"[j]
        k = k >> 1
    result.append((sum,string))

sorted_data = sorted(result, key=lambda x: (-x[0], x[1]))
for d in sorted_data:
    print(d[1])