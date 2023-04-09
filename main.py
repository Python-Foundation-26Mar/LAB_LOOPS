#range func (break & continue)
for i in range(45,210):
    
    if i == 100:
        continue
    print(i)
    if i == 205:
        break

#while loop
Q = "what is the product of 7 * 24 ?"
while input (Q) != "168":
    print("Your Answer is wrong try again..")
else:
    print("You answered this Question correctly")