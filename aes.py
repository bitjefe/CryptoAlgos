
def subBytes1(startNextRoundResult):
    sb0 = ['63','7c','77','7b','f2','6b','6f','c5','30','01','67','2b','fe','d7','ab','76']
    sb1 = ['ca','82','c9','7d','fa','59','47','f0','ad','d4','a2','af','9c','a4','72','c0']
    sb2 = ['b7','fd','93','26','36','3f','f7','cc','34','a5','e5','f1','71','d8','31','15']
    sb3 = ['04','c7','23','c3','18','96','05','9a','07','12','80','e2','eb','27','b2','75']
    sb4 = ['09','83','2c','1a','1b','6e','5a','a0','52','3b','d6','b3','29','e3','2f','84']
    sb5 = ['53','d1','00','ed','20','fc','b1','5b','6a','cb','be','39','4a','4c','58','cf']
    sb6 = ['d0','ef','aa','fb','43','4d','33','85','45','f9','02','7f','50','3c','9f','a8']
    sb7 = ['51','a3','40','8f','92','9d','38','f5','bc','b6','da','21','10','ff','f3','d2']
    sb8 = ['cd','0c','13','ec','5f','97','44','17','c4','a7','7e','3d','64','5d','19','73']
    sb9 = ['60','81','4f','dc','22','2a','90','88','46','ee','b8','14','de','5e','0b','db']
    sbA = ['e0','32','3a','0a','49','06','24','5c','c2','d3','ac','62','91','95','e4','79']
    sbB = ['e7','c8','37','6d','8d','d5','4e','a9','6c','56','f4','ea','65','7a','ae','08']
    sbC = ['ba','78','25','2e','1c','a6','b4','c6','e8','dd','74','1f','4b','bd','8b','8a']
    sbD = ['70','3e','b5','66','48','03','f6','0e','61','35','57','b9','86','c1','1d','9e']
    sbE = ['e1','f8','98','11','69','d9','8e','94','9b','1e','87','e9','ce','55','28','df']
    sbF = ['8c','a1','89','0d','bf','e6','42','68','41','99','2d','0f','b0','54','bb','16']
    
    r1 = startNextRoundResult[0:8]
    r2 = startNextRoundResult[8:16]
    r3 = startNextRoundResult[16:24]
    r4 = startNextRoundResult[24:32]

    b1 = r1[0:2]
    b2 = r1[2:4]
    b3 = r1[4:6]
    b4 = r1[6:8]
    b5 = r2[0:2]
    b6 = r2[2:4]
    b7 = r2[4:6]
    b8 = r2[6:8]
    b9 = r3[0:2]
    b10 = r3[2:4]
    b11 = r3[4:6]
    b12 = r3[6:8]
    b13 = r4[0:2]
    b14 = r4[2:4]
    b15 = r4[4:6]
    b16 = r4[6:8]

    subBytesResult=''
    lst_bytes = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16]
    lst_subBytes = [sb0,sb1,sb2,sb3,sb4,sb5,sb6,sb7,sb8,sb9,sbA,sbB,sbC,sbD,sbE,sbF]

    for byte in lst_bytes:
        firstBit = int(byte[0],16)
        rowSubBytes = lst_subBytes[firstBit]
        secondBit = int(byte[1],16)
        columnSubBytes = rowSubBytes[secondBit]
        subBytesResult = subBytesResult + columnSubBytes
               
    return subBytesResult
 
def shiftRows(subBytesResult):
    r1 = subBytesResult[0:8]
    r2 = subBytesResult[8:16]
    r3 = subBytesResult[16:24]
    r4 = subBytesResult[24:32]

    newr2 = r2[2:8]+r2[0:2]
    newr3 = r3[4:8]+r3[0:4]
    newr4 = r4[6:8]+r4[0:6]

    shiftRowsResult = r1+newr2+newr3+newr4
    return shiftRowsResult

