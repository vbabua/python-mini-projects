import random

roll_again = "Y"
min_value = 1
max_value = 6

while roll_again == "Y" or roll_again == "y":
    print("Rolling the dice......")
    print("Value of the roll is : ", end="")
    print(random.randint(min_value, max_value))
    roll_again = input("Roll again Y/N : ")
