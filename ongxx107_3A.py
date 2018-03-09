#Ren Jeik Ong
#lab section 23

import math

def integerColor(r,g,b):

    r = r/255.0
    g = g/255.0
    b = b/255.0
    
    print("Float Representation: ",format(r,'.2f'),format(g,'.2f'),format(b,'.2f'))

def floatColor(r,g,b):

    r = r*255
    g = g*255
    b = b*255
    
    if r>0:
        r = int(r+.5)
    elif r<0:
        r = int(r-.5)
    if g>0:
        g = int(g+.5)

    elif g<0:
        g = int(g-.5)
    if b >0:
        b = int(b+.5)
    elif b<0:
        b = int(b-.5)

    print("Int representation: ",r , g, b)



#Main function

components = True
while components:
    keep = input("Are input components int or float(i/f)? ")
    
    
    if keep == "i":
        r = float(input("Red component: "))
        g = float(input("Green component: "))
        b = float(input("Blue component: "))
        integerColor(r,g,b)
        components = False
    
    elif keep == "f":
        r = float(input("Red component: "))
        g = float(input("Green component: "))
        b = float(input("Blue component: "))
        floatColor(r,g,b)
        components = False

    else :
        print( "Invalid option")
        components = False


