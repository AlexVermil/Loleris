import math

r = float(input("Sisestage ringi raadius: "))
c = 2 * math.pi * r
s = math.pi * r**2
print(" Pindala " + str(round(s,2)) + " Ümbermõõt " + str(round(c,2)))
