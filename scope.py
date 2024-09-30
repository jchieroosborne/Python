# Global constants for conversion
POUNDS_TO_KG = 0.453592
INCHES_TO_M = 0.0254

# Function to calculate BMI
def calculate_bmi(weight_pounds, height_inches):
    # Convert pounds to kilograms and inches to meters
    weight_kg = weight_pounds * POUNDS_TO_KG
    height_m = height_inches * INCHES_TO_M
    
    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)
    return bmi

# Function to classify the BMI into categories
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Main function to run the BMI calculator
def main():
    # Ask for user's weight and height
    weight_pounds = float(input("Enter your weight in pounds: "))
    height_inches = float(input("Enter your height in inches: "))

    # Calculate BMI
    bmi = calculate_bmi(weight_pounds, height_inches)
    
    # Output BMI with two decimal places
    print(f"Your BMI is: {bmi:.2f}")

    # Classify and display BMI category
    category = classify_bmi(bmi)
    print(f"BMI Category: {category}")

if __name__ == "__main__":
    main()