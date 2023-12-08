# Programmer: Noah
# Description: Square

from math import sqrt

#ask for square area and confirm it's positive
area = int (input ("Enter the square's area: "))
while area < 0:
    print ("The area must be positive! Try again.")
    area = int (input ("Enter the square's area: "))

print ()

#calculate square root and print answer
answer = sqrt (area)
print (f"The square's side length is {answer:,.3f}")
