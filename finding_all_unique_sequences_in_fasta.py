##make a file of unqiue possible sequences in a given range (change sequence size)
sequence_size = 24
file = open("output", "w")
file.close()

from itertools import combinations_with_replacement

alphabets = ["a", "t", "c", "g"]


input_range = enumerate(map(int, range(sequence_size)))


for i in range(6):
    sequence_size += 1
    with open("output", "a") as f:
        for input_range in combinations_with_replacement(alphabets, sequence_size):
            writeme = "".join(input_range)
            f.write(writeme+ "\n")



"""with open("output", "a") as f:
    for input_range in combinations_with_replacement(alphabets, sequence_size):
        write_me = "".join(str(input_range)+ "\n")
        f.write(str(input_range)+ "\n")"""

