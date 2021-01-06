"""
same as normal script but automated:
in file : "in"
the file has to look like:
name,concentration in ng,size in kb
eg. Hshca_1423,176,0.5
where the value and the name are seperated by a comma



calculates from your concentration and bp size of a overhang template how much you need to add for optimal ligation


formula example: (50ng vector * 0.5 kb insert)/3 kb vector
default script assumes 50 ng vector and 3 kb size of vector to be used.
it uses a optimal ratio of 3:1


"""
ratio = 3
vector_size = 3
ng_of_plasmid = 50
in_file = "in"


with open(in_file) as f:
    for lines in f:
        name = lines.split(",")[0]
        concentration = int(lines.split(",")[1])
        size_temp = lines.split(",")[2]
        size = float(size_temp.split("\n")[0])
        vector_ammount = ((ng_of_plasmid*size)/vector_size)*3
        ul_needed = vector_ammount/concentration
        print("ul to add: "+ str(ul_needed)+" , name: "+name," , size insert: ",size," , ng added: ", vector_ammount)



