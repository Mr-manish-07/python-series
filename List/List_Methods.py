l = [67,25,23,55,6,33,122,25]
print(l)
l.append(34) # Added element to the last
l.sort()     # Sort Elements in ascending order
l.reverse()
print("first occurance " ,l.index(25)) # return index of last
print(l.count(25))
m=l  # m and l point to same memory location
n = l.copy() # n and l is not pointing to same memory location
l.insert(1,20000)
p = [3,4,3]
q = [22,22,33]
l.extend(p) # pic all element of p and insert at end of l
k = p+q
print(k)
print(l)