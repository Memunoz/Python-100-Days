# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

height_int = float(height)
weight_int = int(weight)

bmi = weight_int / (height_int ** 2)
bmi_round = round(bmi)


def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Slightly overweight"
    elif bmi < 35:
        return "Obese"
    else:
        return "Clinically obese"


print(f"Your BMI is {bmi_round}, you are {interpret_bmi(bmi)}.")
