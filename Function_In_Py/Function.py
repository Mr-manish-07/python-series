def sumOfTwo(a,b) :
    print(int(a)+int(b))

sumOfTwo(4343,565)

#If I want to define function later as same as abstract method of java so we need to use pass keyword
def fun1 (a,b) :
    pass

newInput = bool(input("Enter True or False : "))
if not newInput:
    print("True given")
else:
    print("False given")


# We can pass default value in argument if use don't give take this and operate
def average(a = 5, b =4):
    avg = (a+b)/2
    print(avg)

average(4,8)
average(4)  #giver value of a
average(b=43)  #given value of b
average(b=43 , a =354) # changing values parameter