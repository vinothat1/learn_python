#Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

def computepay(hrs,rate):#computepay is a function defined initially
    if hrs > 40:
        earned=( 40 * (rate) + (hrs-40)*(1.5*rate))
    else:
        earned=((hrs)*(rate))
    return(earned)#returns the output from the function after the conditions

hrs = input("Hours Worked =")
hrs = int(hrs)
rate = input("Rate per Hour =")
rate = int(rate)

pay=computepay(hrs,rate)#calling a function

print("earned is ",pay)#print the output]
