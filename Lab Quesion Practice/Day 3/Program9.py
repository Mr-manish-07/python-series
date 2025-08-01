# find min max using variable argument list
def find_min_max(*args) :
    if not args :
        return "Not provided any number"
    min = max = args[0]
    for num in args[1:]:
        if num > max :
            max = num
        if num < min :
            min = num

    return  min , max


min , max = find_min_max(34,56,12,9000,567,76,10,456,9,2)
print("Min is " , min , "Max is " , max)


