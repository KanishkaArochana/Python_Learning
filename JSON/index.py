# Using JavaScript Syntac
# Using for data exchange browser and server

# import JSON
import json

# JOSN Serialization --> Json encode (Python convert to Json)
# Using .dump(), .dumps() Methods

#dictionaires
data = { 
    "owner": "Bob",
    "nic": 1234567890,
    "emali": "bobGgmail.com"
}

# Open file & Write
jfile = open("JSON/data_file.json", "w")

#if write a file json usin dump() method
json.dump(data, jfile) #--> Print value in data_file.json file

#---------------------------------------------------------------------------------

# Not file assint but wont string assint using dumps() Methods (Only file import)
json_string = json.dumps(data)
print(json_string) # {"owner": "Bob", "nic": 1234567890, "emali": "bobGgmail.com"}

# Customize data values
json_string = json.dumps(data, indent=4)
print(json_string) 
# {
#     "owner": "Bob",
#     "nic": 1234567890,
#     "emali": "bobGgmail.com"
# }

json_string = json.dumps(data, separators=("," , ":"))
print(json_string) # {"owner":"Bob","nic":1234567890,"emali":"bobGgmail.com"}

# ==========================================================================================

# JOSN Deserialization --> Json encode (Json convert to Phython)
# Using .load(), .loadss() Methods

# Exaple for a Tuples encode to decode

fruits = ("banana", "apple", 2) # Tuples

# Encode
encoded_fruits = json.dumps(fruits)
# Decode ( Not file assint but wont string assint using loads() Methods )
decoded_fruit = json.loads(encoded_fruits)

print(fruits == decoded_fruit) # False

print(type(fruits)) # <class 'tuple'>
print(type(decoded_fruit)) # <class 'list'>

# *** Not equal befor decode elements and after decode element

# ------------------------------------------------------------------

# How to documant Deserialization

jfile = open("JSON/data_file.json", "r")

#if write a file json usin load() method
data = json.load(jfile) #--> Load the value in data_file.json file

print(data, type(data)) # {'owner': 'Bob', 'nic': 1234567890, 'emali': 'bobGgmail.com'}   <class 'dict'>

# ------------------------------------------------------------------

json_string = '{"owner": "Bob", "nic": 1234567890, "emali": "bobGgmail.com"}' # String Formate
print(type(json_string)) # <class 'str'> have a String type data but have json data

data = json.loads(json_string) # Convert to String type data dictionaire type (Json type data)

print(data)# {'owner': 'Bob', 'nic': 1234567890, 'emali': 'bobGgmail.com'}

print(type(data)) # <class 'dict'>