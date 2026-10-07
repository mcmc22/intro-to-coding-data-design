#create an empty list to save the colors
colors = []
#repear the process just 5 times
for element in range(5):
    #the user enter the colors
    color = input("Enter your favourite color: ")
    #with append we add the color to the list colors
    colors.append(color)
#print the asked sentence using + to add the necesary commas and the comand join, joins the list colors in the same text
print("your favourite colors are " + ", ".join(colors))





