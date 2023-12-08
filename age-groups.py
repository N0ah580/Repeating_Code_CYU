# Programmer: Noah
# Description: Age Groups
age = input("Enter an age: ")
child = 0
adult = 0
senior = 0
counter = 0

#Create a loop that repeatedly counts ages and tallies them until 0 is entered
while age != "0":  
    age = float(age)
    
    #tally the answer
    if age <= 12:
        child += 1
    elif age < 65:
        adult += 1
    else:
        senior += 1
        
    #Ask for another age
    age = input("Enter an age: ")
    
#Print off the recorded answers
print ()
print (f" Children: {child}")
print (f" Adults: {adult}")
print (f" Seniors: {senior}")