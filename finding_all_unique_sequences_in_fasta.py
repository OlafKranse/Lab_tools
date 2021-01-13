##make a file of unqiue possible sequences in a given range (change sequence size)
### setup ###
sequence_size = 25
additional_ranges = 10

### main script ###
sequence_size -= 1
file = open("output", "w")
file.close()

from itertools import product

def analyze_gc(text):
    count = 0
    letter_count = 0
    for char in text:
        if char.isalpha():
            count += 1
    for e in text:
        if e == "g" or e == "c":
            letter_count += 1
    p = float(letter_count) / float(count) * 100
    return p
### not finishhed def###

def analyze_number_of_repeats(text):
    check_string = text
    numbers = []
    for x in sorted(set(text)):
        i = 1;
        while x * i in text:
          i += 1
        numbers.append(i-1)
    return(max(numbers))

alphabets = "atcg"
input_range = enumerate(map(int, range(sequence_size)))

for i in range(additional_ranges):
    sequence_size += 1
    with open("output", "a") as f:
        for input_range in product(alphabets, repeat=sequence_size):
            writeme = "".join(input_range)
            if (analyze_gc(writeme) >= 39) and (analyze_gc(writeme) <= 55) :
                if (analyze_number_of_repeats(writeme)) <= 3:
                    f.write(writeme+ "\n")
