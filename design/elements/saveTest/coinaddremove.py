coin_info = {
    "1p": [356,3.56],
    "2p": [356,7.12],
    "5p": [235,2.35],
    "10p": [325,6.50],
    "20p": [250,5],
    "50p": [160,18],
    "£1": [175,8.75],
    "£2": [120,12]
}


coin_type = input("enter coin type")
volunteer_bag_weight = float(input("enter bag weight"))



# Check if the coin type is valid
if coin_type in coin_info:
  key = coin_info[coin_type]
  correct_bag_weight = key[0]
  coin_weight = key[1]
else:
    print("Please enter a valid coin type")
    exit()
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
print(correct_bag_weight)
print(coin_weight)
print()