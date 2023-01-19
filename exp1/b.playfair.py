import module_exp1.b_playfair as pf

text_Plain = input("Enter Plain Text...: ")
text_Plain = pf.removeSpaces(pf.toLowerCase(text_Plain))
PlainTextList = pf.Diagraph(pf.FillerLetter(text_Plain))
if len(PlainTextList[-1]) != 2:
    PlainTextList[-1] = PlainTextList[-1]+'z'

key = input("Enter Key...: ")
key = pf.toLowerCase(key)
list1 = pf.list1
Matrix = pf.generateKeyTable(key, list1)

print("Plain Text:", text_Plain)
CipherList = pf.encryptByPlayfairCipher(Matrix, PlainTextList)

CipherText = ""
for i in CipherList:
    CipherText += i
print("CipherText:", CipherText)
