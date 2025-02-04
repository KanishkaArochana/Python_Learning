# Same name functions but One task at a time.
# The difference between Functions is data types and arguments

# len() --> Inbuild Polymorphism Function

print(len("Python")) # 6 --> String for len() function

print(len([1, 2, 3])) # 3 --> List for len() function

car = {"brand": "Ford", "model": "Mustang", "Year": 1994} 
print(len(car)) # 3 --> Dictionary for len() function

# ===============================================================================

class Ceylon:
    def Capital(self):
        print("Kotte is the capital city of Srilanka")
    def language(self):
        print("Sinhala is the the most widely spoken language of Srilanka")
    def ctype(self):
        print("Sri Lanka is developing country")

class USA:
    def Capital(self):
        print("Washington is the capital city of USA")
    def language(self):
        print("English is the the most widely spoken language of USA")
    def ctype(self):
        print("USA is developing country")

# Create Object

sl = Ceylon()
usa = USA()

# print Using For Loop
for country in (sl, usa):
    country.Capital()
    country.language()
    country.ctype()

# Kotte is the capital city of Srilanka
# Sinhala is the the most widely spoken language of Srilanka
# Sri Lanka is developing country
# Washington is the capital city of USA
# English is the the most widely spoken language of USA
# USA is developing country


# ------------------------- Using Polymorphism Inheritance -------------------------------------

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Moving")

class Boat(Vehicle):
    def move(self):
        print("Sail")

class Car(Vehicle):
    pass

class Plane(Vehicle):
    def move(self):
        print("Flying")

# Create Object
car1 = Car("Toyota", "Supra")
boat1 =  Boat("Sea Ray", "Sundance 350")
plane1 = Plane("Boeing", "A747")

for x in (car1, boat1, plane1):
    print("brand :", x.brand, "model :", x.model)
    x.move() # move function call

# out put -->

# brand : Toyota model : Supra
# Moving  --> move function call

# brand : Sea Ray model : Sundance 350
# Sail  --> move function call

# brand : Boeing model : A747
# Flying --> move function call