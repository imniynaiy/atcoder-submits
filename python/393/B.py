import math


s = input()

count = 0

for j in range(1,math.ceil(len(s)/2)+1):
    for i in range(len(s)-2):
        pa = i
        pb = i +j
        pc = i + 2*j
        if pb >= len(s) or pc >= len(s):
            break
        if s[pa] == "A" and s[pb] == "B" and s[pc] == "C":
            count += 1

print(count)