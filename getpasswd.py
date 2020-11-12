'''
The getpass is a useful module of python that is used to take password input from the user.
The following script shows the use of the getpass module. 
getpass() method is used here to take the input as password 
and ‘if’ statement is used here to compare the input value
with the defined password. “you are authenticated” message will print
if the password matches otherwise it will print “You are not authenticated” message.
'''
#import getpass module
import getpass

# Take password from the user
passwd = getpass.getpass('Password:')

# Check the password
if passwd == "Let me Pass":
    print("You are authenticated")
else:
    print("Wrong password, you are not authenticated")