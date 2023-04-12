import sys

case =  int(sys.stdin.readline().rstrip()) #Reads line
def fact(num): 
    if num> 1:
        return num*fact(num-1) #number input * Num-1
    else:
        return num
    
for num_cases in range(case):
    num = int(sys.stdin.readline().rstrip())
    print(fact(num))
