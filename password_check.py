def is_valid_password(pw):

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
    

print(is_valid_password("short1A"))
print(is_valid_password("longenough"))
print(is_valid_password("Longenough1"))
