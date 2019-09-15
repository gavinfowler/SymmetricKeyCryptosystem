# CS5640 Assignment 1

Run with:
```sh
python3 assn1.py
```

Example input for encryption:
```bash
Choose an option:
0. Test Functions
1. Encyrpt a message
2. Decrypt a message
3. Encrypt then decrypt a message
> 1
Enter a composite key: 22024422230021
Enter a plaintext message: A SECRET MESSAGE
```

Example input for decryption:
```bash
Choose an option:
0. Test Functions
1. Encyrpt a message
2. Decrypt a message
3. Encrypt then decrypt a message
> 2
Enter a composite key: 22024422230021
Enter a cipher: 0335625733212121032333331621
```

Example input for encryption and decryption:
```bash
Choose an option:
0. Test Functions
1. Encyrpt a message
2. Decrypt a message
3. Encrypt then decrypt a message
> 1
Enter a composite key: 22024422230021
Enter a plaintext message: A SECRET MESSAGE
```

In this assignment, you need to write a computer programming code to build a cryptosystem
that accommodates multiple steps, each representing a distinct cryptography technique. So, the
system needs a composite key - multiple keys placed adjacent to the next - one for each crypto
technique. In this assignment, the composite key consists of a set of numbers, where each
number has two digits (there will be no space or separator between the numbers or digits, when
they will be given as input to your program). The last number of the key represents the ‘Key’ for
one-time pad crypto technique, and the previous numbers are used to generate a ‘Key’ for
Columnar Transposition crypto technique by using a Polybius square.

Input:

1. Composite Key
2. Plaintext Message

Output:

Cipher message
