#  Automated Barista
# ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

# Welcome the customer
print("\nHowdy! Welcome to the Computer Coffee House!")

# Name variable / Get the customer's name
name = str.capitalize(input("What is your name?\n"))

banned_list = ['Quinn', 'Miranda', 'Rose']

# Refuse service to banned customers
if name in banned_list:
    banned_status = str.capitalize(input("Are you banned?\n"))
    if banned_status == "Yes":
            print(str.upper("You're not welcome here, " + name + "! Get out!!!"))
            exit()
    else:
        print("Okay, just checking!\n")

# Menu string
menu = "Latte, Coffee, Espresso, Americano, Frappuccino"

# Get the customer's order
order = str.capitalize(input("Thanks for coming in today, " + name + "! What are you having today? Here's what we have on the menu:\n" + menu + "\n"))

# Menu Pricing
if order == "Latte":
    price = 5
elif order == "Coffee":
    price = 2
elif order == "Espresso":
    price = 3
elif order == "Americano":
    price = 4
elif order == "Frappuccino":
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
