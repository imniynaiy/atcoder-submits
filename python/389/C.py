Q = int(input())

arr = []
sum = 0
sum_arr = [0]
deque_count = 0
deque_sum = 0

for i in range(Q):
    query = input()
    if query[0] == '2':
        deque_sum += arr[deque_count]
        deque_count += 1
    else:
        x, k = map(int, query.split())
        if x == 1:
            arr.append(k)
            sum += k
            sum_arr.append(sum)
        if x == 3:
            print(sum_arr[k + deque_count -1] - deque_sum)