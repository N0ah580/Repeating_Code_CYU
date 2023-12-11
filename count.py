# Programmer: 
# Description: Ask the user what to count by and when to end, then print the 
#              count.

count_by = int (input("What do you want to count by? "))
end_at = int (input("What number do you want to end at? "))
print()

num = count_by
while num <= end_at:
    print(num)
    num += count_by
  