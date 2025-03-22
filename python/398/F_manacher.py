S = input()
R = [0] * (2 * len(S))
S2 = [''] * (2 * len(S))
for i in range(len(S)):
  S2[2*i] = S[i]

i = 0
j = 0
while (i < len(S2)):
  while (i-j >= 0 and i+j < len(S2) and S2[i-j] == S2[i+j]):
    j += 1
  R[i] = j
  k = 1
  while (i-k >= 0 and k+R[i-k] < j):
    R[i+k] = R[i-k]
    k += 1
  i += k
  j -= k

k = 0
for i in range(len(S)-1, len(S2)):
  if R[i] >= len(S)-k:
    break
  k += 1

print(''.join(S) + ''.join(S[:k][::-1]))
