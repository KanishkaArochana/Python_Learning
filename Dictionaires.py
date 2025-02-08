# Data store in table
# Use Key Value Pair

bag = {"Pencils": 3, "Pens": 2, "Book": "Harry Potter"}
print(bag) # {'Pencils': 3, 'Pens': 2, 'Book': 'Harry Potter'}
print(type(bag)) # <class 'dict'>

# Can not use duplicate vales

car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "year" : 2020,
    "model" : "Explorer"
}
print(car) # {'brand': 'Ford', 'model': 'Explorer', 'year': 2020}


person = {
    "Name" : "Boob",
    "Age" :21,
    "Height" : 6.2
}

print(person.keys()) # dict_keys(['Name', 'Age', 'Height'])
print(person.values()) # dict_values(['Boob', 21, 6.2])
print(person.items()) # dict_items([('Name', 'Boob'), ('Age', 21), ('Height', 6.2)])

#Acces Value

x = person["Name"]
print(x) # Boob

x = person.get("Name")
print(x) # Boob

x = person.get("Weight")
print(x) # None

# ------------------------ Add value -----------------------------------------------------
    # variable_name[key] = value

dict = {}

dict[0] = "Bob"
dict[1] = "John"
dict[2] = "Rock"

dict["Age"] = [20, 33, 24]
print(dict) # {0: 'Bob', 1: 'John', 2: 'Rock', 'Age': [20, 33, 24]}

# ------------------------ Update value-----------------------------------------------------
    # variable_name[key] = value

vehicle = {"brand": "Ford", "model": "Mustang","year": 2020}
# Befor Update
print(vehicle) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

vehicle["brand"] = "Jeep"
vehicle["model"] = "Compass"
vehicle["year"] = 2022
# After Update
print(vehicle) # {'brand': 'Jeep', 'model': 'Compass', 'year': 2022}

# ---------------------------------- Iteam Remove -----------------------------------------------------

# 1.pop()
  #variable_name.pop(key)

vehicle = {"brand": "Ford", "model": "Mustang","year": 2020}
# Befor  Remove 
print(vehicle) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

vehicle.pop("model")

# After  Remove (Remove the model key)
print(vehicle) # {'brand': 'Ford', 'year': 2020}


# 2.del()
  # del variable_name[key]

vehicle = {"brand": "Ford", "model": "Mustang","year": 2020}
# Befor  Remove 
print(vehicle) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

del vehicle["brand"]

# After  Remove (Remove the brand key)
print(vehicle) # {'model': 'Mustang', 'year': 2020}

# All delete Dictionaires
del vehicle
print(vehicle) # NameError: name 'vehicle' is not defined

# ---------------------------------- Key Output -----------------------------------------------------

car = {"brand": "Ford", "model": "Mustang","year": 2020}


for x in car:
  # Print Keys
    # print(x)
# brand
# model
# year

# Print Vales
 print(car[x])
# Ford
# Mustang
# 2020

# Print Keys and Values
 print(x,car[x])
# model Mustang
# 2020
# year 2020

car = {"brand": "Ford", "model": "Mustang","year": 2020}
  # Print Keys
print(car.keys())

for x in car.keys():
 print(x)
# dict_keys(['brand', 'model', 'year'])
# brand
# model
# year
 
print("_________________________________________")

# Print Vales
print(car.values())

for x in car.values():
 print(x)
# dict_values(['Ford', 'Mustang', 2020])
# Ford
# Mustang
# 2020

print("_________________________________________")

# Print Keys and Values
print(car.items())

for x in car.items():
 print(x)
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])
# ('brand', 'Ford')
# ('model', 'Mustang')
# ('year', 2020)