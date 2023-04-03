#1
number= range(45,210)

for element in number:
    if element == 100:
        continue
    print("element", element)

    if element == 205:
        break
#2
x = "what is the product of 7 * 24 ?"

while input(x) != "168":
    print("Your Answer is wrong try again..")
else:
    print("You answered this Question correctly")