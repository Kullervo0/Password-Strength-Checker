import string
print("\n\n\n\nThis program will check how secure Your password is!\n")

while True:
    password = str(input("Enter your password:\n\n"))
    length = False
    hasUpper = False
    hasLower = False
    hasNumber = False
    hasSpecial = False
    flag = True
    if len(password) > 13:
        length = True
    
    for x in password:
        if x.isupper():
            hasUpper = True
        if x.islower():
            hasLower = True
        if x.isdigit():
            hasNumber = True
        if x in string.punctuation:
            hasSpecial = True

    if hasUpper == False:
        print("You need an Uppercase letter")
        flag = False
    if hasLower == False:
        print("You need a Lowercase letter")
        flag = False
    if hasNumber == False:
        print("You need a Number")
        flag = False
    if hasSpecial == False:
        print("You need a Special Character")
        flag = False
    if length == False:
        print("You need a longer password")
        flag = False
    if flag == True:
        print("Your password is secure!")
    password = None