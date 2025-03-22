S = input()

lenS = len(S)

start = lenS // 2
mid = lenS
for i in range(start, lenS-1):
    si = S[i+1:]
    sii = S[i-(lenS-i -1):i][::-1]
    if si == sii:
        mid = start
        break
    sii = S[i-(lenS-i-2):i+1][::-1]
    if si == sii:
        mid = start + 0.5
        break

if mid == lenS:
    print(S[:-1] + S[::-1])
elif mid - int(mid) == 0:
    s = S[:mid]
    print(s + S[mid] + s[::-1])
else:
    s = S[:int(mid)+1]
    print(s + s[::-1])