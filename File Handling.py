# 1.Open the file
# 2.Read/ Write
# 3.Close the file

# Open the file
       # File object = open(filename, mode)

fhand = open("C:Desktop/Phython/first.txt")
print(fhand) # <_io.TextIOWrapper name='C:/Users/kanis/OneDrive/Desktop/Phython/first.txt' mode='r' encoding='cp1252'>

print("Name of the file :" , fhand.name) # Name of the file : C:/Desktop/Phython/first.txt


# Read File
count = 0
for line in fhand:
    print(line.rstrip()) 
    count += 1
# Hello World
# Testing....

# Num of count
print("Line Count ",count) # 2
fhand.close() # Close the file
# ----------------------------------------------------------------------------------

#2.Read File
print(fhand.read())
fhand.close()
