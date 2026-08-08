# dictionaries are unordered, mutable(can be changed), indexed, cant contain duplicate keys

marks = {
    "abhi": 90,
    "rahul": 62,
    "samay": 28
}

# print(marks, type(marks))
print(marks["abhi"])

print(marks.items()) # it gives us a list of key value pairs in the form of tupples
# if you will use keys at the place of items, then you will get the keys like, "abhi", "absi",....
# if you will write values at the place of items, then you will get values like 100, 62,......   

marks.update({"abhi": 92, "rahul": 88}) # this will update
print(marks)

print(marks.get("abhi")) # this will give you marks
print(marks.get("abhi2")) # this will give none
print(marks["abhi2"]) # this will give error

d = {} # this is an empty dictionary

# Sets

e = set() # dont use s = {} as it will create an empty dictionary

s = {1, 5, 32, 54, 5, 5, 9, "abhi"} # elements wont repeat

# print(s, type(s)) 

s.add(566) # to add in the set
print(s, type(s))
s.remove(1) # to remove
print(s, type(s))

# set_union_intersection
s1 = {1, 45, 6}
s2 = {7, 8, 1, 78}

print(s1.union(s2)) # will give {1, 45, 6, 7, 8, 78}
print(s1.intersection(s2)) # will give {1}
