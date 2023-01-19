#!pip install pycrypto
#AES
import modulefortfsse.AES_exp4 as aes

key=input("Enter the key: ")
c=aes.AESCipher(key)
plain_text=input("Enter the message: ")
print("The message is: ", plain_text)

cipher=c.encrypt(plain_text)
print("Encrypted message is: ",cipher)

dec=c.decrypt(cipher)
print("Decrypted message is: ",dec)
