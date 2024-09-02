# Conversion Factor for Converting kgs into lbs (Line 2)
conversion_factor = 2.20462

# Variable kg that are defined (Lines 5-9)
kg_weight1 = 50
kg_weight2 = 135
kg_weight3 = 20
kg_weight4 = 47.7
kg_weight5 = 98.453

# Calculations for kgs into lbs (Lines 12-16)
lbsweight1 = kg_weight1 / conversion_factor
lbsweight2 = kg_weight2 / conversion_factor
lbsweight3 = kg_weight3 / conversion_factor
lbsweight4 = kg_weight4 / conversion_factor
lbsweight5 = kg_weight5 / conversion_factor

#Out put of kgs into lbs with the conversion factor
print('\nLets calculate Kilograms into Pounds.\n')
print(f'{kg_weight1} Kilograms is equal to{lbsweight1: .2F} Pounds')
print(f'{kg_weight2} Kilograms is equal to{lbsweight2: .2F} Pounds')
print(f'{kg_weight3} Kilograms is equal to{lbsweight3: .2F} Pounds')
print(f'{kg_weight4} Kilograms is equal to{lbsweight4: .2F} Pounds')
print(f'{kg_weight5} Kilograms is equal to{lbsweight5: .2F} Pounds\n') 