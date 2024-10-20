#Encapsulate this code in a function named count,
#and generalize it so that it accepts the string and the letter as arguments.
def count():
    count=0
    for letter in word:
        if letter==find:
            count=count+1
    print(count)
word=input("Enter a name: ")
find=input("Enter the letter to count: ")
count()
