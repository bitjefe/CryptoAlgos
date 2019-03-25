
#Instructions to run:  Compile and Run this program. Then call: driver(). This will prompt for plainText and key then print the ciphertext.

import collections

def driver():
    #plainText = int(input("Enter Plaintext int: "))
    #key = int(input("Enter key int: "))
    plainText = 0
    cipherText = 3242
    CipherTextList = []
    ShiftedCipherList = []


    for k in range(512):
        key = k
        CipherText = encrypt(plainText,key)
        CipherTextList.append(CipherText)   
    
    for x in range(12):
        CipherTextBits = collections.deque([1,1,0,0,1,0,1,0,1,0,1,0])
        shiftedCipherText = ""
        
        CipherTextBits.rotate(x)
        
        for bits in list(CipherTextBits):
            shiftedCipherText += str(bits)
            
        shiftedCipherTextInteger = int(shiftedCipherText,2)

        ShiftedCipherList.append(shiftedCipherTextInteger)

        if(str(shiftedCipherTextInteger) in CipherTextList):
            print("Shift = " + str(x))
            print("Des key = " + format(CipherTextList.index(str(shiftedCipherTextInteger)),'09b'))


    #print(CipherTextList)
    #print(" ")
    #print(ShiftedCipherList)
            

def encrypt(plainText, key):

    plainTextBin = format(plainText,'012b')
    KeyBin = format(key,'09b')
    #print("PlainText = " + str(plainText) +" ("+ str(plainTextBin)+"); key = " + str(key)+" ("+str(KeyBin)+")")

    plainTextLeftBits = plainTextBin[:6]
    plainTextRightBits = plainTextBin[6:]

    def keyGen(iteration):
        if iteration == 1:
            return KeyBin[0:8]
        if iteration == 2:
            return KeyBin[1:9]
        if iteration == 3:
            return str(KeyBin[2:9])+str(KeyBin[0])
        if iteration == 4:
            return str(KeyBin[3:9])+str(KeyBin[0:2])
                

    def expander(plainTextRightBits):
        expanderStr = plainTextRightBits[0]+plainTextRightBits[1]+plainTextRightBits[3]+plainTextRightBits[2]+plainTextRightBits[3]+plainTextRightBits[2]+plainTextRightBits[4]+plainTextRightBits[5]
        return (expanderStr)

    #print("L0"+" = " + str(int(plainTextLeftBits,2)) +" ("+ str(plainTextLeftBits)+"); R0"+" = " + str(int(plainTextRightBits,2))+" ("+str(plainTextRightBits)+")")

    def des(bitsLeft, bitsRight, iteration):

        for x in range(1):
          
            expanderStr = expander(bitsRight)
            KeyBinLeft = keyGen(iteration)

            skList = []
            expanderList = []
            KeyBinLeftList = []

            for char in expanderStr:
                expandedInt = int(char)
                expanderList.append(expandedInt)

            for char in KeyBinLeft:
                KeyBinLeftInt = int(char)
                KeyBinLeftList.append(KeyBinLeftInt)
                                            
            for index in range(len(expanderList)):
                subKeyBit = expanderList[index] ^ KeyBinLeftList[index]
                skList.append(subKeyBit)

            skString = ''.join(str(bit) for bit in skList)

            sBox1In = str(skString[:4])
            sBox1LMB = sBox1In[0]
            sBox1EndBits = sBox1In[1:4]
            sBox1Lead = int(sBox1LMB)

            sBox2In = str(skString[4:])
            sBox2LMB = sBox2In[0]
            sBox2EndBits = sBox2In[1:4]
            sBox2Lead = int(sBox2LMB)


            sBox1Array = [["101","001"],["010","100"],["001","110"],["110","010"],["011","000"],["100","111"],["111","101"],["000","011"]]
            sBox2Array = [["100","101"],["000","011"],["110","000"],["101","111"],["111","110"],["001","010"],["011","001"],["010","100"]]
            
            sBox1_0Row = []
            sBox1_1Row = []
            endBits = ["000","001","010","011","100","101","110","111"]

            r1 = ""

            if sBox1Lead == 0:
                for index in range(len(sBox1Array)):
                    sBox1_0Row.append(sBox1Array[index][sBox1Lead])
                for bit in range(len(endBits)):
                    if sBox1EndBits == endBits[bit]:
                        tableIndex = bit
                        r1 = r1+sBox1_0Row[tableIndex]
                        

            if sBox1Lead == 1:
                for index in range(len(sBox1Array)):
                    sBox1_1Row.append(sBox1Array[index][1])
                for bit in range(len(endBits)):
                    if sBox1EndBits == endBits[bit]:
                        tableIndex = bit
                        r1 = r1+(sBox1_1Row[tableIndex])

            sBox2_0Row = []
            sBox2_1Row = []


            if sBox2Lead == 0:
                for index in range(len(sBox2Array)):
                    sBox2_0Row.append(sBox2Array[index][sBox2Lead])
                for bit in range(len(endBits)):
                    if sBox2EndBits == endBits[bit]:
                        tableIndex = bit
                        r1 = r1+sBox2_0Row[tableIndex]

            if sBox2Lead == 1:
                for index in range(len(sBox2Array)):
                    sBox2_1Row.append(sBox2Array[index][sBox2Lead])
                for bit in range(len(endBits)):
                    if sBox2EndBits == endBits[bit]:
                        tableIndex = bit
                        r1 = r1+sBox2_1Row[tableIndex]
                  
            newR1 = []

            for index in range(len(r1)):
                newR1key = int(bitsLeft[index]) ^ int(r1[index])
                newR1.append(newR1key)

            newR1String = ''.join(str(bit) for bit in newR1)

            lrNew = []
            lrNew.append(bitsRight)
            lrNew.append(newR1String)
            
            return lrNew



    nextSubKeyPairs = des(plainTextLeftBits, plainTextRightBits,1)

    #print("L1 = " + str(int(nextSubKeyPairs[0],2)) +" ("+ str(nextSubKeyPairs[0])+"); R1 = " + str(int(nextSubKeyPairs[1],2))+" ("+nextSubKeyPairs[1]+")")
    nextSubKeyPairs1 = des(nextSubKeyPairs[0], nextSubKeyPairs[1],2)


    #print("L2 = " + str(int(nextSubKeyPairs1[0],2)) +" ("+ str(nextSubKeyPairs1[0])+"); R2 = " + str(int(nextSubKeyPairs1[1],2))+" ("+nextSubKeyPairs1[1]+")")
    nextSubKeyPairs2 = des(nextSubKeyPairs1[0], nextSubKeyPairs1[1],3)


    #print("L3 = " + str(int(nextSubKeyPairs2[0],2)) +" ("+ str(nextSubKeyPairs2[0])+"); R3 = " + str(int(nextSubKeyPairs2[1],2))+" ("+nextSubKeyPairs2[1]+")")
    nextSubKeyPairs3 = des(nextSubKeyPairs2[0], nextSubKeyPairs2[1],4)

    #print("L4 = " + str(int(nextSubKeyPairs3[0],2)) +" ("+ str(nextSubKeyPairs3[0])+"); R4 = " + str(int(nextSubKeyPairs3[1],2))+" ("+nextSubKeyPairs3[1]+")")

    #print("CipherText = " + str(int(nextSubKeyPairs3[0]+nextSubKeyPairs3[1],2)) +" ("+ str(nextSubKeyPairs3[0]+nextSubKeyPairs3[1])+")")

    CipherText = (str(int(nextSubKeyPairs3[0]+nextSubKeyPairs3[1],2)))

    return CipherText




