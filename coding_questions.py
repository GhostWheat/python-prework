# Python Week 2 Coding Questions


# Q1: Write a function to print "hello_USERNAME!"
# USERNAME is the input of the function.
def hello_name(user_name):
    '''Prints a short hello and underscore, prepended to
 the passed argument.'''
    print('hello_'+user_name)


# Q2: Write a python function, first_odds that prints the odd numbers
# from 1-100 and returns nothing
def first_odds():
    '''Prints the odd numbers from 1 to 100, inclusive.'''
    for num in range(1,101):
        if num % 2 == 0:
            continue
        else:
            print(num)


# Q3: Please write a Python function, max_num_in_list to return
# the max number of a given list.
def max_num_in_list(a_list):
    '''For any given list argument containing only numbers,
 this returns the max number in that list'''
    return sorted(a_list, reverse=True)[0]


# Q4: Write a function to return if the given year is a leap year.
# A leap year is divisible by 4, but not divisible by 100, unless it
# is also divisible by 400.
# The return should be boolean Type (true/false).
def is_leap_year(a_year):
    '''Returns whether the argument is a leap year or not.'''
    if a_year % 400 == 0:
        return True
    elif a_year % 100 == 0:
        return False
    elif a_year % 4 == 0:
        return True
    else:
        return False

# Q5: Write a function to check to see if all numbers in list are
# consecutive numbers. For example, [2,3,4,5,6,7] are consecutive
# numbers, but [1,2,4,5] are not consecutive numbers.
# The return should be boolean Type.
def is_consecutive(a_list):
    '''This function takes a list of numbers, and returns True if all
 numbers in the list are one up or one down from the number right before.
  If any two numbers next to each other on the list are more than 1 apart
  in value, the program returns False.'''
    next_num_val = -1
    for index, sel_num_val in enumerate(a_list):
        # If index of currently-selected number in list is less than
        # index of last number on list, grab the value of following num.
        if index < len(a_list)-1:
            next_num_val = a_list[index+1]
        else:
            # If index reaches last number on list, it found no non-
            # consec numbers and will exit, returning True.
            return True
        # print(index,sel_num_val, next_num_val) # This line for testing
        if sel_num_val - next_num_val == 1 or sel_num_val - next_num_val == -1:
            continue
        else:
            return False