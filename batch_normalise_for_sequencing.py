"""
this is a form of the formula v1*c1=V2*c2

it is as follows 

((C1*V1)/C2)-V1 = V2

"""
"""
print("Volume sample: ")
V1 = int(input())
print("Concetration sample: ")
C1 = int(input())
print("Wanted concentration: ")
C2 = int(input())

V2 = ((C1*V1)/C2)-V1
print("Volume to add: ")
print(V2)
"""
print("Volume sample: ")
V1 = int(input())
print("Wanted cocentration in ng/ul: ")
C2 = int(input())

with open("in_file") as f:
    for lines in f:
        name = lines.split(",")[0]
        concentration_temp = lines.split(",")[1]
        concentration = int(concentration_temp.split("\n")[0])
        ul_to_add = ((V1*concentration)/C2)-V1
        total_vol = ((V1*concentration)/C2)
        print("ul to add: "+ str(ul_to_add)+" , name: "+name+",origional conc: "+ str(concentration)+ ", total vol: ", str(total_vol))
