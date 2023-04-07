import sys


cases = int(sys.stdin.readline().rstrip()) #reads lines and strips spaces

for caseNum in range(cases):#runs a for loop for test cases
        line = sys.stdin.readline().rstrip()
        data = line.split(" ")#creates spaces 
        for i in range (len(data)):
            data[i] = int(data[i])
        
        
        #while n3 is bigger than 0, keep subtracting 5 n2 number of times and stay above 0
        #then check if what's left over is less than or EQUAL n2
        
        
        sub = data[2] - data[1]*5
        if data[2] == 0:
            print("true")
        else:
            if (data[1]*5) > data[2]:
                if data[0]< data[2]:
                    print("false")
            else:
                    
                if sub > data[0]:
                    print("false")
                        
                else:
                    print("true")


