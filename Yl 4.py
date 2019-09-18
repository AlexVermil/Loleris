a = int(input("Esimene : "))
b = int(input("Teine : "))
c = int(input("Kolmas : "))

if a > b and a > c:
    maximum = a
elif b > c:
    maximum = b
else:
    maximum = c
print("Maksimum on: " + str(maximum))