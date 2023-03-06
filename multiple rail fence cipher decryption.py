import math
import os
import random
import re
import sys


def decrypt_char_rail_fence(key,cipher_text):
    cipher_text = cipher_text.upper()
    rail = [['\n' for i in range(len(cipher_text))]
                for j in range(key)]
     

    dir_down = None
    row, col = 0, 0
     

    for i in range(len(cipher_text)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
         
        # place the marker
        rail[row][col] = '*'
        col += 1
         
        # find the next row
        # using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
             

    index = 0
    for i in range(key):
        for j in range(len(cipher_text)):
            if ((rail[i][j] == '*') and
            (index < len(cipher_text))):
                rail[i][j] = cipher_text[index]
                index += 1
         

    result = []
    row, col = 0, 0
    for i in range(len(cipher_text)):
         

        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
             

        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
             

        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))

def multiple_char_decrypt(number_of_times,key,text):
    for i in range(number_of_times):
        text = decrypt_char_rail_fence(key,text)
    return text

def remove_filler(filler,text):
    filler = filler.upper()
    text = text.replace(filler," ")
    return text

def decrypt_word_rail_fence(key,intermidiate):
    words = intermidiate.split()
    rail = [['\n' for i in range(len(words))]
                for j in range(key)]
     

    dir_down = None
    row, col = 0, 0
     

    for i in range(len(words)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
         
    
        rail[row][col] = '*'
        col += 1
         
        
        if dir_down:
            row += 1
        else:
            row -= 1
             

    index = 0
    for i in range(key):
        for j in range(len(words)):
            if ((rail[i][j] == '*') and
            (index < len(words))):
                rail[i][j] = words[index]
                index += 1
         

    result = []
    row, col = 0, 0
    for i in range(len(words)):
         

        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
             

        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
             

        if dir_down:
            row += 1
        else:
            row -= 1
    return(" ".join(result))

def multiple_word_decrypt(number_of_times,key,text):
    for i in range(number_of_times):
        text = decrypt_word_rail_fence(key,text)
   
    return text


N = input("Enter the number of times the word railfence is applied:") # integer, the number of times the word railfence is applied
N = int(N)
n = input("Enter number of levels for word railfence cipher") # integer, number of levels for word railfence cipher
n = int(n)
M = input("Enter the number of times character level railfence cipher is applied:") # integer, the number of times character level railfence cipher is applied
M = int(M)
m = input("Enter the number of levels in character level railfence cipher:") # integer, the number of levels in character level railfence cipher
m = int(m)
X = input("Enter string to replace the spaces in the text: ") # string, to replace the spaces in the text
cipher_text = input("Enter the ciphertext:") #cipher text


cipher_text = multiple_char_decrypt(M,m,cipher_text)
cipher_text = remove_filler(X,cipher_text)
plain_text = multiple_word_decrypt(N,n,cipher_text)
print("The plaintext is",plain_text)
