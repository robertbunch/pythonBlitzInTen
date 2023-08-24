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
    #make variables for price and quantity to make things look a little neater
    price = item["price"]
    quantity = item["quantity"]

    #use the global key word or we can't use the money_on_hand variable in a function
    global money_on_hand

    #buy if possible
    item_total_price = price * quantity #to get the total, multiply price and quantity
    if(money_on_hand > item_total_price): #if you have enough money conditional
        money_on_hand -= item_total_price # update money by subtracting price of item * quantity
        cart.append(item) #update cart with the item
    #buy as many as possible
    # for i in range(quantity,0,-1): #looping down means starting at quantity, down to 0, and stepping by -1
    #     item_total_price = price * i # get the price of the quantity as you count down * price
    #     if(money_on_hand > item_total_price): # see above
    #         item["quantity"] = i #update item quantity to be what you can afford
    #         money_on_hand -= item_total_price #see above
    #         cart.append(item) #add to cart
    #         break #stop the loop because we found the max we can buy

for item in grocery_list:
    #call buy_item and send the item
    buy_item(item)

print("You were able to purchase")
for item in cart:
    print(f" {item['quantity']} {item['item_name']}")

print(f"Money leftover: {money_on_hand}")



