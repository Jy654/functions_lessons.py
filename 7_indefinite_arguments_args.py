def tea_order(customer_name, tea_type, *args, **kwargs):
    print(customer_name, "ordered a", tea_type, "tea")
    for arg in args:
        print(" - Add", arg)
    for key, value in kwargs.items():
        print(" - Add", key, ":", value)

tea_order("Alice", "chamomile")
tea_order("Bob", "black", milk="oat")
tea_order("Tony", "black", milk="oat", sweetener="honey")

eves_extras = {"milk": "almond", "sweetener": "sugar", "flavor": "lemon"}






# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).
def sum_squares(*args):
    total=0 # initialize total to 0 
    for num in args: # iterate through each argument
        total += num ** 2 # square the number and add it to the total



    return total #retunhr the total sum of squares
print(sum_sqaures(1, 2, 3)) # example usage
print(sum_squares(4, 5, 6, 7, 8, 9)) # example usage

# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).
def absolute_sum(*args):
    total = 0 # initialize total to 0 
    for num in args: # iterate through each argument
        total += abs(num) # Add the absolute value of the number to total
        # first time through loop: total = 0 + abs(-1) = 1
        # second time through loop: total = 1 + abs(2) = 3
        # third time through loop: total = 3 + abs(-3) = 6


        return total # return the total sum of absolute values
print(absolute_sum(-1, 2, -3)) # example usage
print(absolute(-10, 20, -30, 40 -50)) # example usage
# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"