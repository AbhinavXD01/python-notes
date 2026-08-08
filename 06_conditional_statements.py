a = int(input("enter your age: "))

# below is our elif else ladder

if(a>=18):
    print("you are above the age of consent")
    print("good for you")  # this line is also connected to "if"

elif(a<0):
    print("you are entering an invalid negative age")

elif(a==0):
    print("you are entering 0 which is not a valid age")        

else:
    print("you are below the age of consent")    # this will be printed if everything above doesnt matches the condition
