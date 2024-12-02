def encryption(txt, s):  
    result = ""   
    for i in range(len(txt)):  
        char = txt[i]  
        if (char.isupper()):  
            result += chr((ord(char) + s - 65) % 26 + 65)  
        else:  
            result += chr((ord(char) + s - 97) % 26 + 97)  
    return result  
 
txt =input("Enter the string: ")
s = int(input("Enter the key: "))
  
print("Plain txt : " + txt)  
print("Shift pattern : " + str(s))  
print("Encrypted text: " + encryption(txt, s))

def decryption(ciphertext, shift):
    plaintext = ""
    
    for char in ciphertext:
        if char.isalpha():  
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            shifted_char = chr(start + (ord(char) - start - shift_amount) % 26)
            plaintext += shifted_char
        else:
            plaintext += char 
            
    return plaintext
ciphertext = input("Enter string :")
shift = int(input("Enter key:"))
plaintext = decryption(ciphertext, shift)
print(f"Decrypted text: {plaintext}")
