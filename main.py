


for number in range(45, 210):
    if number == 100:
        continue

    if number == 205:
        break

    print(number)

## 2) Using a while loop and input , do the following :

while int(input("what is the product of 7 * 24 ? ")) != 7*24:
    print("Your Answer is wrong try again..")
else:
    print("You answered this Question correctly")