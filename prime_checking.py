from miller_rabin import prime_loop
from random_gen import final_number

prime_pair = []
both_prime = False
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
