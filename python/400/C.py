n = int(input())

xset = set()

a = 1
b = 1

x = 2 ** a * b ** 2
# print('adding', a, b , x)
xset.add(x)
while x <= n:
    while x <= n:
        b += 1
        x = (2 ** a) * (b ** 2)
        if x <= n:
            # print('adding', a, b , x)
            xset.add(x)
    if x > n:
        b = 1
        a += 1
        x = (2 ** a) * (b ** 2)
        if x <= n:
            # print('adding', a, b , x)
            xset.add(x)

print(len(xset))
