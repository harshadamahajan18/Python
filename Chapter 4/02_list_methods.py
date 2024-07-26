friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends)

friends.append("Harry")
print(friends)

l1 = [1, 34, 62, 2, 6, 11]
# l1.sort() # [1, 2, 6, 11, 34, 62]
# l1.reverse() # [11, 6, 2, 62, 34, 1]
# l1.insert(3, 33333) # [1, 34, 62, 33333, 2, 6, 11] # Insert 333333 such that its index in the list is 3
# value = l1.pop(3)
# print(value)
l1.remove(62)
print(l1)
print(type(l1))