# Creating an empty list called my_list
my_list=[]
# Adding elements to the list using append
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Modifying the list by inserting an element at index 1
my_list.insert(1,15)
# Extending the list with multiple elements
my_list.extend([50,60,70])
# Removing the last element from the list
my_list.pop()
# sorting the list in ascending order
my_list.sort()

# Printing the list and the index of the element 30

print("print the list :" , my_list)
print("the index of 30 is : " , my_list.index(30))