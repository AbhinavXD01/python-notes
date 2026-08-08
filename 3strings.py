# below, all are strings
"abhinav"
'abhinav'
'''abhinav'''

# string is immutable(cant be changed)
# slicing of abhinav is like below
# 0,1,2,3,4,5,6 or -7,-6,-5,-4,-3,-2,-1

name = "abhinav"

nameshort = name[0:3] # from 0 to 3(excluding 3)
print(nameshort)

character1 = name[1]
print(character1)

# below both will give the same response(so its a best way to solve negative too){not sure about this technique}
print(name[-4:-1])
print(name[1:4])

# extra slicing
print(name[:4]) # this means [0:4]
print(name[1:]) # this means [1: full length] or [1:7] here

# string functions
print(len(name))
print(name.endswith("nav"))
print(name.startswith("ab"))
print(name.capitalize())

# escape sequence characters
a = "tesla was genius\nmysterious"
print(a)

b = "tesla was genius\nmysterious \"person\""
print(b) 
# above is used to add double quotes