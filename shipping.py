# Ground Shipping:
weight = 1.5

if weight < 2: 
  cost = (weight * 1.50) + 20.00
elif weight <= 6:
  cost = (weight * 3.00) + 20.00
elif weight <= 10:
  cost = (weight * 4.00) + 20.00
else:
  cost = (weight * 4.75) + 20.00

print("Ground Shipping: $", cost)
# Ground Shipping Premium:

cost_of_premium_ground_shipping = 125.00
print("cost_of_premium_ground_shipping $", cost_of_premium_ground_shipping)

# Drone Shipping:
if weight < 2: 
  cost = (weight * 4.50) + 0.00
elif weight <= 6:
  cost = (weight * 9.00) + 0.00
elif weight <= 10:
  cost = (weight * 12.00) + 0.00
else:
  cost = (weight * 14.25) + 0.00

print("Drone Shipping: $", cost)
