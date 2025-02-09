# for loop is used  when we know the exact number of times in which we need to iterate through

#function
###SI -this is the name of the function

#Amount
#Principle



def SimpleIinterest(principal, Time, R):
    SI=(principal*Time*R)/100
    return SI

Principle = print(input("kindly enter the priciciple amount: "))
Time =int(input("kindly enter the time: "))
Rate =int(input("kindly enter the rate:" ))
Amount=Principle + SimpleIinterest(Principle, Time, Rate)
print(f"the total amountnto be paid back is: {Amount: 2f}")
