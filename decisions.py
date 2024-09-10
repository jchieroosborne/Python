#Ask the user for their age
age = int(input("Please enter your age: "))

#Checking if the user can drive based on minimun learners permit age which is 15 years old in Illinois
if age >= 15:
    drive = True
else:
    drive = False

#Checking if the user can Vote
if age >= 18:
    vote = True
else:
    vote = False

#Checking if the user can buy Alcohol
if age >= 21:
    alcohol = True
else:
    alcohol = False

#Checking if the user can get a Senior Discount

if age >= 65:
    discount = True
else:
    discount = False

print('\nResults:\n')
print(f"Can drive: {'Yes' if drive else 'No'}")
print(f"Can vote: {'Yes' if vote else 'No'}")
print(f"Can buy alcohol: {'Yes' if alcohol else 'No'}")
print(f"Eligible for senior discount: {'Yes' if discount else 'No'}"'\n')
