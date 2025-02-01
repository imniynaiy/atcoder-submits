N,Q = map(int, input().split())

bird_i_in_cage = list(range(1,N+1))
cage_i_has_bird = []
for i in range(N):
    cage_i_has_bird.append([i+1])

even = 0

for i in range(Q):
    str = input()
    if str[0] == '2':
        print(even)
    else:
        _, P,H = map(int, str.split())
        cage = bird_i_in_cage[P-1] - 1
        source_count = len(cage_i_has_bird[P-1])
        target_count = len(cage_i_has_bird[cage])
        if source_count == 1:
            even += 1
        elif source_count % 2 == 0:
            if target_count % 2 == 0:
                even -= 1
            else:
                even -= 2
        elif source_count % 2 != 0 and target_count % 2 != 0:
            even += 2
        bird_i_in_cage[P-1] = H
        cage_i_has_bird[cage].remove(P)
        cage_i_has_bird[H].append(P)

