import module_exp2.b_row_and_column as rc

msg=input("Enter the message: ")
key=input("Enter the key in alphabets: ")
rc.encrypt(msg,key)

msg=input("Enter the message to be decrypted: ")
key=input("Enter the key in alphabets: ")
rc.decrypt(msg,key)
