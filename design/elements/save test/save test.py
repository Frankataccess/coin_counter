# Define the data for the table as a list of lists
accuracy = 10
table_data = [
    ["Name", "coin", "bag weight", "accuracy"]]

# Open a file in write mode ('w')
  # Write the formatted row to the file
volunteer_name = input("enter volunteer name")
coin_type = input("coin type")
bag_weight = input("enter bag weight")
# Adding new line
new_person = [volunteer_name, coin_type, bag_weight, 100]
formatted_new_person = "{: <20} {: <20} {: <20} {: <10}".format(*new_person)  # Adjust width and alignment as needed

with open('save_test.txt', 'a') as file:  # Open the file in append mode
    file.write(formatted_new_person + "\n")  # Write the new formatted row to the file

#need to create accuracy variable and bags counted unique to the volunteer
#add bags counted collum