n, r, c = map(int, input().split())
s = input()

smokes = [[0,0]]

for dir in s:
    hasSmoke = 0
    if dir == 'N':
        for smoke in smokes:
                smoke[0] -= 1
                if smoke[0] == r and smoke[1] == c:
                    hasSmoke = 1
        smokes.append([0, 0])
    elif dir == 'S':
        for smoke in smokes:
                smoke[0] += 1
                if smoke[0] == r and smoke[1] == c:
                    hasSmoke = 1
        smokes.append([0, 0])
    elif dir == 'E':
        for smoke in smokes:
                smoke[1] += 1
                if smoke[0] == r and smoke[1] == c:
                    hasSmoke = 1
        smokes.append([0, 0])
    else:
        for smoke in smokes:
                smoke[1] -= 1
                if smoke[0] == r and smoke[1] == c:
                    hasSmoke = 1
        smokes.append([0, 0])
    print(hasSmoke, end='')