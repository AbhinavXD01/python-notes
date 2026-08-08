# lambda function

def square(n):
    return n*n

print(square(5))

# below using lambda function

square = lambda x: x*x

print(square(5)) 

# another example below

square = lambda x:x*x
square(6)  # returns 36
sum = lambda a, b, c : a + b + c
sum(1, 2, 3) # returns 6






# join method

a = ["abhi", "absi", "abhisi"]

final = "::".join(a)     # you can also use other things like -, : at the place of :: (to join them)
print(final) 

# above output will be abhi::absi::abhisi







# map, filter, reduce



# map          # it applies a function to all the items in an input list.(so it will be applied to every element on this list)
l = [1, 2, 3, 4, 5] 

square = lambda x: x*x

sqlist = map(square, l)
print(list(sqlist))



# filter           # it just filters(as its name suggest)
l = [1, 2, 3, 4, 5] 

def even(n):
    if (n%2 == 0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))



# reduce 1                  # it will work in the sequence(like 1+2 then 3+3 then 6+4 then 10+5)
l = [1, 2, 3, 4, 5]         # for multiply, it will be like(1*2 then 2*3 then 6*4 then 24*5)

from functools import reduce
def sum(a, b):
    return a + b

print(reduce(sum, l))

# below example is just slightly different.

# reduce 2
l = [1, 2, 3, 4, 5] 

from functools import reduce
def sum(a, b):
    return a + b     # addition is happening here

mul = lambda x,y:x*y       # multiplication is happening here

print(reduce(sum, l))
print(reduce(mul, l))  
