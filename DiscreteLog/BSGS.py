#  A baby-step giant-step

import math


def russian_peasant(x, y, z):
    s = 1
    while x > 0:
        if x % 2 == 1:
            s = (s*y) % z
        x = x//2
        y = (y*y) % z;
    return int(s)


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = egcd(b % a, a)
        return g, y - (b // a) * x, x


def compute_m(p):
    m = math.ceil(math.sqrt(p-1))
    return m


def baby_list(g, p):
    m = int(compute_m(p))
    # b = list(range(0, m))
    # s = map((lambda x: pow(g, x, p)), b)  # create list of powers
    # x = dict(zip(s, b))  # zip list of powers and positions into a dictionary
    #

    # Faster
    x = dict()
    pow_ = 1
    for i in range(0, m):
        x[pow_] = i
        pow_ = pow_ * g % p

    return x


def compare_giant(y, g, p):
    if y == 1:
        return 0
    hash_table = baby_list(g, p)
    m = int(compute_m(p))
    _, inv, _ = egcd(g, p)
    inv = inv % p
    a = russian_peasant(m, inv, p)
    z = y
    for i in range(1, m):
        z = (z * a) % p
        if z in hash_table:
            return i * m + hash_table[z]
