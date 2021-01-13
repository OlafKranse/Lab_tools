#this script blasts sequences in file "in" to a given database and outputs no hits in "no_hits"

### inport ###
from Bio.Blast import NCBIWWW
import subprocess
import os
import time
from os import listdir
from os.path import isfile, join
import re

### setup ###
blast_type = "blastn"
database = r"arabidopsis_genome/TAIR10_seq_20101214_updated"
os.chdir(r"G:\My Drive\labbook\python scripts\synthetic promotors")

### main script ###
i = 0
### make blast db into one line ###
"""
print("i")
with open(database, "r") as ff:
    with open("temp", "w") as f:
        for lines in ff:
            if ">" in lines:
                pass
            else:
                f.write(lines)

print("i")

### search for existance of a string in that line ###
with open("temp", "r") as f:
    with open("db", "w") as ff:
        for lines in f:
            temp = lines.split("\n")[0]
            ff.write(temp)

print("i")
"""
with open("db", "r") as f:
    file = f.read()
    with open("output", "r" ) as ff:
        with open("unique_not_in_db", "w+") as fff:
            for lines in ff:
                regex = ".*" + lines + "*."
                subprocess.Popen("grep " +regex+" db  >> test ", shell=True)
            print("i")


with open("db", "r") as f:
    file = f.read()
    with open("output", "r" ) as ff:
        with open("unique_not_in_db", "w+") as fff:
            for lines in ff:
                regex = ".*" + lines + "*."
                if re.search(regex, file):
                    fff.write(lines)
            print("i")

print("i")

with open("db", "r") as f:
    with open("output", "r" ) as ff:
        with open("unique_not_in_db", "a+") as fff:
            for line in f:
                for lines in ff:
                    regex = ".*" + lines
                    if re.match(regex, line):
                        fff.write(lines)

print("i")

with open("db", "r") as f:
    with open("output", "r" ) as ff:
        with open("unique_not_in_db", "a+") as fff:
            for line in f:
                for lines in ff:
                    regex = lines + "*."
                    if re.match(regex, line):
                        fff.write(lines)
