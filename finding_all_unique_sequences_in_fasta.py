##make a file of unqiue possible sequences in a given range (change sequence size)
### setup ###
sequence_size = 3
additional_ranges = 1

### main script ###
sequence_size -= 1
file = open("output", "w")
file.close()

from itertools import product

alphabets = "atcg"


input_range = enumerate(map(int, range(sequence_size)))


for i in range(additional_ranges):
    sequence_size += 1
    with open("output", "a") as f:
        for input_range in list(product(alphabets, repeat=sequence_size)):
            writeme = "".join(input_range)
            f.write(writeme+ "\n")



"""with open("output", "a") as f:
    for input_range in combinations_with_replacement(alphabets, sequence_size):
        write_me = "".join(str(input_range)+ "\n")
        f.write(str(input_range)+ "\n")"""

