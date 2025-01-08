inp=input("Enter a name: ")
length=len(inp)
print("The name you entered: ",inp)
print("Length of the name you entered: ",length)

# index for string starts from 0,1,2...
index_0=inp[0]
print("Index 0 letter is: ",index_0)
index_1=inp[1]
print("Index 1 letter is: ",index_1)
#To print the nth string of the input
index_n=inp[length-1]
print("Index n letter is: ",index_n)
#To print the n-1 th string of the input
index_n_1=inp[length-2]
print("Index n-1 letter is: ",index_n_1)
#To print the length of the input
print("index(length-1) of the word starts from, 0 to",length-1)
#To print the input by calling the strings
print(inp[0:length])