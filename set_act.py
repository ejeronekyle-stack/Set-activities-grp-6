# Set Activities (Unique, Unordered, No Duplicates)

# Activity 1: Remove Duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("Activity 1 - Unique values:", unique_numbers)

# Activity 2: Add and Remove
fruits = {"apple", "banana"}
fruits.add("orange")     
fruits.remove("banana") 
print("Activity 2 - Fruits set:", fruits)

# Activity 3: Set Operations
A = {1, 2, 3}
B = {3, 4, 5}
union_set = A.union(B)
intersection_set = A.intersection(B)
print("Activity 3 - Union:", union_set)
print("Activity 3 - Intersection:", intersection_set)

# Activity 4 (Challenge): Common Students
classA = {"jerone", "cedric", "marc"}
classB = {"marc", "charlz", "jerone","jeshley"}
common_students = classA.intersection(classB)
all_students = classA.union(classB)
print("Activity 4 - Common students:", common_students)
print("Activity 4 - All students:", all_students)
