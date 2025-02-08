# trry:
#   code we wont to run

# except:
#   code which run if an error occured

try :
    print(x)
except :
    print("And exception occures!") # SyntaxError: invalid syntax

#------------------------------------------------------------------------------

try :
    print(x)
except NameError:
    print("Variable X is not defined") # SyntaxError: invalid syntax

except:
    print("Something went wrong")

#------------------------------------------------------------------------------