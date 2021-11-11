#3.3
"""
prints the sentence "Yes - Spathiphyllum is the 
best plant ever!" to the screen if the inputted 
string is "Spathiphyllum" (upper-case)
• prints "No, I want a big Spathiphyllum!" if the 
inputted string is "spathiphyllum" (lower-case)
• prints "Spathiphyllum! Not [input]!" 
otherwise. Note: [input] is the string taken as 
input.
Test your code using the data we've provided for 
you. And get yourself a Spathiphyllum, too!
• isupper(), islower(), lower(), upper(), rstrip(), 
lstrip(), strip() - investigate pls
"""

# plant=input()
plant='SPATHIPHYLLUM'
s='Spathiphyllum'
if plant.isupper:
    print('Yes - Spathiphyllum is the best plant ever!')
elif  plant.islower:
    print('No, I want a big Spathiphyllum!')
else: 
    print ("Spathiphyllum! Not",plant, "!" )
