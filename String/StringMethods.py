#String are immutable in python we when we try to change value it creates a new String object
# len(strVal) finds length
# strVal.upper turns into upper case
# strVal.lower turns into lower case
# str.rstrip("char") it removes if char is present in str at the end
# str.split("char") it split and convert it into List by given char if found
# str.capitalize("Converts first string value into capital letter)
# str.count("val") find how many times value is there in str
# str.find("val") return the index of first occurrence of val else -1
# str.index("val") return index else error
str = "this is a string !!!!!!"
print(len(str))
print(str.upper())
print(str.lower())
print(str.strip("!"))
print(str.replace("this","It"))
print(str.split(" "))
print(str.capitalize())
print(str.count("i"))