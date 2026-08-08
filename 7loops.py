# below is our ideal example of our for loop
for i in range(1, 6):
    print(i)           # it will simply print from 1 to 5

# below is our while loop
i = 1

while(i<6):
    print(i)
    i += 1

'''
Output
1
2
3
4
5
'''    

# below is a way to write the content of a list using while loop
l = [1, 4, "Abhi", True, "Absi"]

i = 0

while(i<len(l)):
    print(l[i])
    i += 1

# below is our for loop

for i in range(4):
    print(i) # it will print 0, 1, 2, 3
# below is another example
for i in range(0, 100, 4):                     # we can also use this in string, list and tupple
    print(i) # it will print 0, 4, 8, 12, ... till 100
 

# how to iterate for loop in string, list and tupple
l = [1, 4, 6, 55, 6, 71, 33]      #list
for i in l:
    print(i) 

t = {5, 55, 12, 78}      #tupple
for i in t:
    print(i)

s = "Abhinav"      #string
for i in s:
    print(i)


# for loop with else
l = [3, 6, 22, 55]

for item in l:
    print(item)

else:
    print("done") # this is printed when loop exhausts!
    

# break in for loop
for i in range(50):
    if(i==34):
        break # exit the loop right now       
    print(i)

# continue in for loop
for i in range(50):
    if(i==34):
        continue # skip this iteration and continue
    print(i)

# pass in for loop
for i in range(645):
    pass              # this means we will work on this later(run the next loop now)
