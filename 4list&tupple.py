# lists are containers to store a set of values of any datatype. example below

# lists are mutable(can be changed), so we can change them like below

friends = ["apple", 8, 76.34, False] # since its mutable, you can also add in between, like "grapes" after "apple"

print(friends[0])
friends[0] = "mango"
print(friends[0]) # this will show mango(at 0 index) from now

# list methods

friends.append("absi")
print(friends) # now "absi" will be added in the end(in the same list, which is not possible in string)

l1 = [5, 4, 33, 21, 6, 18, 9]
l1.sort() # sort will convert it into ascending order
# print(l1)
# if we will write reverse at the place of sort, this list(l1) will be reversed
# l1.insert(3, 3333) # we are telling to insert 3333 at the place of 3

print(l1.pop(3)) # 21 will be printed
l1.pop(3) # 21 will be removed
# you can see the difference above(one is giving that particular value, another is printing after removing it)
print(l1)

# value = l1.pop(3)
# print(value)
# print(l1)
# above part is similar to print(l1.pop(3))

# tupple is immutable(cant be changed)
a = (1, 45, True, 67, 45, "Abhinav") # this cant be changed, coz its a tupple
print(a)

no = a.count(45) # will give us the number of times a particular number has appeared
print(no)

i = a.index(67) # will give you the position(first index from the start not the second one like second 45 above)
print(i)

print(len(a)) # it will give you the length, (6 above)
