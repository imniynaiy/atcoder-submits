s = input()

count = 0
i = 0

while i < len(s):
    ch = s[i]
    if i % 2 == 0:
        if ch == 'i':
            i += 1
            continue
        else:
            count += 1
            s = s[:i] + 'i' + s[i:]
    else:
        if ch == 'o':
            i += 1
            continue
        else:
            count += 1
            s = s[:i] + 'o' + s[i:]

if len(s) % 2 == 1:
    count += 1

print(count)