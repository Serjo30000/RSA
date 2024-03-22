from rsa.RSA import RSA
import sympy

rsa = RSA()

p = sympy.randprime(2**7, 2**8)
q = sympy.randprime(2**7, 2**8)

public_key, private_key = rsa.generate_keypair(p, q)

message = "Hello, RSA!"
print("Text message:", message)
encrypted_message = rsa.encrypt(public_key, message)
print("Encrypted message:", encrypted_message)

decrypted_message = rsa.decrypt(private_key, encrypted_message)
print("Decrypted message:", decrypted_message)