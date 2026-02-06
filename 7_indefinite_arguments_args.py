# def tea_order(customer_name, tea_type, *args, **kwargs):
#     print(customer_name, "ordered a", tea_type, "tea")
#     for arg in args:
#         print(" - Add", arg)
#     for key, value in kwargs.items():
#         print("  - Add", key, ":", value)
# tea_order("Alice", "chamomile")
# tea_order("Bob", "black", milk="oat")
# tea_order("Tony", "black", milk="oat", sweetener="honey")
# eves_extras = {"milk": "almond", "sweetener": "sugar", "flavor": "Lemon"}

# tea_order("Eve", "green", milk="almond", sweetener="sugar", flavor="lemon")
# tea_order("Eve", "Green", eves_extras)
# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.
def sum_squares(*args):
    total = 0 # Initialize total to 0
    for num in args: # Iterate through each argument
        total += num **2 # Add the square of the number to total
        # first time through loop: total = 0 + 1^2  = 1



    return total
print(sum_squares(1, 2, 3))
print(sum_squares(4, 5, 6, 7, 7 , 8, 9))    
# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).

# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).
def absolute_sum(*args):
    total = 0 # Initialize total to 0
    for num in args: # Iterate through each argument
        total += abs(num) # Add the absolute value of the number to total
        # first time through loop: total = 0 + abs(-1) = 1
        # second time through loop: total = 2 + abs(2) = 3
        # third time through loop: total = 3 + abs(-3) = 6



    return total # Return the total sum of absolute values
print(absolute_sum(-1, 2, -3))
print(absolute_sum(-10, 20, -30, 40, -50))
# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"
def personal_numbers(name, *args):
    sum = 0
    for num in args:
        sum += num
    return f"{name}, the sum of your numbers is {sum}"
"{Tito}"
