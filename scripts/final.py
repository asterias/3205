from key_gen import key_gen
from certificate import certificate, signature
from helpers import int_to_str_length, fast_exp, fast_exp_trace
from random_gen import final_number
from challenge import challenge
import textwrap

pair_final_number = final_number(5)

alice_keys = key_gen()
trent_keys = key_gen()

p_a = alice_keys[0]
q_a = alice_keys[1]
n_a = alice_keys[2]
e_a = alice_keys[3]
d_a = alice_keys[4]

p_t = trent_keys[0]
q_t = trent_keys[1]
n_t = trent_keys[2]
e_t = trent_keys[3]
d_t = trent_keys[4]

name = " Alice"

certificate_a = certificate(name, alice_keys, trent_keys)

signature_t = signature(trent_keys[4], certificate_a[2], trent_keys[2])

challege_demo = challenge(13)
k = challege_demo[0]
u = challege_demo[1]
u_bin = challege_demo[2]

byte_array_u = textwrap.wrap(u_bin, 8)
xor_u = int(byte_array_u[0],2)
for i in range(1,len(byte_array_u)):
    xor_u = xor_u ^ int(byte_array_u[i],2)

h_u = '{0:b}'.format(xor_u)

if len(h_u) < 32:
    xor = (32-len(h_u))*'0' + h_u

v = fast_exp(int(h_u,2), d_a, n_a)
Ev = fast_exp(v, e_a, n_a )

print "line:143"
for bits in pair_final_number[2]:
    print bits
print 'Number' + '|', pair_final_number[1], '|' ,pair_final_number[0]

print " "

print "line:205"
print "d = %d" %d_a
print " "
print "line:209"
print "p = %d, q = %d, n = %d, e = %d, d = %d" %(p_a, q_a, n_a, e_a, d_a)
print "p = %s" % int_to_str_length(p_a,32)
print "q = %s" % int_to_str_length(q_a,32)
print "n = %s" % int_to_str_length(n_a,32)
print "e = %s" % int_to_str_length(d_a,32)
print "d = %s" % int_to_str_length(p_a,32)

print " "

print "line:218"
print "p = %d, q = %d, n = %d, e = %d, d = %d" %(p_t, q_t, n_t, e_t, d_t)
print "p = %s" % int_to_str_length(p_t,32)
print "q = %s" % int_to_str_length(q_t,32)
print "n = %s" % int_to_str_length(n_t,32)
print "e = %s" % int_to_str_length(d_t,32)
print "d = %s" % int_to_str_length(p_t,32)

print " "

print "line:243"
print "r = %s" % certificate_a[2]
print "h(r) = %s" % certificate_a[3]
print "s = %s" % signature_t[1]

print " "

print "line:246"
print "h(r) = %d, s = %d" % (int(certificate_a[3],2), signature_t[0])

print " "

print "line:271"
print "k = %d, u = %d" %(k, u)

print " "

print "line:274"
print "u = %s" %u_bin

print " "

print "line:281"
print "u = %d, h(u) = %d, v = %d, Ev = %d" %(u,int(h_u,2),v,Ev)

print " "

print "line:285"
fast_exp_trace(v, e_a, n_a)
