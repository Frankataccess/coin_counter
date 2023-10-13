#open file so total value and total bags is defined
with open('CoinCount.txt', 'r') as file:
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

#sorting

with open('CoinCount.txt', 'r') as file:
    lines = file.readlines()
# Split lines into a list of lists based on whitespace (assuming space-separated values)
list_of_lists = [line.strip().split() for line in lines[1:]]  # Skip the header line

# Sort the list of lists by the accuracy column (assuming accuracy is the fourth column, index 3)
sorted_list_of_lists = sorted(list_of_lists, key=lambda x: float(x[3]), reverse=True)



run = True

while run == True:
    
    #menu
    print (" \n Enter [N] to add a new volunteer \n Enter [B] to see the total amount of bags counted \n Enter [V] to see the total value of all the bags counted \n Enter [S] to display the volunteers sorted by accuracy \n Enter [T] to show the table in the terminal \n Enter [X] to exit")
    choice = input(" \n Enter your choice: ")
    choice = choice.upper()
    if choice == "B": 
        print("The total amount of bags counted is: ",total_bags_callable)
    elif choice == "V":
        print("The total value of all the bags counted is:",total_value_callable)
    elif choice == "S":
        # Display header
        print(lines[0].strip())
       # Display sorted content in the terminal
        for row in sorted_list_of_lists:
            formatted_row = "{: <20} {: <20} {: <20} {: <20} {: <20} {: <20} {: <20} {: <10}".format(*row)
            print(formatted_row)
    elif choice == "T":
            with open("CoinCount.txt", 'r') as file:
                # Read the contents of the file
                file_contents = file.read()
                # Print the contents to the terminal
                print(file_contents)
    elif choice == "N":
        print()
        #start from top 
    elif choice == "E":
        print("Thank you for using coin counter")
        run = False
        exit()

    #sort
