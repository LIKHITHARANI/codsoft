import random
import string

def generate_password(length):
    
    characters=string.ascii_letters +string.digits +string.punctuation
    
    password=' '.join(random.choice(characters)for _ in range(length))
    
    return password

def password():
    
    try:
    
        length=int(input("Enter the desired password length: "))
    
        if length<=0:
    
            print("Password length must be a positive number.")
    
        else:
    
            password=generate_password(length)
    
            print("Generated Password: ",password)
    
    except ValueError:
    
        print("Invalid input.Please enter a valid positive integer for password length.")

password()                
