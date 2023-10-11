# Open the file in read mode
# Open the file in read mode
with open('save_test.txt', 'r') as file:
    # Initialize the sum to 0
    old_sum = 0
    # Flag to indicate whether to ignore the first row
    ignore_first_row = True
    # Read the file line by line
    for line in file:
        # Skip the first row
        if ignore_first_row:
            ignore_first_row = False
            continue
        # Split the line into values
        values = line.split()
        # Extract the value in the second column (index 1)
        # Convert it to an integer and add it to the total sum
        old_sum += int(values[6])

# Print the total sum
print("Sum of values in the second column, ignoring the first row:", old_sum)