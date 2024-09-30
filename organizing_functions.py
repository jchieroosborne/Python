def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)




def main():
    user_input = int(input("\nEnter a positive number: "))
    result = factorial(user_input)
    print(f'The factorial of {user_input} is {result}')

main()