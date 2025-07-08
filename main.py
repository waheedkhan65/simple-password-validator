passkey = input("Enter your passkey: ")
if len(passkey) >= 8:
    has_digit = any(char.isdigit() for char in passkey)
    has_char = any(char.isalpha() for char in passkey)
    
    if has_digit and has_char:
        print("Password is valid")
    else:
        print("Password is invalid")    
        if not has_digit:
            print("* Must contain numbers")
        if not has_char:
            print("* Must contain characters")   
else:
    print("Password is invalid\nPassword is must be 8 characters long")