# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
number_item = len(names)
random_choice = random.randint(0, number_item - 1)
pay_bill = names[random_choice]
print(pay_bill+" will pay the bill")
