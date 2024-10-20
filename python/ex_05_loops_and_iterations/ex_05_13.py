#program that prompts for a list of numbers as 
# above example and at the end prints out
# both the maximum and minimum of the numbers instead of average.
n=5
smallest=None
largest=None
total=0
while n>0:
    inp=input("Enter a number: ")
    n=n-1
    inp=int(inp)
    total=inp+total
    if smallest==None or largest==None:
        largest=inp
        smallest=inp
    elif inp>largest:
        largest=inp
        smallest=smallest
        print("Largest= ",largest)
        print("Smallest= ",smallest)
    elif inp<smallest:
        largest=largest
        smallest=inp
        print("Largest= ",largest)
        print("Smallest= ",smallest)
    print("Maximum= ",largest)
    print("Minimum= ",smallest)
print("Total= ",total)
print("Average= ", total/5)