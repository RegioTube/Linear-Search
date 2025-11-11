# linear search by RegiKing
z = 0
y = 0
Found = False
import random
#    ^^^ variables that have to be defined


# standard list
nlist = [23, 65, 12, 87, 98, 12, 99, 101, 21, 28, 87] #this can be extended

# list comprehension (this overrides the other list, but its disabled) 
# nlist = [random.randrange(1,100) for x in range(1000)]""

# search term (this is what the code is looking for in the list)
sTerm = int(input("Enter a search term: "))


# Checks is the item matches the search term
for item in nlist:
    if sTerm == item:
        
        if Found == True: #if it matches the item, but its already been looped it increments the counter by 1
            y = y + 1

        else:
            Found = True #otherwise it sets Found as "True" so when it loops again it will increment because of the other if statement
            y = 1 #also sets y to 1 incase it only appears once and doesn't get incremented
        z = z + 1

    else:
        z = z + 1

# detects if the item has been found in order to give an output

if Found == True:
    print("Data found, Times detected:", y) #out puts that the data is in the list and how many times it arrived
    print("Operation count:", z)
else:
    print("Data not found")
    print("Operation count:", z)
