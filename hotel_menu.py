menu={
    "pizza": 50,
    "burger": 70,
    "coffee": 80,
    "full meal": 120,
    "ice cream": 45
}

print("WELCOME TO OUR RESTAURANT.......")
print("pizza: Rs50\nburger: Rs70\ncoffee: Rs80\nfull meal: Rs120\nice cream: Rs45")

total_order=0

item_1=input("Enter your order: ")
if item_1 in menu:
    print("your order has been plced.")
    total_order +=menu[item_1]
else:
    print(f"This item {item_1} is not in the menu.")    

another_order=input("Do you want to order something else too (yes/no): ")
if another_order=="yes":
    item_2=input("Enter your order: ")
    if item_2 in menu:
        print("your order has been plced.")
        total_order +=menu[item_2]
    else:
        print(f"This item {item_2} is not in the menu.")

print(f"Your total bill is {total_order}")