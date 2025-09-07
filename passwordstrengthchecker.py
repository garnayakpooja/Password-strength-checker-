def passwordstrengthchecker():
    password=input("Enter your password:")
    import string
    score=0
    haslower=False
    hasupper=False
    hasdigit=False
    hasspecialsymbol=False
    
    for i in password:
        
        if i in string.ascii_lowercase:
            haslower=True
        if i in string.ascii_uppercase:
            hasupper=True
        if i in str(string.digits):
            hasdigit=True
        if i in string.punctuation:
            hasspecialsymbol=True
    if len(password)>=8:
        score+=1
    else:
        print("The password shoould have more than 8 characters")
    if haslower:
        score+=1
    else:
        print("Add lowercase characters to your password")
    if hasupper:
        score+=1
    else:
        print("Add uppercase characters to your password")
    if hasdigit:
        score+=1
    else:
        print("Add digits to your password")
    if hasspecialsymbol:
        score+=1
    else:
        print("Add special symbols to your password")
    if score==5:
        print(" Password Strength:GREAT PASSWORD!")
    elif score==4 or score==3:
        print("Password strength:MODERATE PASSWORD!")
    elif score==1 or score==2:
        print("Password strength:WEAK PASSWORD!")
passwordstrengthchecker()

    