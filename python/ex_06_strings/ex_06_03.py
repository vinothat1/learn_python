#Write a while loop that starts at the last character in the string and
#works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.
inp=input("Enter a Name: ")
length=len(inp)
print("Length of the name is: ", length)
index=length-1
while index>=0:
    print(inp[index])
    index=index-1
print("Now using char and for loop")
for char in inp:
    print(char)