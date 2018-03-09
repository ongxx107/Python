#Ren Jeik Ong labSection23 hw5b


Continue= True

while(Continue):
    string = input("Input the string to search: ")
    substring = input("Input pattern string: ")
    firstCase = False
    i = 0
    while i <= len(string)-len(substring):
        num = 0
        minMatch=len(substring)-1
        for j in range (0,len(substring)):
            if string[i+j]==substring[j]:
                num +=1
                if(i + j == 1):
                    firstCase = True

        
        
        if num == minMatch and firstCase:
            print("Starting at position",format(i+1,"3d"), ": one-character match with",format(string[(i):(i+len(substring))]))
        elif num == minMatch:
            print("Starting at position",format(i,"3d"), ": one-character match with",format(string[(i):(i+len(substring))]))
           
        i += 1
    choice = input("Do you wish to check another pair of strings (y/n)? " )
    if choice !="y":
        Continue = False

