N, K = map(int, input().split())
S = input()

count = 0
lastCh = ''
last1length = 0
last0length = 0

for i in range(N):
    ch = S[i]
    if i == 0:
        if ch == '0':
            lastCh  = ch
            print(ch, end='')
            continue
        if ch == '1':
            count += 1
            if count != K-1:
                lastCh = ch
                print(ch, end='')
                continue
            if count == K-1:
                lastCh = ch
                last1length += 1
                continue
    if ch == '1':
        if lastCh != '1':
            count += 1
    if count != K and count != K-1:
        lastCh = ch
        print(ch, end='')
        continue
    if count == K-1:
        if ch == '1':
            last1length += 1
        if ch == '0':
            last0length += 1
    if count == K:
        if ch == '1':
            last1length += 1
        if ch == '0':
            if lastCh == '0':
                print(ch, end='')
            if lastCh == '1':
                print("1" * last1length, end='')
                print("0"* last0length, end='')
                last1length = 0
                last0length = 0
                print(ch, end='')
    lastCh  = ch
if last1length != 0 or last0length != 0:
        print("1" * last1length, end='')
        print("0"* last0length)