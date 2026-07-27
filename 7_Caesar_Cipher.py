alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print("Welcome to \n",logo)
def cipher(direction,text,shift):
        if direction == 'encode':
            encrypted_text = ""
            for char in text:
                if char not in alphabet:
                    encrypted_text += char
                else:   
                    encrypted_text += alphabet[(alphabet.index(char)+shift)%26]
            print(f"Your encrypted message is: {encrypted_text}" )
        elif direction == 'decode':
            decrypted_text = ""
            for char in text:
                if char not in alphabet:
                    decrypted_text += char
                else:
                    decrypted_text += alphabet[(alphabet.index(char)-shift)%26]
            print(f"Your decrypted message is: {decrypted_text}")
        else: 
            print("Invalid direction input!")

value = True
while value:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    cipher(direction,text,shift)

    value=input("Type 'yes' to continue again or 'no' to exit: ").lower()
    if value == 'yes':
        value=True
    elif value == 'no':
        value= False
        print("Thank You!")
    else:
        value=False
        print("Invalid input!")

