#Enter Plaintext
import numpy as np
P = input("Enter Plain Text: ").upper()

m1=[]
for letter in P:
    m1.append(letter)

## Remove Spaces
for x in range(len(m1)):
    if " " in m1:
        m1.remove(" ")

## Add X or Z between redundant letters
i=0
for e in range(len(m1)//2):
    if m1[i] == m1[i+1]:
        m1.insert(i+1,'X')
    i=i+2

## Make the length of array even
if len(m1)%2 == 1:
    m1.append("X")

## Make blocks
i=0
new=[]
for x in range(1,len(m1)//2+1):
    new.append(m1[i:i+2])
    i=i+2

print(new)

# ##Random Key Generator
# from random import shuffle
# alpha = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
# mat = list(alpha)
# shuffle(mat)

# key = []
# for i in range(5):
#     key.append('')
#     key[i] = mat[5*i : 5*(i+1)]

# key = np.array(key)
# key

key = [['L','G','D','B','A'],['Q','M','H','E','C'],['U','R','N','I','F'],['X','V','S','O','K'],['Z','Y','W','P','T']]

## find position in key matrix
def find_position(key,letter):
    x=y=0
    for i in range(5):
        for j in range(5):
            if key[i][j]==letter:
                x=i
                y=j

    return x,y

####
## Encrypt ##
####

cipher=[]
for e in new:
    p1,q1=find_position(key,e[0])
    p2,q2=find_position(key,e[1])
    if p1 == p2:
        cipher.append(key[p1][(q1+1)%5])
        cipher.append(key[p1][(q2+1)%5])
    elif q1 == q2:
        cipher.append(key[(p1+1)%5][q1])
        cipher.append(key[(p2+1)%5][q2])
    else:
        cipher.append(key[p1][q2])
        cipher.append(key[p2][q1])

C = ''.join(cipher)
print(f'Cipher Text: {C}') ## Cipher Text

####
## Decryption ##
####

new1 = []
i = 0
for x in range(len(cipher)//2):
    new1.append(cipher[i:i+2])
    i=i+2
print(new1)

# Decrypt
plain=[]
for e in new1:
    p1,q1=find_position(key,e[0])
    p2,q2=find_position(key,e[1])
    if p1 == p2:
        plain.append(key[p1][(q1-1)%5])
        plain.append(key[p1][(q2-1)%5])
    elif q1 == q2:
        plain.append(key[(p1-1)%5][q1])
        plain.append(key[(p2-1)%5][q2])
    else:
        plain.append(key[p1][q2])
        plain.append(key[p2][q1])


##Remove Bogus character
for i in range(len(plain)):
    if 'X' in plain:
        plain.remove('X')
        
P = ''.join(plain)
print(f'Plain Text: {P}') ## Plain Text