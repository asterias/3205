from prime_checking import *
from key_selection import *

def key_gen():
    p,q = prime_gen()

    n = p*q
    phi = (p-1)*(q-1)

    e,d = key_selection(phi)
    print "p = %d, q = %d, n = %d, e = %d, d = %d" %(p, q, n, e, d)

    str_p = format(p,'b')
    if len(str_p) < 32:
        str_p = (32-len(str_p))*'0' + str_p

    str_q = format(q,'b')
    if len(str_q) < 32:
        str_q = (32-len(str_q))*'0' + str_q

    str_n = format(p,'b')
    if len(str_n) < 32:
        str_n = (32-len(str_n))*'0' + str_n

    str_e = format(p,'b')
    if len(str_e) < 32:
        str_e = (32-len(str_e))*'0' + str_e

    str_d = format(d,'b')
    if len(str_d) < 32:
        str_d = (32-len(str_d))*'0' + str_d

    print "p = %s" % str_p
    print "q = %s" % str_q
    print "n = %s" % str_n
    print "e = %s" % str_e
    print "d = %s" % str_d

    return p, q, n, e, d

p,q = prime_gen()
print p,q    
