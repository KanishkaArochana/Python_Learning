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

