numbers = [12, 3, 5, 19, 7, 3, 1, 5]
#i define this variable to save the largest numbers, starts with position 0
largest_number = numbers[0]
#i define this variable to save the smallest number, starts with position 0
smallest_number = numbers[0]
#I go through each element in the list
for element in numbers:
    #compare the element of the list with the largest number
    if element >= largest_number:
        largest_number = element
    #compare the element of the list to the smallest number
    if element <= smallest_number:
        smallest_number = element
print(f"The largest number is {largest_number}.")
print(f"The smallest number is {smallest_number}.")