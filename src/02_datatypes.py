"""
Python is a strongly-typed language under the hood, which means 
that the types of values matter, especially when we're trying
to perform operations on them. 

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12

# YOUR CODE HERE

# x + int(y)


print(x + int(y))


# Write a print statement that combines x + y into the string value 57

# YOUR CODE HERE

print(str(x) + y )

# Why is the value 57 when x is turned into a string?

# Because it is treating both values as letters or strings to be put together (like the bellow hello world example); not numbers/integers that are inputted and then have an operation performed on them.

print("hello" + " " + "world")