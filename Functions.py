# def function_name(parameters):
   #Code inside the function

def happyBirthday():
    print("Happy Birthday to you")

#Call the function
happyBirthday()

#---------------------------------------------------------------

# How to inpunt data in funtion
def greeting(name):
    print("Welcome", name)

#Call the function
greeting("Kanishka") #W elcome Kanishka
greeting("Arochana") # Welcome Arochana

#---------------------------------------------------------------

# Using Multipale parameter
def info(name, age):
    print("Name: ", name)
    print("Age: ", age)

info("Kanishka" ,24)
# Name:  Kanishka
# Age:  24

info(25 ,"Arochana")
# Name:  25
# Age:  Arochana

# --------------------------- Return ------------------------------

# Can not a result display but can result output 

def add():
    return 3 + 3

print(add()) #6

# ==================================== Function 2 ===================================================

def name(fname, lname):
    print("Hello," + fname + " " + lname)

# Call the function
name("Kanishka", "Arochana") # Hello,Kanishka Arochana

# name("Kanishka") # Error --> TypeError: name() missing 1 required positional argument: 'lname' (Two Araguments have)

