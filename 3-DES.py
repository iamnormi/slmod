import modulefortfsse.DES_exp3 as des

pt=input("Enter Plain Text ...: ")
pt=des.pad(pt)
print("Plain Text After Padding... : ",pt)
#pt = "123456ABCD132536"
key=input("Enter Key ...: ")
key=des.pad(key)
print("Key after Padding... : ",key)
#key = "AABB09182736CCDD"
key = des.hex2bin(key)
kp= des.keyp
key = des.permute(key, kp ,56)
shift_table = des.shift_table
key_comp = des.key_comp

# Splitting
left = key[0:28] # rkb for RoundKeys in binary
right = key[28:56] # rk for RoundKeys in hexadecimal

rkb = []
rk = []
for i in range(0, 16):
        # Shifting the bits by nth shifts by checking from shift table
        left = des.shift_left(left, shift_table[i])
        right = des.shift_left(right, shift_table[i])

        # Combination of left and right string
        combine_str = left + right

        # Compression of key from 56 to 48 bits
        round_key = des.permute(combine_str, key_comp, 48)

        rkb.append(round_key)
        rk.append(des.bin2hex(round_key))



print("Encryption")
cipher_text = des.bin2hex(des.encrypt(pt, rkb, rk))
print("Cipher Text : ", cipher_text)

print("Decryption")
rkb_rev = rkb[::-1]
rk_rev = rk[::-1]
text = des.bin2hex(des.encrypt(cipher_text, rkb_rev, rk_rev))
print("Plain Text : ", text)

