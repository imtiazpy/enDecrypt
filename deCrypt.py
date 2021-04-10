from cryptography.fernet import Fernet
from keyLoader import load_key

encrypted_message = b'gAAAAABgcYCpkJejjc6pFK1wIB4wMEgiMIH8XUdB7JEALd6rmR555-vOmJAkAGyJPAqnT_-wqpfY16wKoVGhoiYGIdmy1-fGk_ifVdZmQ_epwAdqXQ5t8D0='
key = load_key()

f = Fernet(key)

decrypted_encrypted = f.decrypt(encrypted_message)
print(decrypted_encrypted)
