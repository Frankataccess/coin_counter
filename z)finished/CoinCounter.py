#pre defs
import os

# Define the data for the table as a list of lists 
total_value = 0
table_data = [["Name", "coin", "bag weight", "accuracy","bags correct", "bags counted","total bags","total value"]]

# File check

file_path = "CoinCount.txt"

if os.path.exists(file_path):
    print("File exists")
else:
    print("File not found")
    with open("CoinCount.txt", "w") as file:
        # Write header row to the file
        formatted_header = "{: <20} {: <20} {: <20} {: <20} {: <20} {: <20} {: <20} {: <10}".format(*table_data[0])
        file.write(formatted_header + "\n")
    print("New file has been created")

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


# Define correct bag weights
coin_info = {
        "1p": [356,3.56,1],
        "2p": [356,7.12,1],
        "5p": [235,2.35,5],
        "10p": [325,6.50,5],
        "20p": [250,5,10],
        "50p": [160,18,10],
        "£1": [175,8.75,20],
        "£2": [120,12,20]
    }
        # Initialize the sum to 0
old_sum = 0
old_total_bags = 0





#end pre defs

while  True:
    
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
        # Gather volunteer information/ inputs
        while True:
            volunteer_name = input("Enter volunteer name: ")
            if volunteer_name.isalpha() ==True or volunteer_name.isupper() == True:
                if len(volunteer_name) < 15:
                   break
                else:
                    print("Please enter a shorter name")
            else:
                print("Please enter a valid name with only letters")

        #coin type check

        while True:
            print("Valid coin types: 1p , 2p , 5p , 10p , 20p , 50p , £1 , £2 ")
            coin_type = input("Enter coin type: ")
        
            # Check if the coin type is valid
            if coin_type in coin_info:
                key = coin_info[coin_type]
                correct_bag_weight = key[0]
                coin_weight = key[1]
                new_sum = key[2]
                total_value = old_sum + new_sum
                total_bags = old_total_bags + 1
                break
            else:
                print("Please enter a valid coin type")
            
        #volunteer bag weight check
        while True:
            volunteer_bag_weight = str(input("Enter bag weight in grams: "))
            if len(volunteer_bag_weight) > 3:
                print("Please enter a valid bag wieght")
            else:
                try:
                    volunteer_bag_weight = float(volunteer_bag_weight)
                    break
                except ValueError:
                    print("Error please enter just the integer of the weight to the nearest grams")
        bags_correct = 0

        #bag counter 
        with open("CoinCount.txt", 'r') as file:
            for line in file:
                # Split the line into columns
                columns = line.strip().split()
                # Check if the name exists in the first column
                if columns[0] == volunteer_name :
                    bags_counted = int(columns[5]) + 1
                    break
            else:
                # If the loop completes without finding the name
                bags_counted = 1
            
        #old sum
        with open('CoinCount.txt', 'r') as file:

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
                old_sum += int(values[7])
                old_total_bags = int(values[6])

        #accuracy


        #is bag too heavy or light?
        if volunteer_bag_weight > correct_bag_weight:
            remove_coin = (volunteer_bag_weight - correct_bag_weight) / coin_weight
            remove_coin= round(remove_coin)
            print("you need to remove ",remove_coin," coins")
        elif volunteer_bag_weight < correct_bag_weight:
            remove_coin = (correct_bag_weight - volunteer_bag_weight) / coin_weight
            remove_coin= round(remove_coin)
            print("you need to add ",remove_coin," coins")
        else: 
            print("perfect")

        bags_counted = 0

        # Read file and update counts
        with open("CoinCount.txt", 'r') as file:
            for line in file:
                columns = line.strip().split()
                if columns[0] == volunteer_name:
                    bags_counted = int(columns[5]) + 1
                    bags_correct = int(columns[4])
                    if volunteer_bag_weight == correct_bag_weight:
                        bags_correct += 1
                    break
            else:
                # If the name is not found, initialize counts
                bags_counted = 1
                if volunteer_bag_weight == correct_bag_weight:
                    bags_correct = 1

        # Calculate accuracy
        if bags_counted != 0:
            accuracy = (bags_correct / bags_counted) * 100
        else:
            accuracy = 0




        # Adding new line
        new_person = [volunteer_name, coin_type, volunteer_bag_weight, accuracy, bags_correct, bags_counted, total_bags ,total_value ]
        formatted_new_person = "{: <20} {: <20} {: <20} {: <20} {: <20} {: <20} {: <20} {: <10}".format(*new_person)

        # Append the new row to the file
        with open("CoinCount.txt", 'a', encoding='utf-8') as file:
            file.write(formatted_new_person + "\n")

        print("Data has been added to the file.")
                #start from top 
    elif choice == "X":
        print("Thank you for using coin counter")
        break
        exit()


