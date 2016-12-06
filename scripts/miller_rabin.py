import random
import re

def isPrime(number):
    is_prime = False
    a = random.randint(1,number-1)
    #print "n = %d, a = %d" %(number, a)
    binary_rep_str = "{0:b}".format(number-1)
    k = len(binary_rep_str)
    y = 1
    flag_1 = False
    flag_2 = False
    flag_3 = False
    matrix = "i |xi\t|z\t|y\t|y"
    #print "i |xi\t|z\t|y\t|y"
    for i in range(k):
        #matrix = "i |xi\t|z\t|y\t|y"
        z = y
        y = (y*y) % number
        y_temp = (y*y) % number
        if ((y_temp==1) and (z!=1) and (z!=(number-1))):
            matrix = matrix + "\n%d |%s\t|%d\t|%d\t|%d" %(k-i-1, binary_rep_str[i], z, y_temp, y)
            flag_1 = True
            break
        if (binary_rep_str[i]=='1'):
            y = (y*a) % number
            matrix = matrix + "\n%d |%s\t|%d\t|%d\t|%d" %(k-i-1, binary_rep_str[i], z, y_temp, y)
        else:
            matrix = matrix + "\n%d |%s\t|%d\t|%d\t|%d" %(k-i-1, binary_rep_str[i], z, y_temp, y)

    if y!=1:
        flag_2 = True
    else:
        flag_3 = True
        is_prime = True
    if flag_1 == True:
        print "line:161"
        print "n = %d, a = %d" %(number, a)
        print matrix
        print "%d is not prime because %d^2 mod %d = 1 and %d != 1 and %d != %d-1" %(number,a,number,z,z,number-1)
    if flag_2 == True:
        print "line:161"
        print "n = %d, a = %d" %(number, a)
        print matrix
        print "%d is not prime because %d^%d mod %d != 1" %(number, a,number-1,number)
    if flag_3 == True:
        is_prime = True
        print "line:169"
        print "n = %d, a = %d" %(number, a)
        print matrix
        print "%d is perhaps prime" % number
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
    return prime
