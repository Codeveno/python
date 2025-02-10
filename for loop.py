#for is used to iterate over a sequence
#example
fruits = ["apple", "banana", "cherry"]
for y in fruits:
    print(y)


# In the above example, the for loop iterates over the list of fruits and prints each fruit in the list.

# The for loop does not require an indexing variable to set up the loop. Instead, the for loop can use the iteration variable directly.
#unique example
#example
for x in "banana":
    print(x)

    # to print specific letter in a string
    #example
    for x in "banana":
        if x == "n":
            print(x)



#example
student=["john","james","jane"]
for x in student:
    if x=="james":
        print(x)
