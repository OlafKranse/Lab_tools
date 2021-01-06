#creates random block design based on conditions for a given n

import random

### notes ###
"""
condition meaning:
B = water
Z = zinc chloride + worms
N = zinc chloride
"""
### setup ###
conditions = "B","Z","N"
n = 1500 #How many individual samples to do (eg. n=1500 with 3 conditions will result in random block design of 500 of each condition)
outputfile = "random_block_design.txt"

### main script ###
number_of_con = len(conditions)
how_many_combs = n/len(conditions)

with open(outputfile,"a+") as out:
    for things in range(0,int(how_many_combs)):
        randomNames = random.sample(conditions, random.randint(number_of_con,number_of_con))
        out.write(str(randomNames))
        out.write("\t\t")

