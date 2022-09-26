#  Automated Barista
# ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

# Welcome the customer
print("\nHowdy! Welcome to the Computer Coffee House!")

# Name variable / Get the customer's name
name = input("What is your name?\n")

# Refuse service to banned customers
if name == "Quinn":
    banned_status = input("Are you banned?\n")
    if banned_status == "Yes":
        print("You're not welcome here, " + name + "! Get out!!!")
        exit()
    else:
        print("Okay, just checking!")


# Menu string
menu = "Latte, Coffee, Espresso, Americano, Frappuccino"

# Get the customer's order
order = input("Thanks for coming in today, " + name + "! What are you having today? Here's what we have on the menu:\n" + menu + "\n")

if order == "Latte":
    price = 5

if order == "Coffee":
    price = 2

if order == "Espresso":
    price = 3

if order == "Americano":
    price = 4

if order == "Frappuccino":
    price = 8

# Get drink amount
amount = input("How many " + order + "s would you like?\n")

# Tax variable
tax = 0

# Calculate the total
total = (1 + tax) * (price * int(amount))

# Tell the customer the total
print("Alright, " + name + ", your total today is: $" + str(total))
