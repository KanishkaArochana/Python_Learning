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

