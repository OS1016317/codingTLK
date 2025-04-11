# Step 1: Ask the user to input two numbers
first_number = int(input("Enter first two numbers: "))
second_number = int(input("Enter second two numbers: "))

# Step 2:Store the numbers in a tuple
numbers_tuple =(first_number, second_number)

# Step 3: Swap the value using tuple unpacking
first_number, second_number = second_number, first_number

# Step 4: Print the swapped values
print(f"Swapped values: ({first_number}, {second_number})")
