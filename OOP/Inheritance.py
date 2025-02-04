# Inheritance --> Acess to propatice in Child Class

# Parant Class
class Person:
    #Constaction
    def __init__(self, name):
        self.name  = name

    # Methods
    def eat(self, food):
        print("Person is eating", food)

    def sleep(self):
        print("Person is sleeping...")

# Child class(Employee)
# Inheritance in class
class Employee(Person): # # Inherited 'Person'
    def __init__(self, dep, name):
        super(Employee, self).__init__(name) # Method override (Perant class have function in freedifine chile class)
        self.dep = dep

    def work(self):
        print("Employee is working...")

    def leave(self):
        print("Employee is leaving...")

# Create Object
emp1 = Employee("IT", "Bob")
emp1.eat("apple") # Person is eating apple
print(emp1.name) # Bob

emp2 = Employee("HR", "John")
print(emp2.name) # John


# ------------------------- Multipal  Inheritance --------------------------------

# Class 1
class Car:
    def __init__(self):
        self.name1 = "Lightning"
        print("Going")


# Class 2
class Flyable:
    def __init__(self):
        self.name2 = "Flyer"
        print("Flying")


# Class 3
class FlayingCar(Car, Flyable):
    def __init__(self):
        Car.__init__(self)
        Flyable.__init__(self)
        print("Inherited")

    def printName(self):
        print(self.name1, self.name2)

# Create Object
ob = FlayingCar()
# John
# Going
# Flying
# Inherited

ob.printName() # Lightning Flyer