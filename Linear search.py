# linear search by RegiKing


import random

# standard list
nlist = [23, 65, 12, 87, 98, 12, 99, 101, 21, 28]

# list comprehension 
nlist = [random.randrange(1,100) for x in range(1000)]

# search term
sTerm = int(input("Enter a search term: "))


# Checks is the item matches the search term
for item in nlist:
    if sTerm == item:
        Found = True

# detects if the item has been found in order to give an output
if Found == True:
    print("Data found")
else:
    print("Data not found")

