

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(shift, plaintext):
    cipherText = ''

    for letter in plaintext.lower():
            index = (alphabet.index(letter) + shift) % 26
            cipherText += alphabet[index]

    return cipherText.lower()

def decrypt(shift, ciphertext):
    plainText = ''

    for letter in ciphertext: 
            index = (alphabet.index(letter) -shift) % 26
            plainText += alphabet[index]

    return plainText


for shift in range(0,25,1):
    print ('Shift#',shift,': %s' %decrypt(shift,'ycvejqwvhqtdtwvwu'))
    

#Answer is revealed when shifted by 2 = 'watchoutforbrutus'
print ('')
print ('The decrypted message is: %s' % decrypt(2,'ycvejqwvhqtdtwvwu'))
print ('The ciphertext for this decrypted message: %s' % encrypt(2, 'watchoutforbrutus'))
