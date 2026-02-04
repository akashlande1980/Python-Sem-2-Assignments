# 1.1 Create and access list elements
print("1.1 Create and Access List Elements")
my_list = [10, 20, 30, 40, 50]
print("Created List:", my_list)
print("Access Element at Index 2:", my_list[2])  # Accessing 3rd element

# 1.2 Add and Remove list elements
print("\n1.2 Add and Remove List Elements")
my_list.append(60)  # Adding an element at the end
print("List After Adding 60:", my_list)

my_list.insert(2, 25)  # Inserting an element at index 2
print("List After Inserting 25 at Index 2:", my_list)

my_list.remove(30)  # Removing an element (value 30)
print("List After Removing 30:", my_list)

popped_element = my_list.pop()  # Removing the last element
print("Popped Element:", popped_element)
print("List After Popping Last Element:", my_list)

# 1.3 Sort list elements
print("\n1.3 Sort List Elements")
my_list.sort()  # Sorting the list in ascending order
print("List After Sorting in Ascending Order:", my_list)

my_list.sort(reverse=True)  # Sorting the list in descending order
print("List After Sorting in Descending Order:", my_list)

# 1.4 Reverse list elements
print("\n1.4 Reverse List Elements")
my_list.reverse()  # Reversing the list
print("List After Reversing:", my_list)
