import string
import random
def passgen(min_len, number = True, special_char = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if number:
        characters += digits
    if special_char:
        characters += special
    
    pwd = ""
    moc = False
    has_num = False
    has_sc = False

    while not moc or len(pwd) < min_len:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_num = True
        elif new_char in special:
            has_sc = True
        
        moc = True
        if number:
            moc = has_num
        if special_char:
            moc = moc and has_sc
    return pwd

min_len = int(input("Enter the minimum length: "))   
number = input("Do you want to include numbers (y/n)? ").lower() == "y"   
special_char = input("Do you want to include special character (y/n)? ").lower() == "y"
print("Password: ",passgen(min_len, number, special_char))