#Rewrite your pay program using try and except
hrs = input("Hours Worked =")
try:#try to execute within try condition if error occurs it goes to except condition
    hrs = int(hrs)
    rate = input("Rate per Hour =")
    rate = int(rate)
    if hrs > 40:
        print ("Pay =", 40 * (rate) + (hrs-40)*(1.5*rate))
    else:
        print("Pay =",(hrs)*(rate))
except:# execute only when there is an error or unsatisfied condition in try condition
    print("Error, please enter numeric input")
