# 2.1 Create and Access Set Elements
print("2.1 Create and Access Set Elements")
set_a = {10, 20, 30, 40, 50}
print("Created Set A:", set_a)

# Accessing elements (Iterating through the set)
print("Accessing Set Elements:")
for element in set_a:
    print(element, end=" ")
print()

# 2.2 Union of the Elements
print("\n2.2 Union of the Elements")
set_b = {40, 50, 60, 70, 80}
print("Set B:", set_b)
union_set = set_a.union(set_b)
print("Union of Set A and Set B:", union_set)

# 2.3 Intersection of the Elements
print("\n2.3 Intersection of the Elements")
intersection_set = set_a.intersection(set_b)
print("Intersection of Set A and Set B:", intersection_set)

# 2.4 Difference of the Elements
print("\n2.4 Difference of the Elements")
difference_set_a_b = set_a.difference(set_b)  # Elements in A but not in B
print("Difference of Set A - Set B:", difference_set_a_b)

difference_set_b_a = set_b.difference(set_a)  # Elements in B but not in A
print("Difference of Set B - Set A:", difference_set_b_a)
