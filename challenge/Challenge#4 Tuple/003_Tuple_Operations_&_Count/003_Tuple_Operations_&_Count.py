# Step 1: Creat a tuple with repeated values
fruits_tuple = ("apple", "banana", "apple", "cherry", "banana", "apple")

# Step 2: Ask the user to enter a fruit name
fruits_name = input("Enter a fruit name: ")

# Step 3: Print how many times that fruit appears in the tuple
fruit_count = fruits_tuple.count(fruits_name)
print(f"{fruits_name} appears {fruit_count} time in the tuple.")

