tm = str(input("TM: "))
size = str(input("size fragment: "))
Y = int(input("Reacton volume PCR: "))
Nucl_water = 32.5/50
Buffer = 10/50
DNTP = 1/50
Primer_F = 2.5/50
Primer_R = 2.5/50
polymerase = 0.5/50
X = int(input("Number of PCR sampels: "))
#print("The TM used = "+ str(tm))
print("You will need for your MasterMix: ")
a = Nucl_water*X*Y
b = Buffer * X*Y
c = DNTP * X*Y
d = Primer_F * X*Y
e = Primer_R * X*Y
f = polymerase * X*Y
print(str(round(a, 1)) + " µL" + " Nuclease free water")
print(str(round(b, 1)) + " µL" + " Phusion Buffer")
print(str(round(c, 1)) + " µL" + " DNTPs")
print(str(round(d, 1))  + " µL" + " Primer_F")
print(str(round(e, 1))  + " µL" + " Primer_R")
print(str(round(f, 1)) + " µL" + " Phusion polymerase")

