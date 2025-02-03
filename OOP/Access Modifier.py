# private --> __name (2 underscores)
# protected --> _name (Use only child class) (1 underscore)

class Person:
    def __init__(self, name, weight, height):
        self.name = name # public variable
        self.__bmi = weight/(height*height) # private variable

    def walk(self):
        print(self.name, "is walking...")

# ---------------- Encapsulation (Getter & Setter) ----------------------

# Get Methods
    def get_bmi(self):
        return self.__bmi # private variable (__bmi)

# Set Methods
    def set_bmi(self, bmi):
        self.__bmi = bmi # private variable(__bmi)

# Creating an instance of Person
bob = Person("Bob", 60, 1.52)

print("Name is :", bob.name) # because public variable is can accsess --> Name is : Bob
print("BMI is :", bob.__bmi) # because private variable is can not accsess (Error --> AttributeError: 'Person' object has no attribute '__bmi')

# Trying to change the private variable directly will not affect the original private variable
bob.__bmi = 70 # private variable --> This creates a new instance variable, does not change the original __bmi


print("Before change the BMI,", bob.get_bmi()) # Before change the BMI, 25.969529085872576
bob.set_bmi(30)
print("After changing the BMI,", bob.get_bmi()) # After changing the BMI, 30

print("Outer BMI", bob.__bmi) # Outer BMI 70 (this is a new instance variable, not the private __bmi)