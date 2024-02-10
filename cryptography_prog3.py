from cryptography.fernet import Fernet

choice = input("Please choose an option\n\
A) Encrypt a message\nB) Decrypt a message\n\
Type A or B: ")

if choice.lower() == "a":
    message = input("Please enter a message: ")
    
    key = Fernet.generate_key()
    fernet_obj = Fernet(key)
    encrypted_message = fernet_obj.encrypt(message.encode())
    print(f"This is the message: {encrypted_message}")
    print(f"This is the key: {key}")

if choice.lower() == "b":
    encrypted_message = input("Please enter the encrypted message: ")
    key = input("Please enter a valid key to decode the message: ")

    fernet_obj = Fernet(key)
    decrypted_message = fernet_obj.decrypt(encrypted_message)
    print(f"Here is the message: {decrypted_message}")