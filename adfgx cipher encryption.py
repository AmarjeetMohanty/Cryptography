import math

def encrypt_adfgx_cipher(key,polybius,plaintext):
    key = key.upper()
    polybius = polybius.upper()
    plaintext = plaintext.upper()
    arr1 = ['A','D','F','G','X']
    arr2 =  []
    for i in range(len(key)):
        arr2.append(key[i])
    matrix= [["" for x in range(5)] for y in range(5)]
    r = 0
    c = 0
    for i in range(len(polybius)):
        matrix[r][c] = polybius[i]
        if c==4:
            r = r+1
            c=0
        else:
            c=c+1
    
    ciphertext1 = []
    i = 0
    while i in range(len(plaintext)):
       r = 0
       c = 0
       while r<=4 and c<=4:
        if plaintext[i]==matrix[r][c]:
            ciphertext1.append(arr1[r])
            ciphertext1.append(arr1[c])
            if c==4:
                r = r+1
                c = -1
            c= c+1
            
        else:
            if c==4:
                r = r+1
                c = -1
            c= c+1
       i+=1
    
    matrix2 = [["" for x in range(len(key))] for y in range(math.ceil(len(ciphertext1)/len(key)))]
    transposeMatrix = [["" for x in range(math.ceil(len(ciphertext1)/len(key)))] for y in range(len(key))]
    r = 0
    c = 0
    for i in range(len(ciphertext1)):
        matrix2[r][c] = ciphertext1[i]
        if c==len(key)-1:
            r = r+1
            c=0
        else:
            c=c+1
    
    for i in range(len(matrix2)):
   # iterate through columns
      for j in range(len(matrix2[0])):
        transposeMatrix[j][i] = matrix2[i][j]
    # list(map(int, transposeMatrix))
    indices = [i for i, _ in sorted(enumerate(arr2), key=lambda x: x[1])]
    ciphertextMatrix = []
    r = 0
    c = 0
    while r in range(len(key)) and c in range(math.ceil(len(ciphertext1)/len(key))):
        ciphertextMatrix.append(transposeMatrix[indices[r]][c])
        c = c+1
        if c==math.ceil(len(ciphertext1)/len(key)):
            r =r+1
            c = 0
    return ciphertextMatrix


key = input("Enter the columnar key: ")
polybius = input("Enter the polybius square key: ")
plaintext = input("Enter the plain text:")
ciphertextmatrix = encrypt_adfgx_cipher(key,polybius,plaintext)
ciphertext = ""
for x in ciphertextmatrix:   
    for i in x:  
        ciphertext += i  
    

print("The ciphertext is",ciphertext)