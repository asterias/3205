from helpers import str_to_bin, fast_exp
from key_gen import key_gen
import textwrap

def certificate(name, alice_keys, trent_keys):
    name_bin = str_to_bin(name)
    if len(name_bin) < 48:
        name_bin = (48-len(name_bin))*'0' + name_bin

    n = alice_keys[2]
    e = alice_keys[3]

    binary_str_n = "{0:b}".format(n)
    if len(binary_str_n) < 32:
        binary_str_n = (32-len(binary_str_n))*'0' + binary_str_n

    binary_str_e = "{0:b}".format(e)
    if len(binary_str_e) < 32:
        binary_str_e = (32-len(binary_str_e))*'0' + binary_str_e

    r = name_bin + binary_str_n + binary_str_e

    byte_array = textwrap.wrap(r, 8)

    xor = int(byte_array[0],2)
    for i in range(1,len(byte_array)):
        xor = xor ^ int(byte_array[i],2)

    xor = '{0:b}'.format(xor)

    if len(xor) < 32:
        xor = (32-len(xor))*'0' + xor


    return alice_keys, trent_keys, r, xor

def signature(trent_key, r_hash, n):
    key = int(trent_key)
    n = int(n)
    r_hash = int(r_hash,2)

    signature = fast_exp(r_hash, key, n)
    signature_bin = format(signature,'b')
    if len(signature_bin) < 32:
        signature_bin = (32-len(signature_bin))*'0' + signature_bin

    return signature, signature_bin
