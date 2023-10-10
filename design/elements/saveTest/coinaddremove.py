volunteer_bag_weight = int(input("enter bag weight"))
coin_type = input("enter coin type")

coin_weights = {
    "1p": 3.56,
    "2p": 7.12,
    "5p": 2.35,
    "10p": 6.50,
    "20p": 5,
    "50p": 18,
    "£1": 8.75,
    "£2": 12
}
for coin_type in coin_weights:
    coin_weight = coin_weights[coin_type]

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
#is bag too heavy or light?
if volunteer_bag_weight > correct_bag_weight:
    remove_coin = (volunteer_bag_weight - correct_bag_weight) / coin_weight
elif volunteer_bag_weight < correct_bag_weight:
    print()
else:
    print()
print(correct_bag_weight)