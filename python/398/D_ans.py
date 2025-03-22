def main():
    n, r, c = map(int, input().split())
    s = input()
    t = [r, c]
    f = [0, 0]
    st = set()
    st.add(tuple(f))

    for nx in s:
        if nx == 'N':
            t[0] += 1
            f[0] += 1
        elif nx == 'W':
            t[1] += 1
            f[1] += 1
        elif nx == 'S':
            t[0] -= 1
            f[0] -= 1
        else:
            t[1] -= 1
            f[1] -= 1

        st.add(tuple(f))
        if tuple(t) not in st:
            print("0", end="")
        else:
            print("1", end="")
    print()

if __name__ == "__main__":
    main()