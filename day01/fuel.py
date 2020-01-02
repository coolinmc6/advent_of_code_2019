import math

totalFuel = 0 

f=open("data.txt", "r") #opening input file
f1 = f.readlines() #reading input txt file
for mass in f1:
    fuel = math.floor(int(mass)/3)-2
    totalFuel += fuel

print(totalFuel)