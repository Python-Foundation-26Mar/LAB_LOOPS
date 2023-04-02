#Solve the first lab loops

number=range(45,210)
for elements in number:
    
      if elements==100:
            continue
      print("elenmrnt:",elements)
      if elements==205:
            break
      
#Solve the second lab loops
X="what is the product of 7 * 24 = ?"
while int(input(X)) != 168 :
      print("Your Answer is wrong try again.")
else:
 print("Your Answer You answered this Question correctly")