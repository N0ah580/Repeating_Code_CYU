# Programmer: Noah
# Description: Age Groups
age = int(input("Enter an age: "))
child = 0
adult = 0
senior = 0
counter = 0

#Create a loop that repeatedly counts ages and tallies them until 0 is entered
while age >= 0:  
    
    #tally the answer
    if age <= 12:
        child += 1
    elif age < 65:
        adult += 1
    else:
        senior += 1
        
    #Ask for another age
    age = int (input("Enter an age: "))
    
#Print off the recorded answers
print ()
print (f" Children: {child}")
print (f" Adults: {adult}")
print (f" Seniors: {senior}")