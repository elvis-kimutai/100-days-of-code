print("Welcome to the rollercoaster")
height = int(input("What is your height in cm?"))
bill = 0

if height >= 100:
    print("You can ride the rollercoaster!")
#billing according to the age
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child ticket is 5$")
    elif age <= 18:
        bill = 7
        print("Youth ticket is 7$.")
    else:
        bill = 12
        print("Adult ticket is 12$.")
# if they want photos
    photos = input("Do you want Hot photos taken? Y or N ")
    if photos == "Y":
        bill += 3
    print(f"Your total bill is {bill}")

else:
    print("Sorry you have to grow taller")