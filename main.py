#  Automated Barista
# ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

# Welcome the customer
print("\nHowdy! Welcome to the Computer Coffee House!")

# Name variable / Get the customer's name
name = input("What is your name?\n")

# Menu string
menu = "Latte, Coffee, Espresso, Americano"


# Order variable / Get the customer's order
order = input("Thanks for coming in today, " + name + "! What are you having today? Here's what we have on the menu:\n" + menu + "\n")

# Price variable
price = 5

# Amount variable / Get the number of drinks
amount = input("How many " + order + "s would you like?\n")

# Tax variable
tax = 0

# Calculate the total
total = (1 + tax) * (price * int(amount))

# Tell the customer the total
print("Alright, your total today is $" + str(total) + ".\n")
