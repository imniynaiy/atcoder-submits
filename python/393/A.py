r12, r13 = input().split()

if r12 == r13 == "sick":
    print("1")
elif r12 == r13 == "fine":
    print("4")
elif r12 == "sick" and r13 == "fine":
    print("2")
else:
    print("3")