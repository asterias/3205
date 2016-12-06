import random

def isPrime(number):
    is_prime = False
    a = random.randint(1,number-1)
    print a
    binary_rep_str = "{0:b}".format(number-1)
    k = len(binary_rep_str)
    print binary_rep_str
    y = 1
    print "i |xi\t|z\t|y\t|y"
    for i in range(k):
        z = y
        y = (y*y) % number
        if ((y==1) and (z!=1) and (z!=(number-1))):
            print number, "is not prime because %d^2 mod %d = 1 and %d != 1 and %d != %d-1" %(y,number,z,z,number-1)
            return 0
        if (binary_rep_str[i]=='1'):
            y = (y*a) % number
        print "%d |%s\t|%d\t|%d\t|%d" %(k-i-1, binary_rep_str[i], z, y, y)
    if y!=1:
        print number, "is not prime because %d^%d mod %d != 1" %(a,number-1,number)
    else:
        is_prime = True
        print number, "is perhaps prime"
    return is_prime

def prime_loop(number,times):
    results = []
    prime = False
    for i in range(times):
        results.append(isPrime(number))
        if results[i] == False:
            prime = False
            break
        else:
            prime = True
    if prime == True:
        print "Passed", len(results), "tests"
    else:
        print "Failed on test:", i+1
    return prime
