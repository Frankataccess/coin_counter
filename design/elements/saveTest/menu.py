#menu

with open('save_test.txt', 'r') as file:
    # Initialize the sum to 0
    total_value_callable = 0
    total_bags_callable = 0
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
        total_value_callable += int(values[7])
        total_bags_callable = int(values[6])

#menu
choice = input("Enter [B] to see the total amount of bags counted \n Enter [V] to see the total value of all the bags counted \n Enter [S] to display the volunteers sorted by accuracy  Enter [T] to show the table in the terminal \n Enter [N] to add a new volunteer \n Enter [X] to exit")
choice = choice.upper()
if choice == "B": 
    print("The total amount of bags counted is: ",total_bags_callable)
elif choice == "V":
    print("The total value of all the bags counted is:",total_value_callable)
elif choice == "S":
    print()
    #display sorted list
elif choice == "T":
        with open("save_test.txt", 'r') as file:
            # Read the contents of the file
            file_contents = file.read()
            # Print the contents to the terminal
            print(file_contents)
elif choice == "N":
    print()
    #start from top 
elif choice == "E":
    exit()