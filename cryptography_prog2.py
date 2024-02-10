from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)

message = "If you are reading this, believe me, the world is just a simulation."

fernet_obj = Fernet(key)

encrypted_message = fernet_obj.encrypt(message.encode())

print()
print(encrypted_message)

decrypted_message = fernet_obj.decrypt(encrypted_message).decode()

print()
print(decrypted_message)