# Input section                                                                 
hrs = input('Please enter hours worked: ')                                      
rate = input('Please enter rate of pay: ')                                      
fhrs = float(hrs)                                                               
frate = float(rate)                                                             
                                                                                
# Is it Overtime yes or no and then print out results                           
if fhrs <= 40:                                                                  
    pay = fhrs * frate                                                          
    print(pay)                                                                  
if fhrs > 40:                                                                   
    payr = fhrs * frate                                                         
    payOvertime = (fhrs-40) * (frate * 0.5)                                            
    pay = payr + payOvertime                                                          
    print(pay)