n = int(input())

s = ['?'] * n

if n % 2 == 0:
    for i in range(n):
        if i == n // 2- 1 or i == n // 2 :
            s[i] = '='
        else:
            s[i] = '-'
else:
    for i in range(n):
        if i == n // 2:
            s[i] = '='
        else:
            s[i] = '-'

print(''.join(s))