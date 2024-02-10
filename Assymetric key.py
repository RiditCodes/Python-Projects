import rsa

message = input("Enter a message: ")

publicKey, privateKey = rsa.newkeys(500)
print(publicKey, privateKey)

print()
encrypted_message = rsa.encrypt(message.encode(), publicKey)
print(encrypted_message)

print()
decrypted_message = rsa.decrypt(encrypted_message, privateKey).decode()
print(decrypted_message)