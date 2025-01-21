N = int(input())

i=0
while N > 1:
    i += 1
    N = N // i

print(i)