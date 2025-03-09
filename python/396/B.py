q = int(input())

stack = []

for _ in range(q):
    str = input()
    if str[0] == '1':
        _, x = map(int, str.split())
        stack.append(x)
    elif str[0] == '2':
        if len(stack) == 0:
            print(0)
        else:
            print(stack[-1])
            stack.pop()