# Write your code below this line 👇
def prime_checker(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
if prime_checker(n):
    print("It's a prime number.")
else:
    print("It's not a prime number.")
