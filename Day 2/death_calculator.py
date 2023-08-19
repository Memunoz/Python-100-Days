# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
age_int = int(age)
year = 90 - age_int
month = year*12
weeks = year*52
day = year*365
print(f"You have {day} days, {weeks} weeks, and {month} months left.")
