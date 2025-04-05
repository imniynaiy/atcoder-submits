n = int(input())

xset = {}  # Use a dictionary instead of a set

a = 1
b = 0

twoxxa = []

x = 1
while x < n:
    x *= 2
    twoxxa.append(x)

bsquare = []
x = 0
while x < n // 2:
    x += 2 * b + 1
    b += 1
    bsquare.append(x)

i = 0
j = 0
if i >= len(twoxxa):
    print(0)
    exit()
if j >= len(bsquare):
    print(0)
    exit()

x = twoxxa[i] * bsquare[j]
# print('adding', twoxxa[i], bsquare[j], x)
xset[x] = True  # Add to dictionary

while x <= n:
    while x <= n:
        j += 1
        x = twoxxa[i] * bsquare[j]
        if x <= n:
            # print('adding', twoxxa[i], bsquare[j], x)
            xset[x] = True  # Add to dictionary
    if x > n:
        j = 0
        i += 1
        if i >= len(twoxxa):
            break
        x = twoxxa[i] * bsquare[j]
        if x <= n:
            # print('adding', twoxxa[i], bsquare[j], x)
            xset[x] = True  # Add to dictionary

print(len(xset))  # Output the size of the dictionary
