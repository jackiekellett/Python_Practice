#  Automated Barista
# ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

# Welcome the customer
print("\nHowdy! Welcome to the Computer Coffee House!")

# Name variable / Get the customer's name
name = input("What is your name?\n")



# Refuse service to banned customers
if name == "quinn" or name == "miranda":
    banned_status = input("Are you banned?\n")
    if banned_status == "yes":
        print("You're not welcome here, " + name + "! Get out!!!")
        exit()
    else:
        print("Okay, just checking!")

# Menu string
menu = "Latte, Coffee, Espresso, Americano, Frappuccino"

# Get the customer's order
order = input("Thanks for coming in today, " + name + "! What are you having today? Here's what we have on the menu:\n" + menu + "\n")

# Menu Pricing
if order == "latte":
    price = 5
elif order == "coffee":
    price = 2
elif order == "espresso":
    price = 3
elif order == "americano":
    price = 4
elif order == "frappuccino":
    price = 8
else:
    print("Sorry, we don't have that here.")
    price = 0
    exit()

# Get drink amount
amount = input("How many " + order + "s would you like?\n")

# Tax variable
tax = 0

# Calculate the total
total = (1 + tax) * (price * int(amount))

# Tell the customer the total
print("Alright, " + name + ", your total today is:\n    $" + str(total))
