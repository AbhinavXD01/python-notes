# class is like a blue print whose memory is not allocated yet~

class employee:
    language = "python"
    salary = "1200000"

abhi = employee()
abhi.name = "Abhi"
print(abhi.name, abhi.salary, abhi.language)    

rohan = employee()
rohan.name = "Rohan"
print(rohan.name, rohan.language, rohan.salary)

# here name is obj attribute and salary and language are class attributes as they directly belong to this class



# below is instance vs class

class employee:
    language = "python"
    salary = "1200000"

abhi = employee()
abhi.language = "java"   # now java will be printed at the place of python(coz its an instance attribute)
print(abhi.salary, abhi.language)    



# we can write function inside a class like below...


class employee:
    language = "python"
    salary = "1200000"

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def getInfo(self):
        print("good morning")
    

abhi = employee()
abhi.language = "java"   # now java will be printed at the place of python(coz its an instance attribute)
# print(abhi.salary, abhi.language)
employee.getInfo(abhi)   # we will write(self above to accept this). in a function inside a class. we have to do it.
# abhi.getInfo()  # this and above code will do the same work



# init method

class employee:
    language = "python"
    salary = "1200000"

    def __init__(self, name, salary, language):    # it is a dunder method which is automatically called
        self.name = name                           # when you use __init__(you dont need self or @staticmethod to call it)
        self.salary = salary
        self.language = language 
        print("i am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod          # it is used to avoid using self
    def getInfo():
        print("good morning")
    

abhi = employee("singh", "Bcom")
abhi.name = "abhi"  
print(abhi.salary, abhi.name, abhi.language)

# rohan = employee()
   