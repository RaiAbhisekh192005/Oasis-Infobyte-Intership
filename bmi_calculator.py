def calculate_bmi(weight, height_cm):
    """Calculate BMI given weight in kilograms and height in centimeters."""
    height_m = height_cm / 100  # Convert height from cm to meters
    bmi = weight / (height_m ** 2)
    return bmi

def get_bmi_category(bmi):
    """Determine the BMI category based on the BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height_cm = float(input("Enter your height in centimeters: "))
        
        bmi = calculate_bmi(weight, height_cm)
        category = get_bmi_category(bmi)
        
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")
        
    except ValueError:
        print("Please enter valid numbers for weight and height.")

if __name__ == "__main__":
    main()

