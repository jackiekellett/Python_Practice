#    Camping List
# ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯

camping_stuff = "tent, sleeping bags, water, marshmallows, chocolate, graham crackers, lighter, lantern, mug"

print(camping_stuff)
print(type(camping_stuff))

camping_list = ['tent', 'sleeping bag', 'sleeping bag', 'water', 'marshmallows', 'chocolate', 'graham crackers', 'lighter', 'lantern', 'mug']

print(camping_list)
print(type(camping_list))

# Make a campsite with the Name, Lot number, Temperature, Dangerous?
camp_site = ['Mammoth Cave', 200, 76.4, False]

print(camp_site)
print(type(camp_site))

# Lists are ordered / sequential / indexed
# NOTE: the first item on a list is rank 0; hence, if we want the fifth item, we must specify [4]
item_5 = camping_list[4]

print(item_5)
