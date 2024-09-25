def calculate_interest(principal_amount, interest_rate, investment_time):
    calculated_interest = principal_amount * (interest_rate / 100) * investment_time
    
    return calculated_interest

principal_amount = 1000  # Example principal amount
interest_rate = 5        # Example interest rate
investment_time = 3      # Example investment time in years

result = calculate_interest(principal_amount, interest_rate, investment_time)

print(f"The simple interest for a principal amount of ${principal_amount:,.2f} \
                at an interest rate of {interest_rate}% over a period of \
                {investment_time} years is: ${result:,.2f}")
