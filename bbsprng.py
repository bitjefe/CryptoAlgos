

plainText = '010100110100010101000011010101010101001001000101';
cipherText = '';

p = 24672462467892469787
q = 396736894567834589803
n = p*q
#print("n = %d" % (n))
lsbList = []
tBit = 0;

x = 873245647888478349013
x0 =  x**2
x0 = x0 % n

#print("x0 = ", x0)

for i in range(0,48):
    x1 = (x0**2) % n
    tBit = x1
    if i <= 48:
        x0 = tBit
        lsb = x0%2
        lsbList.append(lsb)
        #print("x(",i,")=", x1)
        
#print("Least significant bits ", lsbList)
#print(len(lsbList))

index = plainText[0]
for i in range(0,48):
    if i<48:
        cipherText += str(lsbList[i])

#change cipherText to hex to check final answer in online tool
cipherTextHex = hex(int(cipherText,2))
plainTextHex = hex(int(plainText,2))

#change text to int for XOR
cipherTextInt = int(cipherTextHex,16)
plainTextInt = int(plainTextHex,16)

#XOR and add "00" to beginning of binary to return to 48 digits
newCipherText = (plainTextInt ^ cipherTextInt)
newCipherTextBinary = "00"+ "{0:b}".format(newCipherText)

#print our binary representation in groups of 4
print( " ".join([newCipherTextBinary[i:i+4] for i in range(0, len(newCipherTextBinary), 4)]))

#answer
# 0010 0011 0100 1000 1011 1011 1011 0101 0010 1101 1100 0101
