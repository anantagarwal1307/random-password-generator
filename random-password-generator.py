# RANDOM PASSWORD GENERATOR

print("RANDOM PASSWORD GENERATOR\n")

from random import choice #For generate a random password

import string #For letters, digits and special symbols

def password(length,num = True, spec = True):
	characters = string.ascii_letters
	digits = string.digits
	symbols = string.punctuation
	
	if num:
		characters += digits
		
	if spec:
		characters += symbols
		
	gen = ""
		
	while len(gen) < length:
		guess = choice(characters)
		gen += guess
		
	print(f"Generated Password is:- {gen}")
		
		
		

length = int(input("Enter a length for a password :- "))

if length <= 0:
	print("Password length never be 0 or less than 0.")

else:
	num = input("Do you want to have numbers (Y/N)?").lower() == "y"
	
	spec = input("Do you want to have special symbols (Y/N)?").lower()  == "y"
	
	password(length, num, spec)		