from prime_checking import *

def key_gen():
    primes = prime_gen()

    p = primes[0]
    q = primes[1]
    n = p*q
    phi = (p-1)*(q-1)

    
