# Inheritance

class employee: 
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# class programmar:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showlanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")    


class programmar(employee):    # this is inherited class
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")        

a = employee()
b = programmar()

print(a.company, b.company)




# Multiple Inheritance

class employee: 
    company = "ITC"
    name = "default name"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.company}")

class coder:
    language = "python"
    def printlanguage(self):
        print("out of all the languages, here is yours: {self.language}")    


class programmar(employee, coder):    # this is inherited class
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")        

a = employee()
b = programmar()

b.show()
b.printlanguage()
b.showlanguage() 




# Multilevel Inheritance

class employee:
    a = 1

class programmar(employee):
    b = 2

class manager(programmar):
    c = 3

o = employee()
print(o.a)    # prints the a attribute        
print(o.b)    # shows an error as there is no b attribute in employee class

o = programmar()
print(o.a, o.b)

o = manager()
print(o.a, o.b, o.c)





# super (it is used to call methods and access functionality from a parent class inside a child class)

class employee:
    def __init__(self):
        print("constructor of employee")
    a = 1

class programmar(employee):
    def __init__(self):
        print("constructor of programmar")
    b = 2

class manager(programmar):
    def __init__(self):
        # super().__init__()                  // if you will uncomment then, programmar will also run
        print("constructor of manager")
    c = 3

# o = employee()
# print(o.a)    # prints the a attribute  

# o = programmar()
# print(o.a, o.b)

# o = manager()
# print(o.a, o.b, o.c)





# class methods

class employee:
    a = 1
    @classmethod 
    def show(cls):
        print(f"the class attribute of a is {cls.a}")      # to see the class attributes(1 here), not instance attributes(45 here)

e = employee()
e.a = 45

e.show





# property decorators 

class employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"the class attribute of a is {cls.a}")

    @property                 # (@property makes a method behave like a variable when you access it.)
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name (self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]  
  

e = employee()
e.a = 45

e.name = "abhi singh"
print(e.fname, e.lname) 

e.show()





# operator overload (here, Operator overloading using methods like __add__ lets a class define how operators (here +) behave for its objects)

class number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):     # you can use others too, like __sub__ for subtraction
        return self.n + num    

n = number(1)
m = number(2)

print(n + m)