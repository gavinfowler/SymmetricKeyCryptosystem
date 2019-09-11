import random
import string
import sys
import math
import numpy as np

############# CONSTANTS ##############
POLYBIUS = [
    ['E', 'Y', 'O', 'P', 'D', '9'],
    ['2', 'H', 'Q', 'X', '1', 'I'],
    ['R', '3', 'A', 'J', '8', 'S'],
    ['F', '0', 'N', '4', 'G', '5'],
    ['Z', 'B', 'U', 'V', 'C', 'T'],
    ['M', '7', 'K', 'W', '6', 'L'],
]

####### ENCRYPTION #########
def encrypt(msg, key):
    """
    Function to encrypt a plaintext message using a key
    """
    newKey = compositeKeyGen(key)
    print(f'newKey: {newKey}')
    cipher = columnarTransposition(msg, newKey['keyForColumn'])
    print(f'cipher: {cipher}')
    result = findFromPolybius(cipher)
    print(f'result: {result}')
    cipher = xor(result, newKey['pad'])
    print(f'cipher: {cipher}')
    return cipher

def columnarTransposition(msg, key):
    """
    Function to encrypt a message using columnar transposition using a specific key
    """
    msg = msg.replace(" ", "")
    arr = []

    for letter in key:
        arr.append([letter])
    count = 0

    while len(msg) > 0:
        letter = msg[0]
        msg = msg[1:]
        print(arr)
        print(count)
        arr[count].append(letter)

        count += 1
        if count >= len(key):
            count = 0
        
    arr.sort()
    cipher = ''

    for i in range(0,len(arr)):
        for j in range(1,len(arr[i])):
            cipher += arr[i][j]
    
    cipher = cipher.lower()
    return cipher

def xor(binaryMsg, binaryKey):
    """
    function to do an XOR on binary
    """
    print(binaryMsg)
    print(binaryKey)
    return binaryMsg


############ DECRYPTION #################
def decrypt(msg, key):
    """
    Function to decrypt a plaintext message using a key
    """
    print('\nBegin decrypt')
    print(msg)
    print(key)
    print('End decrypt')
    return msg

####### GENERAL FUNCTIONS ##########
def compositeKeyGen(key):
    """
    Function generate key for columnar transposition
    """
    pad = '{0:06b}'.format(int(key[-2:]))
    key = key[:-2]
    # print(f'Pad: {pad}')
    # print(f'Key: {key}')
    keyForColumn = ''
    for i in range(0, len(key), 2):
        keyForColumn += POLYBIUS[int(key[i+1])][int(key[i])]
    # print(f'Key for columnar transposition: {keyForColumn}')
    return {'keyForColumn':keyForColumn, 'pad':pad}


def findFromPolybius(word):
    """
    Function to find the coordinates of each letter in a word from the polybius square
    """
    # arrA = np.array(POLYBIUS)
    # x = "T"
    # result = np.where((arrA == x))
    # print(result[0][0], result[1][0])

    total = ''
    indexes = []
    word = word.upper()
    for letter in word:
        index = [(iy,ix) for ix, row in enumerate(POLYBIUS) for iy, i in enumerate(row) if i == letter][0]
        number = str(index[0]) + str(index[1])
        total += '{0:06b}'.format(int(number))
        total += ' '
        # print('{0:06b}'.format(int(number)))
        # print(f'{index[0]} and {index[1]}')
        indexes.append(index)
    # print(f'findFromPolybius: {total}')
    # print(indexes)
    return total

####### MAIN FUNCTIONS #########

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
    key, plaintext, cipher = '', '', ''

    if choice == '1':
        key = input('Enter a composite key: ')
        plaintext = input('Enter a plaintext message: ')
        print(len(key))
        if len(key) <= 3 or len(plaintext) <= 0:
            raise Exception("The key was not long enough to generate a key and a pad or the message was empty")
        print('Encyrpt a message')
        print(f'Original: {plaintext}\nEncrypted message: {encrypt(plaintext, key)}')
    elif choice == '2':
        key = input('Enter a composite key: ')
        cipher = input('Enter a cipher: ')
        print(' Decrypt a message')
    elif choice == '3':
        key = input('Enter a composite key: ')
        plaintext = input('Enter a plaintext message: ')
        print('Encrypt then decrypt a message')
        result = encrypt(plaintext,key)
        result = decrypt(result, key)
        print(f'Result: {result}')

if __name__ == '__main__':
  main()