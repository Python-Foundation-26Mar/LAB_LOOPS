for elm in range(45,211):
    if elm == 100:
        continue
    elif elm > 205:
        break
    else:
        print(elm)


    #sloved second lab
    Question = "What is The product of 7*24?"
    answer = 168 

    while True:
        User_Answer= int(input(Question))


    if User_Answer == answer:
        print("you answerd this question correctly")
    else:
        print ("you anser is wrong Try again.....")
