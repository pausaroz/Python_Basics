user_positive_integer = int(input("Enter a positive integer: "))

for i in range(1, user_positive_integer + 1):
    if user_positive_integer % i == 0:
        print(f"{i} is a factor of {user_positive_integer}")
