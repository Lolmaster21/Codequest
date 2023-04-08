import sys #needed for readline and others
import math
cases = int(sys.stdin.readline().rstrip())#Gets the number of line

for caseNum in range(cases):

    yearamount = int(sys.stdin.readline().rstrip())#Gets the number of line

    for years in range(yearamount):
      year = int(sys.stdin.readline().rstrip())#Gets the number of line

      if year < 1582:
          print("No")

      elif year% 4 != 0:
          print("No")

      elif year%100 !=0:
          print("Yes")

      elif year%400 != 0:
          print("No")

      else:
          print("Yes")


