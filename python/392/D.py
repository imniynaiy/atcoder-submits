n = int(input())
A = []
K = []

face_map = {}

for i in range(n):
    str = input().split()
    k = int(str[0])
    K.append(k)
    a = [int(num) for num in str[1:]]
    A.append(a)
    for j in a:
        if j in face_map:
            face_map[j][i] += 1
        else:
            face_map[j] = [0] * n
            face_map[j][i] += 1

face_p = []

for _, j in enumerate(face_map):
    for k in range(n):
        face_map[j][k] = face_map[j][k] / K[k]
    face_p.append(face_map[j])

result = -1

def get_same_face_p(face_p, i, j):
    same_face_p = 0
    for k in range(len(face_p)):
        if face_p[k][i] == 0 or face_p[k][j] == 0:
            continue
        same_face_p += face_p[k][i] * face_p[k][j]
    return same_face_p

for i in range(n):
    for j in range(i+1, n):
        same_face_p = get_same_face_p(face_p, i, j)
        if result < same_face_p:
            result = same_face_p

print(result)