def mixColumns(shiftRowsResult):
    c1 = shiftRowsResult[0:2]+shiftRowsResult[8:10]+shiftRowsResult[16:18]+shiftRowsResult[24:26]
    c2 = shiftRowsResult[2:4]+shiftRowsResult[10:12]+shiftRowsResult[18:20]+shiftRowsResult[26:28]
    c3 = shiftRowsResult[4:6]+shiftRowsResult[12:14]+shiftRowsResult[20:22]+shiftRowsResult[28:30]
    c4 = shiftRowsResult[6:8]+shiftRowsResult[14:16]+shiftRowsResult[22:24]+shiftRowsResult[30:32]
    lst_c = [c1,c2,c3,c4]

    mixColumnsResult=''
    newByte1=''
    newByte2=''
    newByte3=''
    newByte4=''
    r1=''
    r2=''
    r3=''
    r4=''
    
    for col in lst_c:
        byte1 = int(col[0:2],16)
        byte2 = int(col[2:4],16)
        byte3 = int(col[4:6],16)
        byte4 = int(col[6:8],16)
        
        def multiplyBy2(byte):
            newByte2 = (byte<<1)
            if (newByte2 & 0x100) != 0:
                newByte2 ^= 0x11b
            return newByte2

        def multiplyBy3(byte):
            return multiplyBy2(byte)^byte

        newByte1 = (multiplyBy2(byte1)) ^ (multiplyBy3(byte2)) ^ (byte3) ^ (byte4)
        newByte1 = (hex(newByte1))[2:]

        if(newByte1 == '1'):
            newByte1 = '01'
        elif(newByte1 == '2'):
            newByte1 = '02'
        elif(newByte1 == '3'):
            newByte1 = '03'
        elif(newByte1 == '4'):
            newByte1 = '04'
        elif(newByte1 == '5'):
            newByte1 = '05'
        elif(newByte1 == '6'):
            newByte1 = '06'
        elif(newByte1 == '7'):
            newByte1 = '07'
        elif(newByte1 == '8'):
            newByte1 = '08'
        elif(newByte1 == '9'):
            newByte1 = '09'
        elif(newByte1 == 'a'):
            newByte1 = '0a'
        elif(newByte1 == 'b'):
            newByte1 = '0b'
        elif(newByte1 == 'c'):
            newByte1 = '0c'
        elif(newByte1 == 'd'):
            newByte1 = '0d'
        elif(newByte1 == 'e'):
            newByte1 = '0e'
        elif(newByte1 == 'f'):
            newByte1 = '0f'

        newByte2 = (byte1) ^ (multiplyBy2(byte2)) ^ (multiplyBy3(byte3)) ^ (byte4)
        newByte2 = (hex(newByte2))[2:]

        if(newByte2 == '1'):
            newByte2 = '01'
        elif(newByte2 == '2'):
            newByte2 = '02'
        elif(newByte2 == '3'):
            newByte2 = '03'
        elif(newByte2 == '4'):
            newByte2 = '04'
        elif(newByte2 == '5'):
            newByte2 = '05'
        elif(newByte2 == '6'):
            newByte2 = '06'
        elif(newByte2 == '7'):
            newByte2 = '07'
        elif(newByte2 == '8'):
            newByte2 = '08'
        elif(newByte2 == '9'):
            newByte2 = '09'
        elif(newByte2 == 'a'):
            newByte2 = '0a'
        elif(newByte2 == 'b'):
            newByte2 = '0b'
        elif(newByte2 == 'c'):
            newByte2 = '0c'
        elif(newByte2 == 'd'):
            newByte2 = '0d'
        elif(newByte2 == 'e'):
            newByte2 = '0e'
        elif(newByte2 == 'f'):
            newByte2 = '0f'

        newByte3 = (byte1) ^ (byte2) ^ (multiplyBy2(byte3)) ^ (multiplyBy3(byte4))
        newByte3 = (hex(newByte3))[2:]

        if(newByte3 == '1'):
            newByte3 = '01'
        elif(newByte3 == '2'):
            newByte3 = '02'
        elif(newByte3 == '3'):
            newByte3 = '03'
        elif(newByte3 == '4'):
            newByte3 = '04'
        elif(newByte3 == '5'):
            newByte3 = '05'
        elif(newByte3 == '6'):
            newByte3 = '06'
        elif(newByte3 == '7'):
            newByte3 = '07'
        elif(newByte3 == '8'):
            newByte3 = '08'
        elif(newByte3 == '9'):
            newByte3 = '09'
        elif(newByte3 == 'a'):
            newByte3 = '0a'
        elif(newByte3 == 'b'):
            newByte3 = '0b'
        elif(newByte3 == 'c'):
            newByte3 = '0c'
        elif(newByte3 == 'd'):
            newByte3 = '0d'
        elif(newByte3 == 'e'):
            newByte3 = '0e'
        elif(newByte3 == 'f'):
            newByte3 = '0f'

        newByte4 = (multiplyBy3(byte1)) ^ (byte2) ^ (byte3) ^ (multiplyBy2(byte4))
        newByte4 = (hex(newByte4))[2:]
        
        if(newByte4 == '1'):
            newByte4 = '01'
        elif(newByte4 == '2'):
            newByte4 = '02'
        elif(newByte4 == '3'):
            newByte4 = '03'
        elif(newByte4 == '4'):
            newByte4 = '04'
        elif(newByte4 == '5'):
            newByte4 = '05'
        elif(newByte4 == '6'):
            newByte4 = '06'
        elif(newByte4 == '7'):
            newByte4 = '07'
        elif(newByte4 == '8'):
            newByte4 = '08'
        elif(newByte4 == '9'):
            newByte4 = '09'
        elif(newByte4 == 'a'):
            newByte4 = '0a'
        elif(newByte4 == 'b'):
            newByte4 = '0b'
        elif(newByte4 == 'c'):
            newByte4 = '0c'
        elif(newByte4 == 'd'):
            newByte4 = '0d'
        elif(newByte4 == 'e'):
            newByte4 = '0e'
        elif(newByte4 == 'f'):
            newByte4 = '0f'

        r1 += newByte1
        r2 += newByte2
        r3 += newByte3
        r4 += newByte4

        mixColumnsResult = r1+r2+r3+r4

    return str(mixColumnsResult)

