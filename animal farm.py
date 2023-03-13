import sys
import math
import string

cases = int(sys.stdin.readline().rstrip()) 

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    data = line.split(" ")#creates spaces 
    for i in range (len(data)):
        data[i] = int(data[i])
    #print(data)
    num = data[0]*2 + data[1]*4 + data[2]*4
    print(num)
