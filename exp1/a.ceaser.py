import module_exp1.a_ceaser as cs

text = input("enter string: ")
s=int(input("Enter Shift Key: "))
print("original string: ", text)
print("after encryption: ", cs.encrypt(text, s))
