# 
# Example file for variables
#

# Declare a variable and initialize it
f=0
#print(f)


# re-declaring the variable works
#f="sdfghj"
#print(f)

# ERROR: variables of different types cannot be combined
#print("string" + str(21345))


# Global vs. local variables in functions

def someFuntion():
    global f
    f="def"
    print(f)

someFuntion()
print(f)

del f
print(f)