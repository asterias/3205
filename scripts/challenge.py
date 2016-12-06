from random_gen import lsb_loop
import math

def challenge(k):
    challenge_a_len = int(math.floor(k/2.0))
    challenge_b_len = int(math.ceil(k/2.0))

    zip_challenge_a = lsb_loop(challenge_a_len)
    zip_challenge_b = lsb_loop(challenge_b_len)

    challenge_a = []
    challenge_b = []
    for i,j in zip_challenge_a:
        challenge_a.append(j)

    for m,n in zip_challenge_b:
        challenge_b.append(n)

    challenge_ab = challenge_a + challenge_b
    str_challenge = (32-k)*'0' + ''.join(challenge_ab)
    u = int(str_challenge,2)

    return k, u, str_challenge
