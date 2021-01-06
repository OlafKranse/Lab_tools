"""
This script checks all the fasta files in a given folder against a file called "ref".

it then alligns them and puts them in an output file called "alligned".

"""
import os
import subprocess
from Bio.Seq import Seq

file_create = open("alligned", "w")
file_create.close()

print("some sequencing runs export the sequence in multiple lines, make sure its single line.")
dir_name = os.getcwd()
print(dir_name)
list_dir = os.listdir(dir_name)
a = open("alligned", "w+")
a.close()
to_remove = ("check_sanger_seq.py", "ref", "alligned", '.idea', "for_allignment", "revered")
#removing scripts in folder
for things in to_remove:
    list_dir.remove(things)
#remove me later!@!@!@
"""
list_dir.remove(".idea")
list_dir.remove('for_allignment')
list_dir.remove('revered')
"""

def allign(infile):
    subprocess.call(str("echo " + "\\\n >>" + infile), shell=True)
    subprocess.call(str("cat " + infile + " ref > for_allignment"), shell=True)
    subprocess.call(str("mafft for_allignment >> alligned") , shell=True)

    #subprocess.call(str("echo " + "\\\n >> revered"), shell=True)

def allign_reverse(rev, the_name):
    subprocess.call(str("echo \"" + the_name[1] + "\" > revered"), shell=True)
    subprocess.call(str("echo \"" + rev + "\" >> revered"), shell=True)
    subprocess.call(str("cat revered ref > for_allignment"), shell=True)
    subprocess.call(str("mafft for_allignment >> alligned"), shell=True)


for things in list_dir:
    with open(things) as f:
            allign(things)
            for lines in enumerate(f):
                print(lines[1])
                if ">" in lines[1]:
                    name = lines
                    seq = Seq(next(f))
                    reverse_comp = str(seq.reverse_complement())
                    allign_reverse(reverse_comp, name)



