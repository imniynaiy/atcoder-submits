stri = input()
count = 0

for ch in stri[1:]:
    if ch == '-':
        count += 1
    if ch == '|':
        print(str(count), end=" ")
        count = 0