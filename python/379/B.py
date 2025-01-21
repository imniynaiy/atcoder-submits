N, K = map(int, input().split())
str = input()
count = 0
result = 0

for i in range(N):
    if str[i] == "O":
        count+=1
    else:
        count = 0
    if count == K:
        count = 0
        result +=1

print(result)