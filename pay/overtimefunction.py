# Fuctions Section

# Is it Overtime yes or no and then print out results
def computepay (hours, rate):
    if fhrs <= 40:                                                                  
        pay = fhrs * frate
        return pay        
    if fhrs > 40:                                                                   
         payr = fhrs * frate                                                         
         payo = (fhrs-40) * (frate * 0.5)                                            
         pay = payr + payo
         return pay

# Input section                                                                 
hrs = input('Please enter hours worked: ')                                      
rate1 = input('Please enter rate of pay: ')                                      
fhrs = float(hrs)                                                               
frate = float(rate1)
pr_pay = computepay(fhrs,frate)

# Output Section
print("Pay", pr_pay)