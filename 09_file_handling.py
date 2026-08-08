# below method is used to read a file
f = open("09_file_handling_example1.txt") # you can also write f = open("09_file_handling_example1.txt", "r")
data = f.read()
print(data)
f.close()



# below method is used to create a file
st = "hey everyone!"

f = open("09_file_handling_example2.txt", "w")
f.write(st)
f.close()



f = open("09_file_handling_example3.txt")

# lines = f.readlines()    # readlines returns the list of lines
# print(lines, type(lines))
# f.close()


# below is another way(to write individual lines) 

line1 = f.readline()    # readlines returns the list of lines
print(line1, type(line1))
f.close()

line2 = f.readline()    # readlines returns the list of lines
print(line2, type(line2))
f.close()

line3 = f.readline()    # readlines returns the list of lines
print(line3, type(line3))
f.close()

# below will show nothing
line4 = f.readline()    # readlines returns the list of lines
print(line4, type(line4))
f.close()

# how to print lines using while loop
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()


f = open("09_file_handling_example3.txt")
print(f.read())
f.close()

# The above part can be written using with statement like this:
with open("09_file_handling_example3.txt") as f:
    print(f.read())

# you dont have to explicitely close the file above    
