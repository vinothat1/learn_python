#If you want to finish the current iteration and immediately jump to the next iteration, we use CONTINUE statement
while True:
    line=input(">")
    if line[0]=="#":#if the input is #followed by any characters, the loop will stop and go back to while.
        continue
    if line=="done":
        break
    print(line)
print("Done")
