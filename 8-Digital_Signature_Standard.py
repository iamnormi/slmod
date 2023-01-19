import modulefortfsse.Digital_Signature_Standard_exp8 as dss

print ("First create a text file with some text in it")
print ("If Already done continue/ If Not: Press Ctrl+c ")
global_var=dss.parameter_generation()
keys=dss.per_user_key(global_var[0],global_var[1],global_var[2])

# Sender's side (signing the document):
print()
file_name=input("Enter the name of document to sign: ")
components=dss.signature(file_name,global_var[0],global_var[1],global_var[2],keys[0])

print("r(Component of signature) is: ",components[0])
print("k(Randomly chosen number) is: ",components[2])
print("s(Component of signature) is: ",components[1])

# Receiver's side (verifying the sign):
print()
file_name=input("Enter the name of document to verify: ")
dss.verification(file_name,global_var[0],global_var[1],global_var[2],components[0],components[1],keys[1])
