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