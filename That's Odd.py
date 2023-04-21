import sys #needed for readline and others
cases = int(sys.stdin.readline().rstrip())#Gets the number of line


for caseNum in range(cases):
    num = int(sys.stdin.readline().rstrip())#Walks through each line
    
    if num %2 == 0 :
        print("EVEN")
    else:
        print("ODD")
    
