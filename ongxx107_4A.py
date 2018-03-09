#Ren Jeik Ong HW4A

import turtle

def drawTriangle(edgeLength):

    turtle.showturtle()
    turtle.left(30)
    turtle.forward(edgeLength)
    turtle.right(120)
    turtle.forward(edgeLength)
    turtle.right(120)
    turtle.forward(edgeLength)
    turtle.left(30)
    
    

def drawStemAndTriangle(stemLength, edgeLength):
    
    turtle.forward(stemLength)
    drawTriangle(edgeLength)
    turtle.forward(stemLength)
    turtle.rt(180)
    
    
    
numStem = int(input("Input number of stems and triangles: "))
longStemLength = int(input(" Input long-stem length: "))
edgeLength = longStemLength/5
shortStem = longStemLength/2
stemCount = 0

while stemCount< numStem-1:
    turtle.speed(0)
    drawStemAndTriangle(longStemLength,edgeLength)
    turtle.left(360/numStem)
    drawStemAndTriangle(shortStem,edgeLength)
    turtle.left(360/numStem)
    stemCount += 2
    
    
if(numStem % 2 == 1):
    drawStemAndTriangle(shortStem, edgeLength)
turtle.exitonclick()
