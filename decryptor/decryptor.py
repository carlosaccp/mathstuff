import numpy as np

#This is the array used to encrypt the message
encryptor = np.array([[12,1],[23,14]])

#Function that encrypts a 2-character array using the method in TreasureHunt.pdf
def encrypt(arr):
    #Turn the characters into usable numbers
    val1 = ord(arr[0]) - 64
    val2 = ord(arr[1]) - 64
    #Turn the numbers into a 2-array that can be used for matrix multiplication using np.matmul()
    mat = np.array([[val1],[val2]])
    #Mulitply the encryptor array with the character-value array to encrypt the message
    nomod = np.matmul(encryptor,mat)
    #Mod the resultant matrix mod 26 so every number can be associated with a letter of the alphabet
    modded = np.mod(nomod,26)
    #Turn the numbers in the resultant matrix into characters
    char1 = chr(modded[0][0] + 64)
    char2 = chr(modded[1][0] + 64)
    
    #Output the characters
    return [char1,char2]

#This is the decrpytor array, which is the inverse of the matrix. Had to times by determinant so the decimal approximation is undone as that alters the
#values when doing ord() as 0.9999999213 is floored to 0 and a char that should be 'A' is turned into an '@'.
det = np.linalg.det(encryptor)
decryptor = np.linalg.det(encryptor) * np.linalg.inv(encryptor)

#Function that finds the least congruent value of a number mod 26 that is also divisible by the det of the encryptor matrix - necessary condition for uniqueness in 
#mod matrix equations. To undo this, we must find a number congruent to the orignal number mod 26 that is also divisible by the determinant of the encryptor matrix.

def reversemod(num):
    posmod = num
    negmod = num
    #Finds the first positive number congruent to num mod 26 and divisible by the det of the encryptor matrix
    while (posmod % det != 0):
        posmod += 26
    #Finds the first negative number congruent to num mod 26 and divisible by the det of the encryptor matrix
    while (negmod % det != 0):
        negmod -= 26
    #Compares both numbers congruent to num mod 26 and chooses the one with the smallest absolute value
    if abs(negmod) < abs(posmod):
        finalmod = negmod
    else:
        finalmod = posmod
    return finalmod

#Function that decrpyts a 2-encrypted-character 2-dimensional array
def decrypt(arr):
    #Turns char into useful numbers
    val1 = ord(arr[0]) - 64
    val2 = ord(arr[1]) - 64
    #Find smallest number congruent to val1 divisible my the determinant of the encryptor matrix
    val1 = reversemod(val1)
    val2 = reversemod(val2)
    #Turns the numbers into a 2-array ready to use with matmul()
    mat = np.array([[int(val1)],[int(val2)]])
    #Multiplies the decryptor matrix with the character-value matrix and then finds the values mod-26. This last step is important as we must find values mod 26 to map the alphabet
    outmat = np.mod(np.matmul(decryptor, mat) / det ,26)
    out1 = chr(int(outmat[0][0]) + 64)
    out2 = chr(int(outmat[1][0]) + 64)
    return [out1, out2]

#Message to be decrypted
message = 'MSTMRAAAKPONNURAOMKPAZUYODBCONRTIYCVQGNMYXODBCUAZBKPQB'

#Setting to divide the message into arrays with 2 elements ready for processing
finalist = []
charlist = []
cntr = 0

#For loop divides array into arrays with 2 elements
for char in message:
    if cntr % 2 == 1:
        charlist.append(char)
        finalist.append(charlist)
        charlist = []
        cntr = 0
    else:
        charlist.append(char)
        cntr += 1

#Pass all the 2-arrays into decrypt using a list comprehension to decrypt them
decrypted = [decrypt(arr) for arr in finalist]
print(finalist)

#Join all the 2-arrays to receive final message
emptystring = ''

for array in decrypted:
    for character in array:
        emptystring += character

#Print the final message
print(emptystring)

#Replace 'DOT', 'SLASH' and 'TILDE' with '.', '/' and '~'
pass1 = emptystring.replace('DOT','.')
pass2 = pass1.replace('SLASH','/')
pass3 = pass2.replace('TILDE','~')
#Print the final pass
print(pass3)
