
#https://docs.google.com/presentation/d/1HXwHscuCWSnif3IMF3dcyAKLTgfCOgUb/edit#slide=id.p14
#https://www.geeksforgeeks.org/python-sort-list-of-list-by-specified-index/
#read lines 
#split into list 
#split again 
#then sort 

with open('save_test.txt', 'r') as file:
    lines = file.readlines()
# Split lines into a list of lists based on whitespace (assuming space-separated values)
list_of_lists = [line.strip().split() for line in lines[1:]]  # Skip the header line

# Sort the list of lists by the accuracy column (assuming accuracy is the fourth column, index 3)
sorted_list_of_lists = sorted(list_of_lists, key=lambda x: float(x[3]), reverse=True)
# Display header
print(lines[0].strip())



# Display sorted content in the terminal
for row in sorted_list_of_lists:
    formatted_row = "{: <20} {: <20} {: <20} {: <20} {: <20} {: <20} {: <20} {: <10}".format(*row)
    print(formatted_row)


