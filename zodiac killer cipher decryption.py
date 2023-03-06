import math
def decrypt_zodiac_cipher(key,ciphertext):
    key = int(key)
    column = key
    row = math.ceil(len(ciphertext)/key)
    matrix= [["" for x in range(column)] for y in range(row)]
    r = 0
    c = 0
    count = 0
    for i in range(len(ciphertext)):
        
        matrix[r][c] = ciphertext[i]
        r = r+1
        c = c+2
        c = c%column
        if r==row:
            r = 0
            count = count+1
            c = count
            continue
    
    plaintext = ""
    for x in matrix:   
        for i in x:  
            plaintext += i   

    return plaintext

key  = input("Enter the key:")
ciphertext = input("Enter the ciphertext:")

plaintext = decrypt_zodiac_cipher(key,ciphertext)
print("The plaintext is",plaintext)
