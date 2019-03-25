
alphabet = 'ACGT'

def encrypt(shift, plaintext):
    cipherText = ''

    for letter in plaintext:
        try:
            index = (alphabet.index(letter) + shift) % 4
            cipherText += alphabet[index]
        except ValueError:
            cipherText +=letter;

    return cipherText


def decrypt(shift, ciphertext):
    plainText = ''

    for letter in ciphertext:
        try:
            index = (alphabet.index(letter) -shift) % 4
            plainText += alphabet[index]
        except ValueError:
            plaintext +=letter;
    return plainText


def affine(plaintext):
    cipherText = ''

    for letter in plaintext:
        try:
            index = (3*alphabet.index(letter) + 2) % 4
            cipherText += alphabet[index]
        except ValueError:
            cipherText +=letter;

    return cipherText


    
#Answer when shifted by 1 = 'TCCAAGTGTTGGTGCCAACCGGGAGCGACCCTTTCAGAGACTCCGA'
print('Part a:')
print ('The encryption for this sequence of nucleotides: %s' % encrypt(1, 'GAATTCGCGGCCGCAATTAACCCTCACTAAAGGGATCTCTAGAACT'))
print ('The decrypted (plainText) sequence is: %s' % decrypt(1,'TCCAAGTGTTGGTGCCAACCGGGAGCGACCCTTTCAGAGACTCCGA'))

print('')
print('Part b:')
print('An affine cipher ((3x+2)modulo 4) for the neucleotide alphabet: %s' % affine('ACGT'))
print('An affine cipher ((3x+2)modulo 4) for the neucleotide sequence: %s' % affine('GAATTCGCGGCCGCAATTAACCCTCACTAAAGGGATCTCTAGAACT'))
print('The restrictions relate to the size in the neuclotide alphabet (m=4).  "a" is restricted to the coprime of "m". 3 and 4 are coprimes so this is valid')

