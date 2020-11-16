'''
Regular expression or regex is used in python to match or search and replace any particular portion 
of a string based on the particular pattern. ‘re’ module is used in python to use a regular expression.
 The following script shows the use of regex in python. The pattern used in the script will match those 
 string where the first character of the string is a capital letter. 
 A string value will be taken and match the pattern using match() method. 
 If the method returns true, then a success message will print otherwise an instructional message will print.
 '''

#Import re module
import re

#Take any string data
string = input("Enter a string value: ")

# Define the searching pattern
pattern = '^[A-Z]'

#Match the pattern with input value 
found = re.match(pattern, string)

#Print message based on the return value
if found:
    print("The input value is started with the capital letter")
else:
    print("You have to type string start with the capital letter")    