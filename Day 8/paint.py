# Write your code below this line 👇
def paint(test_h, test_w, coverage):
    num_cans = round(((test_h*test_w)/coverage)+0.5)
    print(f"You'll need {num_cans} cans of paint.")


# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.
# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

paint(test_h, test_w, coverage)
