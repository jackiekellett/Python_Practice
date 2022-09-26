#  Automated Barista
# ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

# Price variable
price = 5
# Tax variable
tax = 0

# Menu string
menu = "Latte, Coffee, Espresso, Americano"

# Welcome the customer
print("\nHowdy! Welcome to the Computer Coffee House!")

# Name variable / Get the customer's name
name = input("What is your name?\n")

# Refuse service to banned customers
if name == "Quinn":
    print("You're not welcome here, " + name + "! Get out!!!")
    exit()

# Get the customer's order
order = input("Thanks for coming in today, " + name + "! What are you having today? Here's what we have on the menu:\n" + menu + "\n")
# Get drink amount
amount = input("How many " + order + "s would you like?\n")
# Calculate the total
total = (1 + tax) * (price * int(amount))
# Tell the customer the total
print("Alright, " + name + ", your total today is: $" + str(total))
