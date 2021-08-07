import math
import euclidean
import random
import prime_generator
def square_and_multiply(x, k, p=None):
    b = bin(k).lstrip('0b')
    r = 1
    for i in b:
        r = r**2
        if i == '1':
            r = r * x
        if p:
            r %= p
    return r
    
def generator(n):
    
    p = prime_generator.generate_primes(n=n, k=1)[0]
    q = prime_generator.generate_primes(n=n, k=1)[0]
    n = p * q
    
    phi_n = (p - 1) * (q - 1)
    
    while True:
        e = random.randrange(1, phi_n-1)
        if math.gcd(e, phi_n) == 1:
            
            gcd, s, t = euclidean.euclidean_calculator(phi_n, e)
            if gcd == (s*phi_n + t*e):
                d = t % phi_n
                break
    return (e, n, d)

def encrypt(x, publicKey):
    e, n = publicKey
    assert x < n

    y = square_and_multiply(x, e, n)
    return y
    
def decrypt(y, privateKey):
    d, n = privateKey
    assert y < n

    x = square_and_multiply(y, d, n)
    return x