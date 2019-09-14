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
    msg = msg.replace(" ", "").lower()
    arr = []

    for letter in key:
        arr.append([letter])
    count = 0

    while len(msg) > 0:
        letter = msg[0]
        msg = msg[1:]
        arr[count].append(letter)

        count += 1
        if count >= len(key):
            count = 0

    arr.sort()
    cipher = ''

    for i in range(0, len(arr)):
        for j in range(1, len(arr[i])):
            cipher += arr[i][j]

    cipher = cipher.lower()
    return cipher


def xor(binaryArr, binaryKey):
    """
    function to do an XOR on binary
    """
    result = ''
    for i in binaryArr:
        xor = int(i, 2) ^ int(binaryKey, 2)
        result += str(xor)
    return result


def testEncryption():
    """
    Function to test encryption
    """
    # Test compositeKeyGen
    compositeKeyGenResult = compositeKeyGen("1422555515")
    assert compositeKeyGenResult['keyForColumn'] == 'BALL'
    assert compositeKeyGenResult['pad'] == '001111'
    print('compositeKeyGen passed')

    # Test columnarTransposition
    columnarTranspositionResult = columnarTransposition(
        "This is a TeSt", 'BALL')
    assert columnarTranspositionResult == 'hsstieiatst'
    print('columnarTransposition passed')

    # Test findFromPolybius
    findFromPolybiusResult = findFromPolybius('ERFZM')
    assert findFromPolybiusResult == [
        '000000', '000010', '000011', '000100', '000101']
    print('findFromPolybius passed')

    # Test xor
    xorResult = xor(['000000', '000010', '000011',
                     '000100', '000101'], '001111')
    assert xorResult == "1513121110"
    print('xor passed')


############ DECRYPTION #################
def cipherToBinary(cipher):
    """
    Function convert a cipher into binary
    """
    pairs = []
    binary = []
    while cipher:
        pairs.append(cipher[:2])
        cipher = cipher[2:]
    for element in pairs:
        binary.append('{0:06b}'.format(int(element)))
    return binary


def keywordToNum(key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    kywrd_num_list = list(range(len(key)))
    init = 0
    for i in range(len(alpha)):
        for j in range(len(key)):
            if alpha[i] == key[j]:
                init += 1
                kywrd_num_list[j] = init
    return kywrd_num_list


def decryptColumnarTransposition(msg, key):
    num_of_rows = math.ceil(len(msg)/len(key))

    arr = [''] * num_of_rows
    for i in range(num_of_rows):
        arr[i] = [''] * len(key)
        for j in range(len(key)):
            arr[i][j] = ''

    keyn = keywordToNum(key)
    keyn_count = 1
    msg_index = 0
    while keyn_count < len(keyn)+1:
        for i in range(len(keyn)):
            if (keyn[i] == keyn_count):
                for j in range(num_of_rows):
                    if arr[j][i] == '' and msg_index < len(msg):
                        arr[j][i] = msg[msg_index]
                        msg_index = msg_index + 1
                keyn_count = keyn_count + 1
    
    for i in range(num_of_rows):
        arr[i] = ''.join(arr[i])

    plaintext = ''.join(arr)
    return plaintext


def decrypt(msg, key):
    """
    Function to decrypt a plaintext message using a key
    """
    print(msg)
    print(key)
    compositeKeyGenResult = compositeKeyGen(key)
    print('\nBegin decrypt')
    binary = cipherToBinary(msg)
    print(binary)
    padkey = compositeKeyGenResult['pad']
    #insert one time pad here
    # padResult =
    #insert getting string of letters from Polybius here
    # polybiusResult = 
    colKey = compositeKeyGenResult['keyForColumn']
    decryptColumnarTransposition(polybiusResult, colKey)
    print('End decrypt')
    return msg

####### GENERAL FUNCTIONS ##########


def compositeKeyGen(key):
    """
    Function generate key for columnar transposition
    Test with entering a '0' on selection
    """
    pad = '{0:06b}'.format(int(key[-2:]))
    key = key[:-2]
    # print(f'Pad: {pad}')
    # print(f'Key: {key}')
    keyForColumn = ''
    for i in range(0, len(key), 2):
        keyForColumn += POLYBIUS[int(key[i + 1])][int(key[i])]
    # print(f'Key for columnar transposition: {keyForColumn}')
    return {'keyForColumn': keyForColumn, 'pad': pad}


def findFromPolybius(word):
    """
    Function to find the coordinates of each letter in a word from the polybius square
    Test with entering a '0' on selection
    """

    total = ''
    indexes = []
    arr = []
    word = word.upper()
    for letter in word:
        index = [(iy, ix) for ix, row in enumerate(POLYBIUS)
                 for iy, i in enumerate(row) if i == letter][0]
        number = str(index[0]) + str(index[1])
        total += '{0:06b}'.format(int(number))
        total += ' '
        arr.append('{0:06b}'.format(int(number)))
        # print('{0:06b}'.format(int(number)))
        # print(f'{index[0]} and {index[1]}')
        indexes.append(index)
    # print(f'findFromPolybius: {total}')
    # print(indexes)
    # return total
    return arr

####### MAIN FUNCTIONS #########


def options():
    """
    Print out and get choice
    """
    acceptableChoice = False
    while not acceptableChoice:
        choice = input('Choose an option:\n' +
                       '0. Test Functions\n' +
                       '1. Encyrpt a message\n' +
                       '2. Decrypt a message\n' +
                       '3. Encrypt then decrypt a message\n' +
                       '> ')
        if int(choice) > -1 and int(choice) < 4:
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
            raise Exception(
                "The key was not long enough to generate a key and a pad or the message was empty")
        print('Encyrpt a message')
        print(
            f'Original: {plaintext}\nEncrypted message: {encrypt(plaintext, key)}')
    elif choice == '2':
        key = input('Enter a composite key: ')
        cipher = input('Enter a cipher: ')
        decrypt(cipher, key)
        print(' Decrypt a message')
    elif choice == '3':
        key = input('Enter a composite key: ')
        plaintext = input('Enter a plaintext message: ')
        print('Encrypt then decrypt a message')
        result = encrypt(plaintext, key)
        result = decrypt(result, key)
        print(f'Result: {result}')
    elif choice == "0":
        testEncryption()


if __name__ == '__main__':
    main()
