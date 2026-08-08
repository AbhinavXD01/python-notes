Pa = 1  #this is int

b = 4.4  #this is float

name = "abhinav"  #this is string

c = False  #this is boolean 

d = None  # e is a none type variable


# Variable names rules below

# 1) a variable name can contain alphabets, digits and underscores
# 2) a variable name can only start with alphabet and undercores
# 3) no while space is allowed to be used inside a variable name


# Operators in pyton
    
# 1) arithmetic: +, -, *, /, etc
# 2) assignment: =, +=, -=, etc
# 3) comparison: ==, >, >=, <, !=, etc
# 4) logical: and, or, not


# arithmetic operators
e = 7
f = 8
g = e + f
print(g)


# assignment operators
h = 5-2 # assign 5-2 in h 
print(h) 
j = 8
j += 4 # increment the value of j by 4 and then assign it to j
print(j)


# comparison operators
# ==(both sides should be same)
# !=(both sides should b different)
k = 5<4
print(k)


# logical operators

# truth table of 'or'
print("True or False is ", True or False)  # will give True
print("True or True is ", True or True)  # will give True
print("False or True is ", False or True)  # will give True
print("False or False is ", False or False)  # will give False

# truth table of 'and'
print("True and False is ", True and False)  # will give False
print("True and True is ", True and True)  # will give True
print("False and True is ", False and True)  # will give False
print("False and False is ", False and False)  # will give False

# below will just convert true to false and false to true
print(not(True))


# how to know the type? see below
l = 40
m = type(l) # class int

print(m)

# how to change the type? see below
n = "78.904"
o = float(n) # n but the type should be float
p = type(o)
# above, the type of n is str(if you will comment o), otherwise it is float
print(p)

# how to take inputs? see below
q = int(input("enter number 1: "))
r = int(input("enter number 2: "))

print("number 1 is: ", q)
print("number 2 is: ", r)
print("sum is ", q + r)
