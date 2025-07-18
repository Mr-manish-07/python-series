#len(<str val> ) is used to find the length of the string
#we can access string index from anywhere to any by strVal[2:6],we are accessing 2 to 5 , 6 excluded
#Negative indexing works like when we do access StrVal[0:-3] it works as len(StrVal) - 3 ;


a= "This is a string value"
print(len(a))
print(a[0:len(a)])
print(a[-1:7])
print(a[:-5]) #Automatic insert 0 there