#new empty list to put all even numbers
even_numbers = []
#my range is from 1 to 21, to include de 20. if not, the list only goes to 18
for element in range(1,21):
    #i want only the even, that means only the numbers that have the rest = 0 when i divide the number in a half
    if (element%2 == 0):
        #that commend allows me to add items to the list
        even_numbers.append(element)
print(even_numbers)