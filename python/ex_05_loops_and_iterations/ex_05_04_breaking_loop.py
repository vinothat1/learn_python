#breaking out of a loop
#break statement ends the current loop and jumps to the statement immediately following the loop
while True:#Condition
    line=input("> ")
    if line=="done":#if condition
        break#break exits the loop
    print("the loop continues as the input is  not done and is",line)
print("The loop is finished as the input is done!")
