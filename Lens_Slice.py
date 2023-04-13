# Your code below:

toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)

print(f"We sell {num_pizzas} different kinds of pizza!")

# 2D list

pizza_and_prices = [
    [2, "peppeorni"],
    [6, "pineapple"],
    [1, "cheese"],
    [3, "sausage"],
    [2, "olives"],
    [7, "anchovies"],
    [2, "mushrooms"]
]

print(pizza_and_prices)


# Sorting and Slicing Pizzas

pizza_and_prices.sort()
print(pizza_and_prices)

# Cheapest Pizza
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

# Priciest Pizza
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

pizza_and_prices.pop()

# Add the new toppings
pizza_and_prices.insert(4, [2.5, "peppers"])


three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
