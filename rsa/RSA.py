import random
import sympy

class RSA:
    def generate_keypair(self, p, q):
        n = p * q
        phi = (p - 1) * (q - 1)
        e = random.randint(1, phi - 1)
        while sympy.gcd(e, phi) != 1:
            e = random.randint(1, phi - 1)
        d = sympy.mod_inverse(e, phi)
        return ((e, n), (d, n))

    def encrypt(self, public_key, plaintext):
        e, n = public_key
        cipher = [pow(ord(char), e, n) for char in plaintext]
        return cipher

    def decrypt(self, private_key, ciphertext):
        d, n = private_key
        plain = [chr(pow(char, d, n)) for char in ciphertext]
        return ''.join(plain).encode('latin1').decode('utf-8')
