word=input("Enter a name: ")
find=input("Enter the letter to count: ")
count=0
for letter in word:
    if letter==find:
        count=count+1
print("There are ",count,"(",find,")s in ",word)