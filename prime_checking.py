from miller_rabin import *
from random_gen import *

prime_pair = []
both_prime = False
i = 0
def prime_gen():
    while both_prime == False:
        number = final_number(5)[1]
        times = 20

        final_prime = prime_loop(number, times)

        if final_prime == True:
            prime_pair.append(number)
            if len(prime_pair) == 2:
                if prime_pair[0] == prime_pair[1]:
                    prime_pair.pop()
                else:
                    both_prime == True
                    p , q = prime_pair
                    return p, q

t,r = prime_gen()
print "primes are: ", t,r
