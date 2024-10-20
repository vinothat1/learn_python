#Write a program which repeatedly reads integers until the user entersv“done”.
#Once “done” is entered, print out the total, count, and average of the integers.
#If the user enters anything other than a integers, detect their mistake using
#try and except and print an error message and skip to the next integers.
count=0
total=0
while True:
    inp=input("Enter a number: ")
    if inp==("done"):
        print("done, End of program")
        print(count,total,total/count)
        break
    try:
        inp == int(inp)
        
    except:
        print("Enter valid input")
        continue
    count=1+count
    total=int(inp)+total
print("End of the program")