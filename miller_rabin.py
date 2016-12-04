import random

def isPrime(number):
    is_prime = False
    a = random.randint(1,number-1)
    print a
    binary_rep_str = "{0:b}".format(number-1)
    k = len(binary_rep_str)
    print binary_rep_str, k
    y = 1
    for i in range(k):
        print i, binary_rep_str[i]
        z = y
        print z
        y = (y*y) % number
        print y
        if ((y==1) and (z!=1) and (z!=(number-1))):
            print number, "is not prime"
            return 0
        if (binary_rep_str[i]=='1'):
            y = (y*a) % number
    print "Y is", y
    if y!=1:
        print number, "is not prime"
    else:
        is_prime = True
        print number, "is perhaps prime"
    return is_prime

test = []
for i in range(20):
    test.append(isPrime(9767))
    is_prime = False
    if test[i] == False:
        is_prime = False
        break
    else:
        is_prime = True
if is_prime == True:
    print "Passed", len(test), "tests"
else:
    print "Failed on", i+1, "test"
