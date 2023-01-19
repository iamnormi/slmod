import module_exp1.c_hillcipher as hc

msg = input("Message: ")
encrypted_msg = hc.encrypt(msg)
print(encrypted_msg)
decrypted_msg = hc.decrypt(encrypted_msg)
print(decrypted_msg)
