import random
import math
import time
import sys
from itertools import combinations
from functools import reduce
from operator import mul

sys.set_int_max_str_digits(0) # 在IDLE Python中使用这句

def pollard_rho(n):
    """使用 Pollard's Rho 算法寻找 n 的一个因数"""
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    if n % 5 == 0:
        return 5

    # 定义随机函数 f(x) = (x^2 + c) % n
    while True:
        c = random.randint(1, n - 1)
        f = lambda x: (pow(x, 2, n) + c) % n

        x, y, d = 2, 2, 1
        while d == 1:
            x = f(x)
            y = f(f(y))
            d = math.gcd(abs(x - y), n)

        if d != n:  # 找到一个非平凡因数
            return d

def factor(n):
    """递归分解整数 n，返回其所有质因数"""
    factors = []
    if n == 1:
        return factors
    if is_prime(n):  # 如果 n 是质数，直接加入因数列表
        factors.append(n)
        return factors
    d = pollard_rho(n)
    factors += factor(d)  # 递归分解因数 d
    factors += factor(n // d)  # 递归分解 n // d
    return sorted(factors)  # 返回排序后的因数列表

def is_prime(n):
    """判断一个整数是否为质数"""
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def get_all_combinations(lst):
    result = []
    for r in range(1, len(lst) + 1):  # 生成不同长度的组合
        result.extend(combinations(lst, r))
    return result

def reduce_to_product(lst_of_lists):
    return [reduce(mul, sublist, 1) for sublist in lst_of_lists]

n = int(input())
prime_factors = factor(n)

all_factors = reduce_to_product(get_all_combinations(prime_factors))

all_factors = [1] + all_factors + [n]

all_factors = list(dict.fromkeys(all_factors))

def check(f, n):
    c = n / f
    to_sqrt = 3 * 4 * c - 3 * f ** 2
    if to_sqrt < 0:
        return False, 0, 0
    b = 1/6 * (math.sqrt(to_sqrt) - 3 * f)
    a = b + f
    if b == int(b) and b >= 1:
        return True, b+f, b
    return False, 0, 0

for f in all_factors:
    can, a,b = check(f, n)
    if can:
        print(""+ str(int(a)) + " "+ str(int(b)))
        exit()

print(-1)