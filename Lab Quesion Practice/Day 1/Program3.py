#WAP for taking command line argument and add it
import sys
if len(sys.argv) < 3:
    print("Not sufficient argument given")
else:
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    print(n1+n2)