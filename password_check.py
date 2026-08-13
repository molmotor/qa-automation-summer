def is_valid_password(pw):
    # returns True if pw is at least 8 characters,
    if len(pw) >= 8:
        if any(char.isdigit() for char in pw) == True:
            if any(char.isupper() for char in pw) == True:
                return True
            else:
                return False
        else:
            return False

    else:
        return False    
    # has at least one digit, and at least one uppercase letter
    # returns False otherwise
    

print(is_valid_password("short1A"))
print(is_valid_password("longenough"))
print(is_valid_password("Longenough1"))