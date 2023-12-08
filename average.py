# Programmer: Noah
# Description: Average

#ask for first grade and start counters
grade = input("Enter a student's grade: ")
total = 0
counter = 0

#Create a loop that repeatedly counts grades and tallies them until 0 is entered
while grade != "0":  
    grade = float(grade)
    
    if grade < 0:
        print ("Invalid percent grade! Try again.")
        
    elif grade > 100:
        print ("Invalid percent grade! Try again.")
    
    else:
        counter += 1
        total += grade
        
    #Ask for next grade    
    grade = input("Enter a student's grade: ")
    
  #find and print the class average  
average = total / counter
print (f"The class average is {average:,.1f}%.")
    