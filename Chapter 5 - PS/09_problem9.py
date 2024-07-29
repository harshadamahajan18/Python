# Can you change the values inside a list which is contained in set S?


s = {8, 7, 12, "Harry", [1,2]}

s[4][0] = 9 # Error


# No, you cannot directly change the values inside a list that is contained in a set in Python. This is because lists are mutable, and mutable types are not allowed as elements in a set. Sets require their elements to be hashable, and mutable types (like lists) are not hashable due to their changeable nature.