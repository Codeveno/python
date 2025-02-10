#tr-except block is used to catch exceptions in Python.
#example
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print ("Error: can\'t find file or read data")
else:
    print ("Written content in the file successfully")
    fh.close()


# In the above example, a file is opened in write mode. If the file does not exist, it would throw an exception and the program would crash.

# To avoid this, we use a try-except block so that if an exception occurs, we can handle it and prevent the program from crashing.
