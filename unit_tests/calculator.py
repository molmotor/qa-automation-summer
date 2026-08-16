def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return("invalid!")
    else:
        return a/b


print(add(3, 5))
print(subtract(10, 4))
print(multiply(6, 7))
print(divide(10, 0))
print(divide(10, 2))