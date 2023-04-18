import sys
import math
import string

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier


cases = int(sys.stdin.readline().rstrip())#Gets the number of line

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()#Walks through each line
    data = line.split(" ")
    for  i in range(0,len(data)):
         data[i] = int(data[i])
        
    answer = round_half_up((data[0]/(data[1] - data[2]))*data[2])
    print(int(answer))
