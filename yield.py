#yield in python is used to return a value from a function without terminating the function.
#It is used to return a generator object to the caller function.
#The yield keyword is used to return a value from a function without terminating the function.
#It is used to return a generator object to the caller function.
#The yield keyword is used to return a value from a function without terminating the function.
#It is used to return a generator object to the caller function.
#The yield keyword is used to return a value from a function without terminating the function.
#It is used to return a generator object to the caller function.
#The yield keyword is used to return a value from a function without terminating the function.
#It is used to return a generator object to the caller function.

#example
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

# Driver code to check above generator function
def main():
    for value in simpleGeneratorFun():
        print(value)
        #print output
        #1

if __name__ == "__main__":
    main()
    


