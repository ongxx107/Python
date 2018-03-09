#Ren Jeik ong
#lab section 23

import math



def savingChange(savings,increase,withdraw):
    return (savings*(1.0+increase)-withdraw)



#MainFunction

yearcount = 1
savings = float(input("Input original savings: "))
increase = float(input("Input yearly increase: "))
withdraw = float(input("Input yearly withdraw: "))
years =int (input("Input number of years: "))

while (savings >= 0) and (yearcount <= years):
    savings = savingChange(savings,increase,withdraw)
    if savings >0:
        print("Year: ",yearcount , "Amount: $   ",format(savings,'10.2f'))
        yearcount +=1
    else:
        print("Savings depleted during year", yearcount)

savingChange(savings,increase,withdraw)



