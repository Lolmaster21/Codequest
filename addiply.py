#codequest addiply problem
#you get 1 number telling you how many rows you're going to get
#youre going to get x number of rows of two problems
#Then you need to output the numbers added and the numbers multiploed
import sys

num = int(input())
for i in range(num):
    line = sys.stdin.readline().rstrip()
    num1, num2 = (int(val) for val in line.split(" "))
    
    print(num1+num2, end = " ")
    print(num1*num2)

