#pre defs
import os
# Define the data for the table as a list of lists 
total_value = 0
table_data = [["Name", "coin", "bag weight", "accuracy","bags correct", "bags counted","total bags","total value"]]
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

#end pre defs 

# Gather volunteer information/ inputs
volunteer_name = input("Enter volunteer name: ")

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
    try:
        volunteer_bag_weight = float(input("Enter bag weight in grams: "))
        break
    except ValueError:
        print("Error please enter just the integer of the weight in grams")
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


# Variable check
print("bags correct:", bags_correct)
print("bags counted:", bags_counted)
print("volunteer bag weight:", volunteer_bag_weight)
print("correct bag weight", correct_bag_weight)
print("accuracy:", accuracy)
print("correct bag weight: ",correct_bag_weight)
print("coin weight: ",coin_weight)
print("old sum: ",old_sum)
print("new sum:",new_sum)
print("total value:",total_value)
print("total bags: ", total_bags)

# Adding new line
new_person = [volunteer_name, coin_type, volunteer_bag_weight, accuracy, bags_correct, bags_counted, total_bags ,total_value ]
formatted_new_person = "{: <20} {: <20} {: <20} {: <20} {: <20} {: <20} {: <20} {: <10}".format(*new_person)

# Append the new row to the file
with open("CoinCount.txt", 'a') as file:
    file.write(formatted_new_person + "\n")

print("Data has been added to the file.")