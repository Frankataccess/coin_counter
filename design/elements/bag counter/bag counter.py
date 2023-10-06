# bag counter 
#read text file 
#if the name is the same then read the bags counted collumn and add one to the volunteer 
#else just add 1
# Name to search for
volunteer_name = "Charlie"

# Open the file in read mode ('r')
with open('save_test.txt', 'r') as file:
    found = False  # Initialize a flag to check if the name is found
    for line in file:
        if volunteer_name in line:
            found = True
            break  # Name found, no need to continue searching

if found:
    print(f"The name '{volunteer_name}' was found in the file.")
else:
    print(f"The name '{volunteer_name}' was not found in the file.")
