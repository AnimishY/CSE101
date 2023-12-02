Departments = ['Toys', 'Clothes', 'Sporting', 'Stationary']
Discounts = {'Toys': 10, 'Clothes': 20, 'Stationary': 5}
GST_rates = {'Toys': 6, 'Clothes': 12, 'Sporting': 18}
Toys_Price_List = {'car': 9, 'teddy': 4, 'Lego': 50}
Clothes_Price_List = {'shirt': 9, 'shorts': 4, 'socks': 13, 'jacket': 40}
Sporting_Price_List = {'ball': 9, 'racquet': 4, 'bat': 13, 'shuttle': 12}
Stationary_Price_List = {'pencil': 9, 'scale': 13, 'pen': 20, 'erasure': 15}

Shopping_List = input("Enter shopping list: ")
expected_total = input("Enter expected total: ")

total_amount = 0

for item, quantity in Shopping_List:
    if item in Toys_Price_List:
        department = 'Toys'
        price = Toys_Price_List[item] * quantity
    elif item in Clothes_Price_List:
        department = 'Clothes'
        price = Clothes_Price_List[item] * quantity
    elif item in Sporting_Price_List:
        department = 'Sporting'
        price = Sporting_Price_List[item] * quantity
    elif item in Stationary_Price_List:
        department = 'Stationary'
        price = Stationary_Price_List[item] * quantity
    else:
        print(f"Item '{item}' not found in any department.")
        continue
    
    if department in Discounts:
        discount = Discounts[department]
        price -= price * discount / 100
    
    gst_rate = GST_rates.get(department, 0)
    gst_amount = price * gst_rate / 100
    
    total_amount += price + gst_amount

if total_amount == expected_total:
    print("Test case passed")
else:
    print("Test case failed")