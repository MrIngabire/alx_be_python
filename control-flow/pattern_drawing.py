# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Use a while loop to iterate through each row
row = 0
while row < size:
    # Use a for loop to print asterisks in each row without newline
    for column in range(size):
        print("*", end="")
    # Move to the next line after printing each row
    print()
    row += 1
