#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
hrs = input("Hours Worked =")
rate = input("Rate per Hour =")
hrs = float(hrs)
rate = float(rate)
if hrs > 40: #always a colon at the end of line while using condition
    #print("Overtime")
    print ("Pay =", 40 * (rate) + (hrs-40)*(1.5*rate))
else:
    #print("Regular")
    print("Pay =",(hrs)*(rate))
