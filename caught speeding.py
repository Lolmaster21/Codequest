import sys


cases = int(sys.stdin.readline().rstrip()) #reads lines and strips spaces

for caseNum in range(cases):#runs a for loop for test cases
        line = sys.stdin.readline().rstrip()
        data = line.split(" ")#creates spaces 
       # for i in range (len(data)):
        #    data[i] = int(data[i])
        data[0] = int(data[0])
        
        if data[1]=="true":
            if data[0] <=65:
                print("no ticket")
            elif data[0] <= 85:
                print("small ticket")
            else:
                print("big ticket")
                
        else:
            if data[0] <=60:
                print("no ticket")
            elif data[0] <= 80:
                print("small ticket")
            else:
                print("big ticket")
        
        



