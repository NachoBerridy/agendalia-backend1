from cryptography.fernet import Fernet
import base64
import os

# Genera una clave Fernet
key = Fernet.generate_key()

# Codifica la clave en base64
encoded_key = base64.urlsafe_b64encode(key)

print("Fernet Key:", encoded_key.decode('utf-8'))