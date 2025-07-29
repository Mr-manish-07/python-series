from unittest import skipIf

list_ele = [3, 4, 5, 3, 6, 4, 35, "Manish", "Raja", True]
stringVal = "Manish"
if "a" in stringVal :
    print("a is present in str")
elif 3 in list_ele :
    print("3 is present in list")
else:
    print("Nothing is both is present")
print(list_ele)
print(list_ele[:])
print(list_ele[1:-1])

#can take three argument starting , ending , jumping by

print(list_ele[1:-1: 2])

print(["raj","manish",True,45]) #we can create list inside

#We can use loop inside list to create it and even we can use condition
lst = [i for i in range(5000)  if i % 100 == 0]
print(lst)