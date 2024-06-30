#INVENTORY EXAMPLE PROJECT

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
print(inventory_len)

first = inventory[0]
print(first)

last = inventory[-1]
print(last)

inventory_2_6 = inventory[2:6]
print(inventory_2_6)

first_3 = inventory[0:3]
print(first_3)

twin_beds = inventory.count("twin bed")
print(twin_beds)

inventory.remove("king bed")
removed_item = "king bed"

print(inventory)

print(removed_item)

inventory.insert(10, "19th Century Bed Frame")

print(inventory)

inventory.sort(reverse = True)
print(inventory)

inventory_sorted = sorted(inventory)
print(inventory_sorted)




#PIZZA STORE EXAMPLE PROJECT

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"] 
print(toppings)

prices = [2, 6, 1, 3, 2, 7, 2]
print(prices)

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)
print(num_pizzas)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")

pizza_and_prices = [(2,	"pepperoni"), (6, "pineapple"), (1, "cheese"), (3, "sausage"), (2, "olives"), (7, "anchovies"), (2,	"mushrooms")]

pizza_and_prices.sort()

cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

priciest_pizza = pizza_and_prices[6]
print(priciest_pizza)

pizza_and_prices.pop(-1)

pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
