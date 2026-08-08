# functions are used to avoid writing repeatable code

def avg():
    a = int(input("enter your number: "))
    b = int(input("enter your number: "))
    c = int(input("enter your number: "))

    average = (a + b + c)/3
    print(average)

avg()  # this is called function call(we are calling our function here)
print("Thank you!")
avg() 


def goodDay():
    print("Good Day")

goodDay()


def goodDay(name):
    print("Good Day" + name)

goodDay("Abhi")
goodDay("Absi")
goodDay("Abhisi")


def goodDay(name, ending):
    print("Good Day" + name)
    print(ending)

goodDay("Abhi", "Thank you")
goodDay("Absi", "Thanks")


def goodDay(name, ending):
    print("Good Day" + name)
    print(ending)
    return "done"

a = goodDay("Abhi", "Thank you")
print(a)


def great(name):
    gr = "hello" + name
    return gr

a = great("abhi")
# a will now contain "hello abhi"


# below, it is taking thanks coz we write(by default its thank you)
def goodDay(name, ending="Thank you"):
    print(f"Good Day + {name}")
    print(ending)

goodDay("Abhi", "Thanks")
goodDay("Absi")


# recursions(this is factorial actually, you know it right?)
# factorial(0) = 1
# factorial(1) = 1
# factorial(2) = 2 X 1
# factorial(3) = 3 X 2 X 1
# factorial(4) = 4 X 3 X 2 X 1

# factorial(n) = n * factorial(n-1)

def factorial(n):
    if(n==1 or n==0):
        return 1 
    return n * factorial(n-1)

n = int(input("enter a number: "))
print(f"the factorial of this number is: {factorial(n)}")
