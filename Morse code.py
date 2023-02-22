import sys
import string

morse = {
    'A' : ". -",
    'B' : "- . . .",
    'C' : "- . - .",
    'D' : "- . .",
    'E' : ".",
    'F' : ". . - .",
    'G' : "- - .",
    'H' : ". . . .",
    'I' : ". .",
    'J' : ". - - -",
    'K' : "- . -",
    'L' : ". - . .",
    'M' : "- -",
    'N' : "- .",
    'O' : "- - -",
    'P' : ". - - .",
    'Q' : "- - . -",
    'R' : ". - .",
    'S' : ". . .",
    'T' : "-",
    'U' : ". . -",
    'V' : ". . . -",
    'W' : ". - -",
    'X' : "- . . -",
    'Y' : "- . - -",
    'Z' : "- - . .",
    ' ' : " "
    }

thing = []
cases = int(input())
for i in range(cases):
    phrase = input()
for i in range(len(phrase)):
        thing.append(morse[phrase[i]])
for i in range(len(thing)):
    print(thing[i], end = '')