def startNextRound(mixColumnsResult,key):
        key = int(key,16)
        mixColumnsResult = int(mixColumnsResult,16)
        startNextRoundResult = bin(mixColumnsResult ^ key)
        startNextRoundResult = str(hex(int(startNextRoundResult,2)))
        return startNextRoundResult

# Start
plaintext = '328831e0435a3137f6309807a88da234'
print("=== Plaintext ===")
print(plaintext[0:2]," ",plaintext[2:4]," ",plaintext[4:6]," ",plaintext[6:8])
print(plaintext[8:10]," ",plaintext[10:12]," ",plaintext[12:14]," ",plaintext[14:16])
print(plaintext[16:18]," ",plaintext[18:20]," ",plaintext[20:22]," ",plaintext[22:24])
print(plaintext[24:26]," ",plaintext[26:28]," ",plaintext[28:30]," ",plaintext[30:32],"\n\n")

lst_keys = ['2b28ab097eaef7cf15d2154f16a6883c','a088232afa54a36cfe2c397617b13905','f27a5973c296355995b980f6f2437a7f','3d471e6d8016237a47fe7e887d3e443b','efa8b6db4452710ba55b25ad417f3b00','d47cca11d183f2f9c69db815f887bcbc','6d11dbca880bf900a33e86937afd41fd','4e5f844e545fa6a6f7c94fdc0ef3b24f','eab5317fd28d2b8d73baf52921d2602f','ac19285777fad15c66dc2900f321416e','d0c9e1b614ee3f63f9250c0ca889c8a6']

mixColumnsResult=''

