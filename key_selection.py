import math
from prime_checking import prime_gen

def ext_euclidean(phi, e):
    r0 = phi;
    r1 = e;
    x0 = 1;
    x1 = 0;
    y0 = 0;
    y1 = 1;
    z = [r0,x0,y0];
    while r1>0:
        r = r0%r1;
        q = (r0-r)/r1;
        x = x0-q*x1;
        y = y0-q*y1;
        z = [r1,x1,y1];
        x0 = x1;
        y0 = y1;
        x1 = x;
        y1 = y;
        r0 = r1;
        r1 = r;
    #print("\ngcd(phi(n), e=",phi, e, "=", r0, "\nWeight s: ", x0, "\nWeight t: ", y0);
    return r0, y0

def key_selection(phi):
    int_sqrt_phi = int(math.floor(math.sqrt(phi)))
    are_coprime = False
    i = 3
    while are_coprime == False:
        inverse = ext_euclidean(phi, i)
        if inverse[0] == 1:
            d = inverse[1]
            are_coprime == True
            #print "The inverse of %d mod %d is d = %d" % (i, phi, d)
            if d<0:
                d = d % phi
            return (i,d)
        else:
            i = i + 2
