#Strings are immutable which means you can’t change an existing string.
inp=input("Enter your name: ")
name="Mr."+inp
print(name)
firstname=name[3:]
print("First name is: ",firstname)