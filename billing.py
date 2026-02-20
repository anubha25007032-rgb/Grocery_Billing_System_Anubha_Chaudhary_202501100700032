# Grocery Store Billing System using Python

# Step 1: Take input prices of 3 items from user
item1 = float(input("Enter price of Item 1: "))
item2 = float(input("Enter price of Item 2: "))
item3 = float(input("Enter price of Item 3: "))

# Step 2: Calculate total cost
total = item1 + item2 + item3

# Step 3: Check if discount applicable (10% if total > 50)
discount = 0
if total > 50:
    discount = total * 0.10   # 10% discount

# Step 4: Calculate final payable amount
final_amount = total - discount

# Step 5: Display bill details
print("\n------ Grocery Bill ------")
print("Original Total: $", round(total, 2))
print("Discount: $", round(discount, 2))
print("Final Amount to Pay: $", round(final_amount, 2))