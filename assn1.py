import random
import string
import sys
import math

############# CONSTANTS ##############
POLYBIUS = [
    ['E', 'Y', 'O', 'P', 'D', '9'],
    ['2', 'H', 'Q', 'X', '1', 'I'],
    ['R', '3', 'A', 'J', '8', 'S'],
    ['F', '0', 'N', '4', 'G', '5'],
    ['Z', 'B', 'U', 'V', 'C', 'T'],
    ['M', '7', 'K', 'W', '6', 'L'],
]

def encrypt(key):
    """
    Function to encrypt a plaintext message using a key
    """
    compositeKeyGen(key)
    print('encrypt')

def decrypt():
    """
    Function to decrypt a plaintext message using a key
    """
    print('decrypt')

def compositeKeyGen(key):
    """
    Function generate key for columnar transposition
    """
    pad = key[-2:]
    key = key[:-2]
    print(f'Pad: {pad}')
    print(f'Key: {key}')
    keyForColumn = ''
    for i in range(0, len(key), 2):
        keyForColumn += POLYBIUS[int(key[i+1])][int(key[i])]
    print(f'Key for columnar transposition: {keyForColumn}')
    print(f'pad to binary: {"{0:06b}".format(int(pad))}')
    # for i in keyForColumn:
    #     findFromPolybius(i)
    binaryKey = findFromPolybius(keyForColumn)
    print(f'Key to Binary: {binaryKey}')

def columnarTransposition(msg, key):
    """
    Function to encrypt a message using columnar transposition using a specific key
    """
    print('columnarTransposition')

def findFromPolybius(word):
    """
    Function to find the coordinates of each letter in a word from the polybius square
    """
    total = ''
    indexes = []
    for letter in word:
        index = [(iy,ix) for ix, row in enumerate(POLYBIUS) for iy, i in enumerate(row) if i == letter][0]
        number = str(index[0]) + str(index[1])
        total += '{0:06b}'.format(int(number))
        total += ' '
        print('{0:06b}'.format(int(number)))
        print(f'{index[0]} and {index[1]}')
        indexes.append(index)
    # print(f'findFromPolybius: {total}')
    print(indexes)
    return total
  
key = "BALL"
  
# Encryption 
def encryptMessage(msg):
    """
    Test function for columnar transposition
    """
    keylen = len(key)
    msg = msg.replace(" ", "")
    arr = []

    for letter in key:
        arr.append([letter])
    count = 0
    
    while len(msg) > 0:
        letter = msg[0]
        msg = msg[1:]
        arr[count].append(letter)

        count += 1
        if count >= 4:
            count = 0
        
    arr.sort()
    cipher = ''

    for i in range(0,len(arr)):
        for j in range(1,len(arr[i])):
            cipher += arr[i][j]
  
    print(f'Cipher: {cipher.lower()}')
    newCipher = ' '.join(cipher[i:i+keylen] for i in range(0, len(cipher), keylen))
    print(f'newCipher: {newCipher.lower()}')
    return newCipher 

def options():
    """
    Print out and get choice
    """
    acceptableChoice = False
    while not acceptableChoice:
        choice = input('Choose an option:\n' +
            '1. Encyrpt a message\n' +
            '2. Decrypt a message\n' +
            '3. Encrypt then decrypt a message\n' +
            '> ')
        if int(choice) > 0 and int(choice) < 4:
            acceptableChoice = True
        else:
            print('\nPlease choose an acceptable option\n')
    return choice

def main():
    choice = options()
    if choice == '1':
        print('Encyrpt a message')
    elif choice == '2':
        print(' Decrypt a message')
    elif choice == '3':
        print('Encrypt then decrypt a message')

    # key = input('Enter a composite key: ')
    # plaintext = input('Enter a plaintext message: ')

    # encrypt(key)

    encryptMessage("This is a test")
    
    # encryptCT("BALL", "THIS CODE")
    # print(encryptMessage("THIS IS A TEST MESSAGE"))
    # print(encryptMessage("THIS"))

if __name__ == '__main__':
  main()