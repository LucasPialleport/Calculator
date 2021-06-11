
#Oppération de base :
def addition(x:float, y:float):
    return x+y

def soustraction(x:float, y:float):
    return x-y

def multiplication(x:float, y:float):
    return x*y

def division(x:float, y:float):
    if y == 0 : return "NULL : divided by zero"
    return x/y

def carre(x:float):
    return  x*x