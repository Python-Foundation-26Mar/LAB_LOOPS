#Loop Raha saleh 
# This is Lap 1 in the LOOP ...
for number in range(45, 211):
    if number == 100:
        continue
    print(number)
    if number == 205:
        break


# This is Lap 2 in the LOOP ...


# Ask  the user  
question = "What is the product of 7 * 24?"
answer = 168


while True:
    user_answer = int(input(question))
    # check if the answer is right...
    if user_answer == answer:
        print("You answered this question correctly!")
        break
    # if the answer is wrong...
    else:
        print("Your answer is wrong. Try again...")
        