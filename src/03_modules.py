"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# --need to be in the src folder to perform any of this in the terminal
"""
Type the following in the terminal to see the results
    python 03_modules.py 5.68 "Hello" "Look it!" 321564 "GoodBye!"

    - or -

    python [filename] num "arg2" boolean
"""
# Use sys to get command line arguments from the user

# Print out the command line arguments in sys.argv, one per line: 
# YOUR CODE HERE

print ( sys.argv )
# The first argument will be the filename
if len(sys.argv) > 1 :
    for arg in sys.argv:
        print( arg )
    #below prints out the argument at index 1 if there is one
    print(sys.argv[1])

    # #Bellow is if you enter in a number as an argument at index 1
    print(float(sys.argv[1]) + 5)
else:
    print('No arguments provided')

# Print out the OS platform you're using:
# YOUR CODE HERE

# Returns a named tuple describing the Windows version currently running
print("I am using Windows" + " " + str(sys.getwindowsversion()[0]))

#Returns the platform
print("I am using " + str(sys.platform))

# Print out the version of Python you're using:
# YOUR CODE HERE

# printing implementation identifier name
print(sys.implementation.name)

# accessing the "version" tuple items within implementation
print("I am using Python" + " " + str(sys.implementation.version.major) + "." + str(sys.implementation.version.minor) )

# accessing implementation’s name and version
print(sys.implementation.cache_tag)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

"""
# NOTE when working with a new module, you can use dir and pass in that module to see all the attributes and methods you have access to
"""
# print(dir(os))

# Print the current process ID
# YOUR CODE HERE

print("The current process ID is: " + str(os.getpid()))

# Print the current working directory (cwd):
# YOUR CODE HERE

print("The current working directory is: " + str(os.getcwd()))

# Print out your machine's login name
# YOUR CODE HERE
print("The login name: " + str(os.getlogin()))