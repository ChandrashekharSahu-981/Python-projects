import random
print("Welcome to Password Generator!")
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', 
    '_', '`', '{', '|', '}', '~']

require_letters=int(input("Enter the number of letters you want in your password: "))
require_digits=int(input("Enter the number of digits you want in your password: "))
require_symbols=int(input("Enter the number of symbols you want in your password: ")) 

password_list=[]
for char in range(0,require_letters):
    password_list += random.choice(letters)
    
for char in range(0,require_digits):
    password_list += random.choice(digits)

for char in range(0,require_symbols):
    password_list += random.choice(symbols)

print("Your password is: ")
for char in password_list:
    print("".join(random.choice(password_list,)),end="")