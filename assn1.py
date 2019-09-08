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
    cipher = "" 
  
    # track key indices 
    k_indx = 0
  
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))
  
    # calculate column of the matrix 
    col = len(key) 
      
    # calculate maximum row of the matrix 
    row = int(math.ceil(msg_len / col)) 
  
    # add the padding character '_' in empty 
    # the empty cell of the matix  
    fill_null = int((row * col) - msg_len) 
    msg_lst.extend('_' * fill_null) 
  
    # create Matrix and insert message and  
    # padding characters row-wise  
    matrix = [msg_lst[i: i + col]  
              for i in range(0, len(msg_lst), col)] 
  
    # read matrix column-wise using key 
    for _ in range(col): 
        curr_idx = key.index(key_lst[k_indx]) 
        cipher += ''.join([row[curr_idx]  
                          for row in matrix]) 
        k_indx += 1
  
    return cipher 

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
            print(int(choice))
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

    key = input('Enter a composite key: ')
    # plaintext = input('Enter a plaintext message: ')
    encrypt(key)
    # encryptCT("BALL", "THIS CODE")
    # print(encryptMessage("THIS IS A TEST MESSAGE"))
    # print(encryptMessage("THIS"))

if __name__ == '__main__':
  main()