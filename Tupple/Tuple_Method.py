tup = (23,34,45,66,"Manish","Ranjeet",True,34,67)
l = list(tup)
l.append(False)
print(tup.count(34))

val = tup.index(34,0, len(tup))
print("In which index 34 is present",val)

print(tup)
print(l)