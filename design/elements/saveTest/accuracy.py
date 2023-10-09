volunteer_name = input("Enter volunteer name: ")
coin_type = input("Enter coin type: ")
volunteer_bag_weight = int(input("Enter bag weight: "))
bags_correct = 0  # Initialize bags_correct as an integer, not a string

# Define correct bag weights
correct_bag_weights = {
    "1p": 356,
    "2p": 356,
    "5p": 235,
    "10p": 325,
    "20p": 250,
    "50p": 160,
    "£1": 175,
    "£2": 120
}

# Check if the coin type is valid
if coin_type in correct_bag_weights:
    correct_bag_weight = correct_bag_weights[coin_type]
else:
    print("Please enter a valid coin type")
    exit()

bags_counted = 0

# Read file and update counts
with open("save_test.txt", 'r') as file:
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