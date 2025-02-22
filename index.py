# Data Types

# 1.String
x = "Hello World"

#display x:
print("String is :" , x) # String is : Hello World

#display the data type of x:
print(type(x))  #<class 'str'>

# 2.Interger
x = 20

#display x:
print(x) # 20

#display the data type of x:
print(type(x))  #<class 'int'>

# 3. Float
x = 20.5

#display x:
print(x) # 20.5

#display the data type of x:
print(type(x))  #<class 'float'>

# 4.Complex
x = 1j

#display x:
print(x) # 1j

#display the data type of x:
print(type(x))  #<class 'complex'>

# 5.List (Used to store multipla value in one variable --> [])
x = ["apple", "banana", "cherry", 41]

#display x:
print(x)  # ['apple', 'banana', 'cherry', 41]

#display the data type of x:
print(type(x)) # <class 'list'>


# 6.Tuple (Same to list but after assint value do not change --> () )
x = ("apple", "banana", "cherry")

#display x:
print(x)  # ['apple', 'banana', 'cherry']

#display the data type of x:
print(type(x))  # <class 'tuple'>


# 7.Range
x = range(6)

#display x:
print(x)  # range(0, 6)

#display the data type of x:
print(type(x))  # <class 'range'>


# 8.Dictionary (Use to key value pair --> {} )
x = {"name" : "John", "age" : 36}

#display x:
print(x) # {'name': 'John', 'age': 36}

#display the data type of x:
print(type(x)) # <class 'dict'>


# 9.Set
x = {"apple", "banana", "cherry"}

#display x:
print(x) # {'apple', 'banana', 'cherry'}

#display the data type of x:
print(type(x)) # <class 'set'>


# 10.Frozenset
x = frozenset({"apple", "banana", "cherry"})

#display x:
print(x) # frozenset({'banana', 'apple', 'cherry'})

#display the data type of x:
print(type(x)) # <class 'frozenset'>


# 11.Boolian
x = True

#display x:
print(x) # True

#display the data type of x:
print(type(x)) # <class 'bool'>



# 12.Bytes
x = b"Hello"

#display x:
print(x) # b'Hello'

#display the data type of x:
print(type(x)) # <class 'bytes'>


# 13. Byte Array
x = bytearray(5)

#display x:
print(x) # bytearray(b'\x00\x00\x00\x00\x00')

#display the data type of x:
print(type(x)) # <class 'bytearray'>


# 14.Memory View
x = memoryview(bytes(5))

#display x:
print(x) # <memory at 0x0000021520D64AC0>

#display the data type of x:
print(type(x)) # <class 'memoryview'>


# 15.None
x = None

#display x:
print(x) # None

#display the data type of x:
print(type(x)) # <class 'NoneType'>


#---------------------------------------------- Concatenation ---------------------------------------------------

line = "Hello" + "Word"
print(line) #HelloWord
print(type(line)) #<class 'str'>

# line = "Hello" + 4
print(line) # TypeError: can only concatenate str (not "int") to str


#--------------------------------------------- Convert ---------------------------------------------------------

# Convert Integer to Float 
x = 80 + 90
print(x) #170
print(type(x)) #<class 'int'>

x = float(80) + 90
print(x) #170.0
print(type(x)) # <class 'float'>

# ===============================================

# Convert String to Integer
x = "987"
print(x) # 987
print(type(x)) #<class 'str'>

x = int(x)
print(x) # 987
print(type(x)) #<class 'int'>

# ===============================================

# Convert Integer to String 
x = "Hello Word"
# x = int(x) # Erro Can't String to Integer

x = "987"
x = int(x)
print(type(x)) # Can Convert String nimber --> <class 'int'>

#--------------------------------------------- INPUT Function -------------------------------------------------

name = input("Enter Your Name :")
print("Your name is : ", name)

# Alrady Use to input funtion has a string data type
print(type(name)) # Sach as <class 'str'>