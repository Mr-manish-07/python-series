from unittest import skipIf

list = [3,4,5,3,6,4,35,"Manish","Raja",True]
str = "Manish"
if "a" in str :
    print("a is present in str")
elif 3 in list :
    print("3 is present in list")
else:
    print("Nothing is both is present")
print(list)
print(list[:])
print(list[1:-1])

#can take three argument starting , ending , jumping by

print(list[1:-1: 2])

print(["RAjeet","Manis",True,45]) #we can create list inside

#We can use loop inside list to create it and even we can use condition 
lst = [i for i in range(5000)  if i % 100 == 0]
print(lst)