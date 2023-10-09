
# Read the name you want to search for
volunteer_name = input("Enter volunteer name: ")

# Open the file and search for the name
with open("save_test.txt", 'r') as file:
    for line in file:
        # Split the line into columns
        columns = line.strip().split()
        # Check if the name exists in the first column
        if columns[0] == volunteer_name :
            # If found, print the entire row
            print("Name found. Details: ", columns)
            # If you want to access a specific value in the same row, you can do so by index
            # For example, the coin type in the second column would be columns[1]
            print(columns[5])
            break
    else:
        # If the loop completes without finding the name
        print("Name not found in the file.")