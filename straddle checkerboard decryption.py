def decrypyt_straddle_checkerboard(key,ciphertext,a,b):
    matrix= [["" for x in range(10)] for y in range(3)]
    ciphertext = str(ciphertext)
    a=int(a)
    b=int(b)
    r=0
    c=0
    i=0
    while i in range(len(key)):
        
        if r==0 and c==a :
            matrix[r][c] = ""
            c=c+1
            
            if c==10:
             r=r+1
             c=0
            continue
        elif r==0 and c==b:
            matrix[r][c] = ""
            c=c+1
            
            if c==10:
             r=r+1
             c=0

            continue
        matrix[r][c] = key[i]
        i = i+1
 
        c=c+1
        if c==10:
            r=r+1
            c=0
        if i == 26:
           break


    cipherMatrix = []
    a = str(a)
    b = str(b)
    j = 0 
    while j in range(len(ciphertext)):
       
       if ciphertext[j] == a or ciphertext[j]== b:
          
          joined_cipher = ciphertext[j]+ciphertext[j+1]           
          cipherMatrix.append(joined_cipher)          
          j=j+2          
          
       else: 
          cipherMatrix.append(ciphertext[j])
          j=j+1
 
    a = int(a)
    b = int(b)
    plaintextMatrix = []
    for i in range(len(cipherMatrix)):
       cipherMatrix = list(map(int, cipherMatrix))
       if cipherMatrix[i]<10:
          plaintextMatrix.append(matrix[0][cipherMatrix[i]])
       elif cipherMatrix[i]//10==a:
          plaintextMatrix.append(matrix[1][cipherMatrix[i]%10])
       else:
          plaintextMatrix.append(matrix[2][cipherMatrix[i]%10])

    plaintext = ""
    for x in plaintextMatrix:
       for i in x:
          plaintext += i      
   
    return plaintext

key = input("Enter the key:")
a,b = input("Enter the size of matrix:").split()
ciphertext = input("Enter the ciphertext:")


plaintext = decrypyt_straddle_checkerboard(key,ciphertext,a,b)
print("The plaintext is",plaintext)


