"""Create a BMI calculator, BMI which stands for Body Mass Index can be calculated using the formula:

BMI = (weight in Kg)/(Height in Meters)^2.
Write python code which can accept the weight and height of a person and calculate his BMI."""

def bmi(weight,height):
    """
    Calculate the Body Mass Index (BMI) using the given weight and height.
    Args:
        weight: a float representing the weight in kilograms
        height: a float representing the height in meters
    Returns:
        a float representing the BMI
    """
    result = weight/(height*height)
    return result


weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in m: "))

print(f"Your BMI is: {round(bmi(weight,height),2)}")