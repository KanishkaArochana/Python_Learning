# Module import --> Import module_name
import MyModules

# Modules Rename (Using as Keyword)
   #import module_name as alias_name
import MyModules as md

# Access to function in MyModules File
MyModules.greeting("Bob") # out put --> Hello Bob
MyModules.bye("John") # out put --> Good Bye John

# -------------------------------------------------------------

# Access to Dictionaires (Variables) in MyModules File
x = MyModules.person1["name"]
print(x) # Bob

x = md.person1["age"]
print(x) # 27

# ============================ Phython Built-in Modules ==========================
# Using muth Modules
import math

print(math.sqrt(25)) # 5.0
print(math.pow(2, 3)) # 2**3 -->8.0
print(math.pi) # 3.141592653589793

# -------------------------------------------------------------

# Using random Modules
import random

print(random.randint(0, 5)) # Out put in Between 0 and 5 int random number
print(random.random()) # Out put in Between 0 and 1 float random number 
print(random.random() * 100) # Out put in Between 0 and 100 float random number 

lst = [1, 5, "hello", True, 1.7]
print(random.choice(lst)) # Output in random value in list

# -------------------------------------------------------------

# Using platform Modules
import platform

print(platform.system()) # Windows --> our operating system name return

# -------------------------------------------------------------

# Using datetime Modules
import datetime
import time

print(time.time()) # return time 
print(datetime.datetime(2024, 5, 23))  # 2024-05-23 00:00:00

# -------------------------------------------------------------

# Using dir() function
   # All propites and function in this run file

print(dir())

list = [1, 2, 3, 4, 5]
print(dir(list)) # return the all function using list

# Assint math module
import math
print(dir(math))  # return the all function using math module



# ============================ from - import Modules ==========================
# Use to Mthod of Modules
from MyModules import person1

print(person1) # --> {'name': 'Bob', 'age': 27, 'country': 'USA'}
print(person1["country"]) # --> USA

print(MyModules.person1["country"]) # --> Error

# -------------------------------------------------------------
# Can import need to propityes 
from math import pow, sqrt

print(sqrt(16)) # 4.0
print(pow(4, 3)) # 64.0
print(pi) # Error --> Only import pow, sqrt propeties

# -------------------------------------------------------------
# Can all propityes import
        # from module_name import *
from math import *

print(sqrt(16)) # 4.0
print(pow(2, 3)) # 8.0
print(pi) # 3.141592653589793 --> All propeties import math modules

# My module import
from MyModules import *

greeting("John") # Hello John
bye("Alex") # Good Bye Alex
