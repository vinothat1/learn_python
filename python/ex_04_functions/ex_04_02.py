#Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.
def computegrade(inp):

    if 1>=inp >=0.9:
        print("A")
    elif .9>inp >=.8:
        print("B")
    elif .8>inp>=.7:
        print("C")
    elif .7>inp>=.6:
        print("D")
    elif 0<inp<.6:
        print("F")
    else:
        print("Wrong input")

inp=input("Enter a Score :")
print(type(inp))
inp=float(inp)
print(type(inp))

cmp=computegrade(inp)
