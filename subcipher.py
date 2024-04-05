import random

# function declarations
def makeKey(alphabet,number,cipherkey):
    for i in range(1,len(alphabet)+1):
        randnum = random.choice(number)
        cipherkey[alphabet[i]] = alphabet[randnum]
        number.remove(randnum)
    with open('SubCipherKey.txt', 'w+') as file:
        for key in cipherkey.keys():
            file.write(f"{key} : {cipherkey[key]}\n")

def encrypt(message, cipherkey):
    code = ''
    for i in range(len(message)):
        code += cipherkey[message[i]]

    return code

def decrypt(code, cipherkey):
    decrypted = ''
    for i in range(len(code)):
        decrypted += list(cipherkey.keys())[list(cipherkey.values()).index(code[i])]

    return decrypted



message = input().replace(" ","").lower()
print(message)

alphabet = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k',
             12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 
             22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}
number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
cipherkey = {}

makeKey(alphabet, number, cipherkey)

code = encrypt(message, cipherkey)
print(f"Encrypted: {code}")

brokeIT = decrypt(code, cipherkey)
print(brokeIT)
