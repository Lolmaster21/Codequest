import sys
import math
import string

cases = int(sys.stdin.readline().rstrip()) #reads lines and strips spaces

def easter(y):
    
    a = y% 19

    b = y% 4

    c = y% 7
    
    k = ((y)//100)
    
    p = (13+(8*k))//25
    
    q = ((k)//4)
    
    m =(15- p + k -q) % 30

    n =(4+ k- q) %7
    
    d = (19*a + m) %30
    
    e =(2*b + 4*c + 6*d + n)%7
    
    f = (11*m+11)%30
    
    date =  22 + d + e

    if date <= 31:
        month = "03"

    if date  > 31:
        date -= 31
        month = "04"


    return(year,'/',month,'/',date)

   
    
for caseNum in range(cases):#runs a for loop for test cases
    year = int(sys.stdin.readline().rstrip())#Gets the number of line
    print((easter(year)))


