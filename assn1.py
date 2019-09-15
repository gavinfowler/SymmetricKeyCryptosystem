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

    cipher = cipher.upper()
    return cipher


def xor(binaryArr, binaryKey):
    """
    function to do an XOR on binary
    """
    result = ''
    for i in binaryArr:
        xor = int(i, 2) ^ int(binaryKey, 2)
        strXor = str(xor)
        if len(strXor) == 1:
            strXor = '0' + strXor
        result += strXor
    return result


def testEncryption():
    """
    Function to test encryption
    """
    # Unit Tests
    # Test compositeKeyGen
    compositeKeyGenResult = compositeKeyGen("1422555515")
    assert compositeKeyGenResult['keyForColumn'] == 'BALL'
    assert compositeKeyGenResult['pad'] == '001111'

    compositeKeyGenResult = compositeKeyGen('22024422230021')
    assert compositeKeyGenResult['keyForColumn'] == 'ARCANE'
    assert compositeKeyGenResult['pad'] == '010101'
    print('compositeKeyGen passed')

    # Test columnarTransposition
    columnarTranspositionResult = columnarTransposition(
        "This is a TeSt", 'BALL')
    assert columnarTranspositionResult == 'HSSTIEIATST'

    columnarTranspositionResult = columnarTransposition(
        "A SECRET MESSAGE", 'ARCANE')
    assert columnarTranspositionResult == 'ATGCSEEEARSSME'
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

    # Integration Test
    cipher = encrypt('A SECRET MESSAGE', '22024422230021')
    assert cipher == '0335625733212121032333331621'


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

def decryptOneTimePad(msg, key):
    intAry = []
    rsltStr = ''
    for x in msg:
        intAry.append(int(x, 2) ^ int(key, 2))
    for y in intAry:
        intStr = str(y)
        if len(intStr) == 1:
            intStr = '0' + intStr
        rsltStr += intStr
    return rsltStr

def decryptColumnarTransposition(msg, key):
    tempMsg = msg
    numRows = math.ceil(len(msg)/len(key))
    colsWithExtras = len(msg) % len(key)

    lettersWithExtras = []
    extrasCount = 0
    for i in key:
        lettersWithExtras.append(i)
        extrasCount += 1
        if extrasCount >= colsWithExtras:
            break

    arr = []
    count = 0

    # Building array with key
    for letter in key:
        # letter = letter + str(count)
        arr.append([letter])
        count += 1
    arr.sort()

    # populating array
    count = 0
    for letter in arr:
        numRowsForArr = numRows
        if letter[0] in lettersWithExtras:
            lettersWithExtras.remove(letter[0])
        else:
            numRowsForArr -= 1
        tempLetters = tempMsg[0:numRowsForArr]
        tempMsg = tempMsg[numRowsForArr:]
        for i in tempLetters:
            arr[count].append(i)
        count += 1

    # Sorting build array using key
    newArr = []
    for letter in key:
        for i in range(0, len(arr)):
            if arr[i][0] == letter:
                temp = arr.pop(i)
                newArr.append(temp)
                break

    # Getting values
    plaintext = ''
    rowCount = 1
    colCount = 0
    for i in range(0,len(msg)):
        plaintext += newArr[colCount][rowCount]

        colCount += 1

        if colCount > len(key) - 1:
            colCount = 0
            rowCount += 1

    return plaintext

def getFromPolybiusNumbersToLetters(numbers):
    keyForColumn = ''
    for i in range(0, len(numbers), 2):
        # print(f'numbers[i ]: {numbers[i]}')
        # print(f'numbers[i + 1]: {numbers[i + 1]}')
        keyForColumn += POLYBIUS[int(numbers[i + 1])][int(numbers[i])]
        # print(f'POLYBIUS[numbers[i + 1]][numbers[i]]: {POLYBIUS[int(numbers[i + 1])][int(numbers[i])]}')
    return keyForColumn


def decrypt(msg, key):
    """
    Function to decrypt a plaintext message using a key
    """
    print(msg)
    print(key)
    compositeKeyGenResult = compositeKeyGen(key)
    print('\nBegin decrypt')
    binary = cipherToBinary(msg)
    print(f'Binary: {binary}')
    padkey = compositeKeyGenResult['pad']
    print(f'KeyGen: {padkey}')
    padResult = decryptOneTimePad(binary, padkey)
    print(f'padResult: {padResult}')
    #insert getting string of letters from Polybius here
    polybiusResult = getFromPolybiusNumbersToLetters(padResult)
    print(f'polybiusResult: {polybiusResult}')
    colKey = compositeKeyGenResult['keyForColumn']
    print(f'colKey: {colKey}')
    plaintext = decryptColumnarTransposition(polybiusResult, colKey)
    print(f'plaintext: {plaintext}')
    print('End decrypt')
    return msg

####### GENERAL FUNCTIONS ##########
def validateKeyLen(key):
    if len(key) % 2 != 0:
        raise Exception(
            'Error: Key given was of odd length')
    if len(key) <= 0:
        raise Exception(
            'The key was not long enough to generate a key and a pad')
    if not key.isdigit():
        raise Exception(
            'Error: key is not numeric')


def compositeKeyGen(key):
    """
    Function generate key for columnar transposition
    Test with entering a '0' on selection
    """
    pad = '{0:06b}'.format(int(key[-2:]))
    key = key[:-2]
    validateKeyLen(key)
    # print(key)
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
        print()
        decrypt('0335625733212121032333331621', '22024422230021')


if __name__ == '__main__':
    main()
