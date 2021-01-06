#grep radom lines from list for given n

import random

n = 22 #how many do you want to randomly pick
inputfile = "in.txt"
outputfile = "out.csv"



with open(inputfile, "r") as f:
    splitLines = f.readlines()
    randomNames = random.sample(splitLines, random.randint(n,n))
    for lines in randomNames:
        with open(outputfile, "a+") as out:
            out.write(lines)
