import sys
if(len(sys.argv) < 4) :
    print("InSufficient Value Provides ")
else:
    y = sys.argv[2]
    x = sys.argv[1]
    z = sys.argv[3]
    print(max(x,y,z))