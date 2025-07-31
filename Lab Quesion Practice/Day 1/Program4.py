#WAP to find given command line first argument is even or odd
import sys
if len(sys.argv) < 2:
    print("Not Enough parameter")
else:
    print("Even " if int(sys.argv[1]) % 2 == 0 else "odd" )
