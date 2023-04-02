
# First 
num=range(45,210)

for elements in num :
    if elements==100:
        continue
    print("Element :", elements)
    if elements==205:
        break

#------------------------------------------------------------

# Second 

msg="what is the product of 7 * 24 ?"

while int(input(msg)) != 168 :
     print("Your Answer is wrong try again.")
         
else:       

     print("Your Answer You answered this Question correctly")  