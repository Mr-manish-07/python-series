# find fibonacci and print it upto n using recursion

def fibo (n) :
    if n==0 or n==1  :
        return n
    return fibo(n-1) + fibo(n-2)

num = int (input("Enter any number : "))
print(fibo(num))
