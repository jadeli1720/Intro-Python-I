"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

From above link:
    a[start:stop]  # items start through stop-1
    a[start:]      # items start through the rest of the array
    a[:stop]       # items from the beginning through stop-1
    a[:]           # a copy of the whole array

    step value, which can be used with any of the above:
    a[start:stop:step] # start through not past stop, by step

    The key point to remember is that the :stop value represents the first value that is NOT in the selected slice. So, the difference between stop and start is the number of elements selected (if step is 1, the default).

    The other feature is that start or stop may be a negative number, which means it counts from the end of the array instead of the beginning. So:

    a[-1]    # last item in the array
    a[-2:]   # last two items in the array
    a[:-2]   # everything except the last two items

    Similarly, step may be a negative number:

    a[::-1]    # all items in the array, reversed
    a[1::-1]   # the first two items, reversed
    a[:-3:-1]  # the last two items, reversed
    a[-3::-1]  # everything except the last two items, reversed

    Python is kind to the programmer if there are fewer items than you ask for. For example, if you ask for a[:-2] and a only contains one element, you get an empty list instead of an error. Sometimes you would prefer the error, so you have to be aware that this may happen.


Use Python's slice syntax to achieve the following:
"""

   #[0, 1, 2, 3, 4, 5] 
a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
print(a[1:2]) #Starts at [1] and does not include anything beyond [2]

# Output the second-to-last element: 9
print(a[4:5])

# Output the last three elements in the array: [7, 9, 6]
print(a[-3:])

# Output the two middle elements in the array: [1, 7]
print(a[2:4])  

# Output every element except the first one: [4, 1, 7, 9, 6]
print(a[1:]) 

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[:-1])

# For string s...
"""
    +---+---+---+---+---+---+
    | P | y | t | h | o | n |
    +---+---+---+---+---+---+
    0   1   2   3   4   5   6
    -6  -5  -4  -3  -2  -1
"""

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
# print(len(s))
print(s[7:12])