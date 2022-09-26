#    Camping List
# ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

# camping_stuff = "tent, sleeping bags, water, marshmallows, chocolate, graham crackers, lighter, lantern, mug"

# print(camping_stuff)
# print(type(camping_stuff))

# camping_list = ['tent', 'sleeping bag', 'sleeping bag', 'water', 'marshmallows', 'chocolate', 'graham crackers', 'lighter', 'lantern', 'mug']

# print(camping_list)
# print(type(camping_list))

# # Make a campsite with the Name, Lot number, Temperature, Dangerous?
# camp_site = ['Mammoth Cave', 200, 76.4, False]

# print(camp_site)
# print(type(camp_site))

# # Lists are ordered / sequential / indexed
# # NOTE: the first item on a list is index 0; hence, if we want the fifth item, we must specify [4]
# item_5 = camping_list[4]

# print(item_5)

########################################
########################################

# #    Camping List
# # ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

# supplies = ['tent', 'sleeping bag', 'sleeping bag', 'water', 'marshmallows', 'chocolate', 'graham crackers', 'lighter', 'lantern', 'mug']

# # Make a campsite with the Name, Lot number, Temperature, Dangerous?
# camp_site = ['Mammoth Cave', 200, 76.4, False]

# # Add items to the Supplies list using Append
# #supplies.append('toilet paper')
# #supplies.append('pillow')

# # Add multiple items to list using Extend
# #supplies.extend(['toilet paper', 'pillow', 'pillow'])

# # Add item to the beginning of your list using Insert
# # the first value is the index, the second is the data to add
# supplies.insert(0, 'toilet paper')
# #print(supplies)

# # What happens when you try to Insert something at the end of the list?
# supplies.insert(-1, 'pillow')
# print(supplies)
# ### This places the item SECOND TO LAST since it is INSERTING

########################################
########################################

#    Camping List
# ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

supplies = ['tent', 'sleeping bag', 'sleeping bag', 'water', 'marshmallows', 'chocolate', 'graham crackers', 'lighter', 'lantern', 'mug']

# Make a campsite with the Name, Lot number, Temperature, Dangerous?
camp_site = ['Mammoth Cave', 200, 76.4, False]

# # You packed an extra sleeping bag, get rid of it!
# ### CLEAR
# supplies.clear()
# print(supplies)
# ### OH NO!! Clear DELETED THE WHOLE LIST

# # You packed an extra sleeping bag, get rid of it!
# ### REMOVE
# supplies.remove('sleeping bag')
# print(supplies)
# ### SUCCESS

# You packed an extra sleeping bag, get rid of it!
### POP
supplies.pop(1)
print(supplies)
### SUCCESS

# What happens if you POP the same index multiple times?
supplies.pop(1)
supplies.pop(1)
print(supplies)
### It deletes the item at index 1, then reevaluates the index and then removes the item now at index 1
