# WAP to check wheather the string provided by the client/user is palidrome or not.
# pop ---> Palindrome
# abcd ---> Not Palindrome


while True:
    a=input("Enter a String : ")

    if a==a[::-1]:
        print("PALINDROME")
        break
    else:
        print("Not Palindrome")
        
