from prime_checking import prime_gen
from key_selection import key_selection

def key_gen():
    p,q = prime_gen()

    n = p*q
    phi = (p-1)*(q-1)

    e,d = key_selection(phi)

    return p, q, n, e, d
