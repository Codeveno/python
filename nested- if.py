#nested if is used when we have to check multiple conditions.
#example
y=100
if y>30:
    print("y is greater than 30")
    if y>50:
        print("y is greater than 50")
    else:
        print("y is less than 50")
else:
    print("y is less than 30")