for key in lst_keys:
    if lst_keys.index(key)==10:
        continue

    print("=== Round ",lst_keys.index(key)+1," ===")

    print("--- Start of round ---")
    if lst_keys.index(key)==0 and key == '2b28ab097eaef7cf15d2154f16a6883c':
        plaintext = int(plaintext,16)
        key = int(key,16)
        exor = bin(plaintext^key)
        startOfRound = str(hex(int(exor[:128],2)))
        startOfRound = startOfRound[2:]
        print(startOfRound[0:2]," ",startOfRound[2:4]," ",startOfRound[4:6]," ",startOfRound[6:8])
        print(startOfRound[8:10]," ",startOfRound[10:12]," ",startOfRound[12:14]," ",startOfRound[14:16])
        print(startOfRound[16:18]," ",startOfRound[18:20]," ",startOfRound[20:22]," ",startOfRound[22:24])
        print(startOfRound[24:26]," ",startOfRound[26:28]," ",startOfRound[28:30]," ",startOfRound[30:32],"\n")
        subBytesResult = subBytes1(startOfRound)
    else:
        mixColumnsResult = int(mixColumnsResult,16)
        key = int(key,16)
        startNextRoundResult = mixColumnsResult ^ key
        startNextRoundResult = hex(startNextRoundResult)[2:]
        print(startNextRoundResult[0:2]," ",startNextRoundResult[2:4]," ",startNextRoundResult[4:6]," ",startNextRoundResult[6:8])
        print(startNextRoundResult[8:10]," ",startNextRoundResult[10:12]," ",startNextRoundResult[12:14]," ",startNextRoundResult[14:16])
        print(startNextRoundResult[16:18]," ",startNextRoundResult[18:20]," ",startNextRoundResult[20:22]," ",startNextRoundResult[22:24])
        print(startNextRoundResult[24:26]," ",startNextRoundResult[26:28]," ",startNextRoundResult[28:30]," ",startNextRoundResult[30:32],"\n")
        subBytesResult = subBytes1(startNextRoundResult)

    print("--- After subBytes ---")
    print(subBytesResult[0:2]," ",subBytesResult[2:4]," ",subBytesResult[4:6]," ",subBytesResult[6:8])
    print(subBytesResult[8:10]," ",subBytesResult[10:12]," ",subBytesResult[12:14]," ",subBytesResult[14:16])
    print(subBytesResult[16:18]," ",subBytesResult[18:20]," ",subBytesResult[20:22]," ",subBytesResult[22:24])
    print(subBytesResult[24:26]," ",subBytesResult[26:28]," ",subBytesResult[28:30]," ",subBytesResult[30:32],"\n")
    shiftRowsResult = shiftRows(subBytesResult)
    print("--- After shiftRows ---")
    print(shiftRowsResult[0:2]," ",shiftRowsResult[2:4]," ",shiftRowsResult[4:6]," ",shiftRowsResult[6:8])
    print(shiftRowsResult[8:10]," ",shiftRowsResult[10:12]," ",shiftRowsResult[12:14]," ",shiftRowsResult[14:16])
    print(shiftRowsResult[16:18]," ",shiftRowsResult[18:20]," ",shiftRowsResult[20:22]," ",shiftRowsResult[22:24])
    print(shiftRowsResult[24:26]," ",shiftRowsResult[26:28]," ",shiftRowsResult[28:30]," ",shiftRowsResult[30:32],"\n")
    mixColumnsResult = mixColumns(shiftRowsResult)
    print("--- After mixColumns ---")
    print(mixColumnsResult[0:2]," ",mixColumnsResult[2:4]," ",mixColumnsResult[4:6]," ",mixColumnsResult[6:8])
    print(mixColumnsResult[8:10]," ",mixColumnsResult[10:12]," ",mixColumnsResult[12:14]," ",mixColumnsResult[14:16])
    print(mixColumnsResult[16:18]," ",mixColumnsResult[18:20]," ",mixColumnsResult[20:22]," ",mixColumnsResult[22:24])
    print(mixColumnsResult[24:26]," ",mixColumnsResult[26:28]," ",mixColumnsResult[28:30]," ",mixColumnsResult[30:32],"\n\n")

shiftRowsResult = int(shiftRowsResult,16)
key = int(key,16)
ciphertext = shiftRowsResult ^ key
ciphertext = hex(ciphertext)[2:]
print("=== Ciphertext ===")  
print(ciphertext[0:2]," ",ciphertext[2:4]," ",ciphertext[4:6]," ",ciphertext[6:8])
print(ciphertext[8:10]," ",ciphertext[10:12]," ",ciphertext[12:14]," ",ciphertext[14:16])
print(ciphertext[16:18]," ",ciphertext[18:20]," ",ciphertext[20:22]," ",ciphertext[22:24])
print(ciphertext[24:26]," ",ciphertext[26:28]," ",ciphertext[28:30]," ",ciphertext[30:32],"\n")
