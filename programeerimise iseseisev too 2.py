results = [10, 18, 65, 100, 255]

max=max(results[0], results[1])

secondmaximum=min(results[0], results[1])

for i in range(2, len(results)):
    if results[i]>max:
        secondmax=max
        max=results[i]
    else:
        if results[i]>secondmax:
            secondmax=results[i]
            
print("Second Highest Number In List Is: " ,str(secondmax))
                