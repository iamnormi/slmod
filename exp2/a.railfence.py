import module_exp2.a_railfence as rf

plain_text=input("Enter the string to be encrypted: ")
n=int(input("Enter the number of rails: "))
rf.encrypt(plain_text,n)

cipher_text=input("Enter the string to be decrypted: ")
n=int(input("Enter the number of rails: "))
rf.decrypt(cipher_text,n)
