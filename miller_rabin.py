import random

def primality_testing(number):
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
        print number, "is perhaps prime"

primality_testing(9767)
