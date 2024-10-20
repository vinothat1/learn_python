 #Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:

try:
    inp=input("Enter a Score :")
    print(type(inp))
    inp=float(inp)
    print(type(inp))
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
except:
    print("ERROR MESSAGE")
