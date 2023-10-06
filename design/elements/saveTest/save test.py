# Define the data for the table as a list of lists
accuracy = 10
table_data = [["Name", "coin", "bag weight", "accuracy", "bags counted"]]

# File check
import os

file_path = "save_test.txt"

if os.path.exists(file_path):
    print("File exists")
else:
    print("File not found")
    with open("save_test.txt", "w") as file:
        # Write header row to the file
        formatted_header = "{: <20} {: <20} {: <20} {: <20} {: <10}".format(*table_data[0])
        file.write(formatted_header + "\n")
    print("New file has been created")

# Gather volunteer information
volunteer_name = input("Enter volunteer name: ")
coin_type = input("Enter coin type: ")
bag_weight = input("Enter bag weight: ")
bags_counted = 0

# Adding new line
new_person = [volunteer_name, coin_type, bag_weight, accuracy, bags_counted]
formatted_new_person = "{: <20} {: <20} {: <20} {: <20} {: <10}".format(*new_person)

# Append the new row to the file
with open("save_test.txt", 'a') as file:
    file.write(formatted_new_person + "\n")

print("Data has been added to the file.")