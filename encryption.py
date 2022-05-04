from microbit import *
 
#ENCRYPTION FUNCTION    

def encrypt(text):
    alpha  = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 123456789:{}'"
    crypta = "I8Hbr9 TsY2a{tJqgMvGNuz3F1of7XASDBncP5kxphUmeVw}QE4dO'L:iKZRjWyCl6"
    result = ""
 
    for letter in text:
        letter = letter.upper()
        index = alpha.find(letter)
        result = result + crypta[index]
 
    return result
 
#MAIN CODE
 
while True:
    sleep(1500)
    plaintext = input("\nEnter a String to Encrypt: \n(Permitted Characters: A-Z, a-z, 1-9, :, {}, ')\n\n")
    
    result = encrypt(plaintext)
 
    print("result =", result)
