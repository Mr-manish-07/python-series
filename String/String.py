#Anything is written inside double quotes ( " ") will be considered as String
#But here we can use single quotes as well (' ') will be work as same as upper line
#We can use double quotes between of statement when we use starting and ending as double quotes
#In this condition we need to use single quotes or scape sequence (line 8 )
#Using Triple quotes help us to write multiple line String value
#We can use Indexing in String but when it comes to java , it doesn't allow to do it
#This is just like javascript is also allows to access String value using indexes.
#If we try to access index out of value ex: if we have 5 character there and try to access
#       6 index or even 5 index it will throw index error


name = "Manish"
fullName = 'Manish Kumar '
about = "This is Manish kumar from \"Ranchi\" jharkhand "
print(name,"," ,fullName,",",about)
fullDetails  = ''' This is good to 
    go because we are using 
    triple quotes
'''
print(name[0])

# print(name[6])    #IndexError: string index out of range
