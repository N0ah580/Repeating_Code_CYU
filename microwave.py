# Programmer: Noah
# Description: Microwave

from time import sleep

time = int (input ("Enter seconds: "))

#count down from given number 
counter = time
while counter >= 0:
    print (counter)
    counter -= 1
    sleep (1)

#print the staggered beeps
sleep (1)
print ("BEEP!")
sleep (1)
print ("BEEP!")
sleep (1)
print ("BEEP!")
sleep (1)
print ("BEEP!")
sleep (1)
print ("BEEP!")
    
