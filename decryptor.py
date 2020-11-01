import numpy as np

encryptor = np.array([[12,1],[23,14]])


def encrypt(arr):
    val1 = ord(arr[0]) - 64
    val2 = ord(arr[1]) - 64
    mat = np.array([[val1],[val2]])
    nomod = np.matmul(encryptor,mat)
    modded = np.mod(nomod,26)
    char1 = chr(modded[0][0] + 64)
    char2 = chr(modded[1][0] + 64)

    return [char1,char2]

decryptor = np.array([[14.0,-1.0],[-23.0,12.0]])

def reversemod(num):
    posmod = num
    negmod = num
    while (posmod % 15 != 0):
        posmod += 26
    while (negmod % 15 != 0):
        negmod -= 26
    if abs(negmod) < abs(posmod):
        finalmod = negmod
    else:
        finalmod = posmod
    return finalmod

def decrypt(arr):
    val1 = ord(arr[0]) - 64
    val2 = ord(arr[1]) - 64
    val1 = reversemod(val1)
    val2 = reversemod(val2)
    mat = np.array([[int(val1)],[int(val2)]])
    outmat = np.mod(np.matmul(decryptor, mat) / 15 ,26)
    out1 = chr(int(outmat[0][0]) + 64)
    out2 = chr(int(outmat[1][0]) + 64)
    return [out1, out2]


message = 'MSTMRAAAKPONNURAOMKPAZUYODBCONRTIYCVQGNMYXODBCUAZBKPQB'

finalist = []
charlist = []
cntr = 0

for char in message:
    if cntr % 2 == 1:
        charlist.append(char)
        finalist.append(charlist)
        charlist = []
        cntr = 0
    else:
        charlist.append(char)
        cntr += 1

decrypted = [decrypt(arr) for arr in finalist]
print(finalist)
emptystring = ''

for array in decrypted:
    for character in array:
        emptystring += character
print(emptystring)

pass1 = emptystring.replace('DOT','.')
pass2 = pass1.replace('SLASH','/')
pass3 = pass2.replace('TILDE','~')
print(pass3)
