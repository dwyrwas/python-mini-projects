import sys
import random

# check if filename is supplied as a command line argument
if sys.argv[1:]:
    filename = sys.argv[1]
else:
    filename = input("What is the name of the file? (extension included): ")

try:
    file = open(filename,'r') #include argument to make sure that file is opened in read-only mode
except (FileNotFoundError, IOError): # handle exception
    print("File doesn't exist!")
    exit()


# get lines
lines = file.readlines() #Return all lines in the file, as a list where each line is an item in the list
# generate a random number between possible interval
random_line = random.randint(0, len(lines))
#print the line we want
print(lines[random_line].rstrip())

file.close() #close the file once we print the word we wanted
