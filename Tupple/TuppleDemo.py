tup = (3,42,55,"Manish")
print(id(tup))
print(type(tup),tup)

tup1 = (3)
print(type(tup1)) # for 1 element python consider as int so we need to use ,
tup2 = (4,)
print(type(tup2))

#tup[0] = 3 # we cant change the value of tuple since it is immutable so it can't be changed
print(tup[0], " " , tup[1] , " " , tup[2] )

tup3 = tup[0:4] #creating a new tuple with three element of tup
print(tup3)