def machine():
    keys = "abcdefghijklmnopqrstuvwxyz ,.!?"
    value = keys[10:] + keys[:10]

    encrypt_dic = dict(zip(keys, value))
    decrypt_dic = dict(zip(value, keys))

    message = input("Enter message: ")

    encrypted_message = ''.join([encrypt_dic[characters]
                                    for characters in message.lower()])
    
    print(encrypted_message)

    decrypted_message = ''.join([decrypt_dic[characters]
                                    for characters in encrypted_message])
    
    return decrypted_message.capitalize()

print(machine())