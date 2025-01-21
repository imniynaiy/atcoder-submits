H,c1,c2= input().split()
H = int(H)
S = input()
Result = ""
for ch in S:
  if ch == c1:
    Result += ch
  else:
    Result += c2

print(Result)