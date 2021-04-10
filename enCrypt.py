from cryptography.fernet import Fernet

from keyGenerator import write_key
from keyLoader import load_key

# Generate the key
write_key()

# load the previously generated key
key = load_key()

# Message that we want to encrypt.
message = "Python is awesome.".encode()

# initialize the Fernet class
f = Fernet(key)

# encrypt the message
encrypted = f.encrypt(message)

# print how it looks
print(encrypted)
