#finally word in python is used to execute some code block irrespective of the exception is raised or not.
#example
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
finally:
    print ("Error: can\'t find file or read data")
    fh.close()
    