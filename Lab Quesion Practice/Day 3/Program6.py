# find fibonacci and print it upto n

num = int(input("Enter Your Number  : "))
n = 0
m = 1
val = n+m
for i in range(2,num) :
    n = m
    m = val
    val = m+n

print(val)