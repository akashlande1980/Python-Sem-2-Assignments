# 4.1 Create and Access Dictionary Elements
print("4.1 Create and Access Dictionary Elements")
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print("Created Dictionary:", my_dict)

# Accessing elements
print("Access 'name':", my_dict["name"])  # Accessing a value by its key
print("Access 'age':", my_dict.get("age"))  # Using `get()` to access a value

# 4.2 Update Dictionary
print("\n4.2 Update Dictionary")
my_dict["age"] = 26  # Updating an existing key-value pair
print("Updated 'age' to 26:", my_dict)

my_dict["profession"] = "Engineer"  # Adding a new key-value pair
print("Added 'profession':", my_dict)

# 4.3 Removing Elements
print("\n4.3 Removing Elements")
removed_value = my_dict.pop("city")  # Removing a specific key
print(f"Removed 'city': {removed_value}")
print("Dictionary After Removing 'city':", my_dict)

del my_dict["name"]  # Deleting a key-value pair
print("Dictionary After Deleting 'name':", my_dict)

my_dict.clear()  # Clearing all elements from the dictionary
print("Dictionary After Clearing All Elements:", my_dict)

# 4.4 Merging Dictionaries
print("\n4.4 Merging Dictionaries")
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4, "e": 5}
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)

merged_dict = dict1.copy()  # Copy dict1 into a new dictionary
merged_dict.update(dict2)  # Merge dict2 into the new dictionary
print("Merged Dictionary:", merged_dict)
