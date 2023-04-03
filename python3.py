#1
for i in range(45, 211):
    if i == 100:
        continue
    elif i > 205:
        break
    else:
        print(i)

#2
while True:
    answer = input("What is the product of 7 * 24? ")
    if answer == "168":
        print("You answered this question correctly!")
        break
    else:
        print("Your answer is wrong, please try again...")
