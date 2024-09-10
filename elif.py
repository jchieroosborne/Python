age = int(input("Please enter your age: "))
    
    # The initial price
price = 0.0
    
    # price based on age
if age < 1:
        price = 0.00
elif age < 12:
        price = age * 1.00
elif age < 65:
        price = 16.95
else:
        price = 12.95
    
    # The result
print(f"The price of the buffet for your age is: ${price:.2f}")