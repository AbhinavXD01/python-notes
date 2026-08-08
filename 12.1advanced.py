# walrus operator(it allows you to assign values to variables as part of an expression)
# in short, it makes work easy and fast

if (n := len([1, 2, 3, 4, 5])) > 3:
    print("list is too long ({n} elements, expected <= 3)")




# type definitions(it makes work of coders easy by letting them know about the type)

n : int = 5   # we can tell type also(int here)

name : str = "abhi"   # string here

def sum(a: int, b:int)  ->  int:     # it is a way to how to do it in a function
    return a+b




# typing import    

from typing import list, union, tuple, dict
# example below

person: tuple[str, int] = ("alice", 30)

scores: dict[str, int] = {"alice": 90, "bob": 85} 




# match statement

def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404: 
            return "not found"
        case 500:
            return "internal server error"
        case 403:
            return "unknown status"
        
# usage
print(http_status(200))  # output: ok        
print(http_status(404))  # output: not found        
print(http_status(500))  # output: internal server error        
print(http_status(403))  # output: unknown status        





# exception           (it will come here when program doesnt work)

try: 
    a = int(input("hey, enter a number: "))
    print(a)

except ValueError as v:   # it will be used when user is writing that particular thing(for a particular error)
    print("heyyy")
    print(v)

except Exception as e:    # we use this so that it doesnt crash when user write something unexpected(and show him response), 
    print(e)              # example - if he is writing string(but we give int), then it will work.

print("thank you") 





# raising exceptions

a = int(input("enter a number: "))
b = int(input("enter second number: "))

if(b == 0):           # because of this user wont go further(if he will use 0)
    raise ZeroDivisionError("our program is not meant to divide numbers by zero")
else:
    print(f"the division a/b is {a/b}") 






# try else

try:        # if try will run successfully, then it will go inside else
    a = int(input("hey, enter a number: "))
    print(a)

except ValueError as v:
    print("heyyy")
    print(v)

except Exception as e:
    print(e)

else: 
    print("i am inside else")





# finally   # in function, code doesnt run after return, buy finally will run even after that.(main reason)

def main():         # in function, we have to write return to get the answer, but it doesnt matter for finally(not sure about reason)
    try:
        a = int(input("hey, enter a number: "))    
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("i am inside of finally")

main()





# main.py

# from 12.1badvanced import myFunc

# if __name__ == "__main__":
    # if this code is directly executed by running the file its present in
    # print("we are directly running this code")





# global        # global keyword changes the global variables(89 will be converted to 3)

a = 89

def fun():
    global a
    a = 3
    print(a)

fun()
print(a) 






# enumerate

l = [4, 54, 333, 25, 90]

# index = 0
# for item in l:
#     print(f"the item number at index {index} is {item}")
#     index += 1

# this can be simplified using enumerate function

for index, item in enumerate(l):
    print(f"the item number at index {index} is {item}")






# list comprehension

mylist = [1, 4, 5, 9, 2]

squaredlist = []
for item in mylist:
    squaredlist.append(item*item)

print(squaredlist) 