import sys

cases = int(sys.stdin.readline().rstrip()) 

for num_cases in range(cases):
    datastring = sys.stdin.readline()
    data = datastring.split(" ")

    x = int(data[0])
    y = int(data[1])
    xdata = []
    ydata = []
    for i in range(x):
        xdata.append(sys.stdin.readline())
    for j in range(y):
        ydata.append(sys.stdin.readline())
    
    for i in range(x):
            if xdata[i] == ydata[j]:
                xdata[i] == 0                
            else:
                print(xdata[i])

 
