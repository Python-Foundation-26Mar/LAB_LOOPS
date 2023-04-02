
myVar = range(45, 210)
for number in myVar:
    if number == 100:
        continue
    elif number == 205:
        break
    print("The sequence is:", number)