usernames = ["molmotor", "web", "hil", "sjks", "user with space", "user with number 22 and space", "userwithnumber44"]

for username in usernames :
    if len(username) < 5 or ' ' in username : 
        print(username, "is invalid")
    else:
        print(username, "is valid")