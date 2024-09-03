#The Start of the code it will introduce itself and state that it will help calculate their monthly spending then add all the inputs together

print('\nHello! I am a calculator that will help you determine your monthly costs using data that you will provide!\n*Please state the amount in USD*\n\nLets get started\n')

#Defined Variables with user inputs

rent = float(input('What is your montly Housing cost?:'))
utilities = float(input('What is your montly averge on Utilities?:'))
gas = float(input('How much do you spend on Gasoline a week?:'))
groceries = float(input('How much do you spend on Groceries a week?:'))
healthcare = float(input('How much do you spend on Health Care every paycheck?:'))
personalcare = float(input('How much do you spend on Personal Care / Hygene products every month?:'))
clothing = float(input('If you purchase clothing every month please state how much you spend a month if you do not spend anything please input 0.:'))
debt = float(input('What is your Debt payment per month?:'))

#Condsidering most people know how much they spend a week on certain things and not a month we have to multiple their input to accomodate for the weeks in the month depending on the circumstances...

gas = (gas * 4)
groceries = (groceries * 4)
healthcare = (healthcare * 2)

#Calculations to provide the user with their monthly costs

Monthly_Costs = rent + utilities + gas + groceries + healthcare + personalcare + clothing + debt
Yearly_Costs = Monthly_Costs * 12
 
print(f'Your total Monthly cost is{Monthly_Costs: .2F}$ USD and your yearly cost is{Yearly_Costs: .2F}$ USD' )

