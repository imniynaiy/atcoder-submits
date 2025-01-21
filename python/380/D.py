S = input()
Q = input()
K = [int(num) for num in input().split()]

Slen = len(S)
for k in K:
    k2  = k - 1
    n = k2 % Slen
    r = int.bit_count(k2//Slen) % 2
    if r == 1:
        print(S[n].swapcase(),end=' ')
    else:
        print(S[n], end=' ')