username = "molmotor"
password = "molmotor123"

usernameinput = input("Enter username:")
if usernameinput == username:
    passwordinput = input("Please enter your password:")
    if passwordinput == password:
        print("valid")
    else:
        print("invalid")
else:
    print("invalid")
