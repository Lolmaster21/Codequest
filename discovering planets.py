import sys #needed for readline and others
import math
cases = int(sys.stdin.readline().rstrip())#Gets the number of line

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()#Walks through each line
    data = line.split(" ")#creates spaces
    
    data[0] = float(data[0])
    data[3] = float(data[3])

    if data[0] > 100:
      print("The planet is too hot.")
      
    elif data[0] < 0:
          print("The planet is too cold.")
          
    else:
      if data[1]=="false":
          print("The planet has no water.")
          
      else:
          if data[2] == "false":
             print("The planet has no magnetic field.")
          else:
                if data[3] > 0.6:
                  print("The planet's orbit is not ideal.")
                else:
                    print("The planet is habitable.")
