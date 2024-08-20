#Create BMI Calculator
#BMI = weight(kg) / (height(m) * height(m))

weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in m: "))
BMI = weight/(height*height) #or BMI = weight/height**2

print(f"Your BMI is: {BMI}")

