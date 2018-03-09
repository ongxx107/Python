#Ren Jeik Ong labSection23 hw5a

import math
import random

data = int(input("How many data? "))
value =str(input("Input data values: "))

value = value.split(" ")
if(len(value) == 1):
    print("Empty List, no data points entered")
else:
    for i in range(0,len(value)):
        value[i] =float(value[i])

    average = sum(value)/len(value)
    print ("Average: ",average)

    dataVals =value
    originalAverage = average
    def new_average(dataVals,difference,originalAverage):
        sumAll = 0
        LengthList = 0
        for i in dataVals: 
            if not((i > originalAverage + difference) or (i < originalAverage - difference)):
               sumAll += i 
               LengthList += 1
        return format(sumAll/LengthList, ".2f")
       


    Continue = True
    while(Continue):
        outlier=[]
        difference = float(input("Input difference: "))
        plus = average+difference
        minus = average-difference
        for x in range(0,len(value)):
            if value[x] > plus:
                outlier.append(value[x])
            elif value[x] < minus:
                outlier.append(value[x])
            
        print("Outliers: ",end='')
        for x in outlier:
            print(x,end=' ')
        print("\nAverage excluding outliers: ",new_average(dataVals,difference,originalAverage))

        difContinue=(input("Do you wish to input another difference (y/n)? "))
        if difContinue == "y":
            continue
        elif difContinue != "y":
            valContinue=input("Do you wish to input another data set(y/n)? ")
            if valContinue != "y":
                Continue = False
            else:
                data = int(input("How many data? "))
                value =str(input("Input data values: "))
                value = value.split(" ")
                for i in range(0,len(value)):
                    value[i] =float(value[i])
                average = sum(value)/len(value)
                print ("Average: ",average)
                dataVals =value
                originalAverage = average
            
                    
        

            

            
        
            
    

    

    


        
    

        



