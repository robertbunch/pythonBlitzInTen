# List of grocery items with dictionaries containing item_type, price, and quantity
grocery_list = [
    {"item_name": "Apples", "price": 1.5, "quantity": 10},
    {"item_name": "Donut", "price": 1.4, "quantity": 6},
    {"item_name": "Milk", "price": 5.0, "quantity": 1},
    {"item_name": "Spaghetti", "price": 2.5, "quantity": 3},
    {"item_name": "Eggs", "price": 4.0, "quantity": 1}
]
money_on_hand = 35.0  # Initial amount of money on hand
cart = []  # List to store maximum purchase statements

def buy_item(item):
    price = item["price"]
    quantity = item["quantity"]
    global money_on_hand
    #buy if possible
    # item_total_price = price * quantity
    # if(money_on_hand > item_total_price):
    #     money_on_hand -= item_total_price
    #     cart.append(item)
    #buy as many as possible
    for i in range(quantity,0,-1):
        item_total_price = price * i
        if(money_on_hand > item_total_price):
            item["quantity"] = i
            money_on_hand -= item_total_price
            cart.append(item)
            break

for item in grocery_list:
    buy_item(item)

print("You were able to purchase")
for item in cart:
    print(f" {item['quantity']} {item['item_name']}")

print(f"Money leftover: {money_on_hand}")

