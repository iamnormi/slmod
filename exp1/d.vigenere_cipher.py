import module_exp1.d_vigenere_cipher as vc

string = input("Enter the message: ")
keyword = input("Enter the keyword: ")
key = vc.generateKey(string, keyword)
encrypt_text = vc.encryption(string,key)
print("Encrypted message:", encrypt_text)
print("Decrypted message:", vc.decryption(encrypt_text, key))
