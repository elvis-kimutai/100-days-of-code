import random

name_string = input("Enter everybodys name separated by a comma ")
names = name_string.split(", ")

no_items = len(names)

payer_choice = random.randint(0, no_items - 1)

payer = names[payer_choice]
print(payer + " will pay the bill today")