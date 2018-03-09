# Ren Jeik Ong HW4B

import random

def savingsChange(savings, increase, withdraw):
     return savings * (1.0 + increase) - withdraw
savings = float(input("Input original savings: "))
increasemin = float(input("Input yearly increase minimum: "))
increasemax = float(input("Input yearly increase maximum: "))
withdrawmin = float(input("Input yearly withdraw minimum: "))
withdrawmax = float(input("Input yearly withdraw maximum:400 "))
years = int(input("Input number of years: "))
trials = int(input("Input number of trials: "))

yearCount = 1

successCount=0

for x in range(0,trials):
     new_savings = savings
     while (yearCount <= years and new_savings >= 0.0):
          i =random.uniform(increasemin, increasemax)
          w =random.uniform(withdrawmin,withdrawmax)
          new_savings = savingsChange(new_savings, i, w)
          yearCount = yearCount + 1
          
     yearCount =1
     if(new_savings > 0.0):
          successCount += 1
successCount = format((successCount/trials)*100, '.2f')
print("Success Percentage: " + str(successCount) + " %")

