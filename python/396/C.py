
def function():
    n,m = map(int, input().split())

    B = list(map(int, input().split()))
    W = list(map(int, input().split()))
    sum = 0
    count_b = 0

    B.sort(reverse=True)
    W.sort(reverse=True)

    for b in B:
        if b >=0:
            sum += b
            # print("pick B:", b)
            count_b += 1

    count_w = 0

    for w in W:
        if w < 0:
            break
        elif count_w < count_b:
            sum += w
            count_w += 1
            # print("pick W:", w)
        elif count_b < n:
            if B[count_b] + w > 0:
                sum += w + B[count_b]
                count_b += 1
                if count_b == n:
                    return sum
                count_w += 1
                if count_w == m:
                    return sum
    
    return sum
                # print("pick W and B:", w, B[count_b])

sum = function()

print(sum)