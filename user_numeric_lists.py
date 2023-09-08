# import some standard modules first - how many can you make use of?
import math
import random
import statistics as stats


# TODO: import from local util_datafun_logger.py 

from util_datafun_logger import setup_logger


# TODO: Call the setup_logger function to create a logger and get the log file name

logger, logname = setup_logger(__file__)


# TODO: Create some shared data lists if you like - or just create them in your functions

# Create list1 - a fairly long (20 or more list of numbers)
list1 = [random.randint(0, 100) for _ in range(20)]

# Create listx representing 10 integer times
listx = list(range(10))

# Create listy representing 10 values/measurements read at those times
listy = [2 * x + random.uniform(-1, 1) for x in listx]

# TODO: define some custom functions

def quick_stats():
    logger.info(f"Songs played per hour: {list1}")
    logger.info(f"Range to 10: {listx}")

    mean = stats.mean(list1)
    median = stats.median(list1)
    mode = stats.mode(list1)

    stdev = stats.stdev(list1)
    variance = stats.variance(list1)

    logger.info(f"Song played mean:{mean}")
    logger.info(f"Songs played median:{median}")
    logger.info(f"Songs played mode: {mode}")
    logger.info("")

    logger.info(f"Songs played standard deviatoin: {stdev}")
    logger.info(f"Songs played variance: {variance}")


def correlation():
    logger.info(f"listx: {listx}")
    logger.info(f"listy: {listy}")

    correlations = stats.correlation(listx, listy)
    slope, intercept = stats.linear_regression(listx, listy)

    xmax =max(listx)
    newx = 15 
    newy = slope * newx + intercept

    logger.info(f"correlation between x and y: {correlations}")
    logger.info(f"The equation of the best fit line is: y = {slope}x + {intercept}")
    logger.info(f"We predict that when x = {newx}, y will be about {newy}")

def list_stats():
    
    min_1 = min(list1)
    max_1 = max(list1)
    total = len(list1)
    sum_1= sum(list1)
    average = stats.mean(list1)
    set_list = set(list1)
    sorted_list = sorted(list1)
    sorted_reversed = sorted(list1, reverse=True)

    logger.info(f"The men of list1 is {min_1}")
    logger.info(f"The max of list1 is {max_1}")
    logger.info(f"The sum of List is: {total}")
    logger.info(f"The average of list1 is {average}")
    logger.info(f"The set of List1 is : {set_list}")
    logger.info(f"The sorted list of list1 : {sorted_list}")
    logger.info(f"The reversed sorted list of list1: {sorted_reversed}")

def list_types(): 
    # Make a new short list named lst
    lst = [1, 2, 3, 4]

    # append() a single value to the list
    lst.append(5)
    logger.info(f'After append: {lst}')

    # extend() the list with a new list you pass in
    lst.extend([6, 7])
    logger.info(f'After extend: {lst}')

    # insert() at an index, insert a value
    lst.insert(3, 8)
    logger.info(f'After insert: {lst}')

    # remove(5) remove the number 5 from the list, if found (change 5 to a value in your list)
    lst.remove(5)
    logger.info(f'After remove: {lst}')

    # count(2) count how many times 2 appears in your list (if it doesn't, change 2 to a value in your list)
    count_2 = lst.count(2)
    logger.info(f'Number of times 2 appears: {count_2}')

    # sort()
    lst.sort()
    logger.info(f'After sort: {lst}')

    # sort(), with reverse=True to get them in descending order
    lst.sort(reverse=True)
    logger.info(f'After sort with reverse: {lst}')

    # copy()
    lst_copy = lst.copy()
    logger.info(f'Copy of lst: {lst_copy}')

    # pop() the first item off the top of the list/stack
    first_item = lst.pop(0)
    logger.info(f'First item popped: {first_item}')
    logger.info(f'After first pop: {lst}')

    # pop() the last time off the bottom of the list/stack
    last_item = lst.pop()
    logger.info(f'Last item popped: {last_item}')
    logger.info(f'After second pop: {lst}')

def transformation():
    # Create a list of numbers
    numbers = [1, 2, 3, 4, 5, 6]

    # Use the built-in filter() function to keep x such that x is less than 4
    filtered_numbers = list(filter(lambda x: x < 4, numbers))
    logger.info(f'Filtered numbers: {filtered_numbers}')

    # Use the built-in map() function to map each x to cube root of x
    cuberoots = list(map(lambda x: math.pow(x, 1/3), numbers))
    logger.info(f'Cube roots: {cuberoots}')

    # Use the built-in map() function to calculate the volume of a cube with a side equal to the value in your list
    volumes = list(map(lambda x: x * x * x, numbers))
    logger.info(f'Volumes: {volumes}')

    # Use a list comprehension to filter to get x (for each x in list1) if x is less than 4 or some other cutoff
    filtered_numbers = [x for x in list1 if x < 4]
    logger.info(f'Filtered numbers: {filtered_numbers}')

    # Use a list comprehension to triple each value in your list1, that is to get x*3 (for x in list1)
    tripled_numbers = [x * 3 for x in list1]
    logger.info(f'Tripled numbers: {tripled_numbers}')

    # Use a list comprehension to transform your numeric list into another numeric list using a transformation of your choice
    squared_numbers = [x * x for x in list1]
    logger.info(f'Squared numbers: {squared_numbers}')


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    logger.info("Calling quick stats ")
    quick_stats()

    logger.info("Calling correlation")
    correlation()

    logger.info("Calling list_stats")
    list_stats()

    logger.info("Calling list_types")
    list_types()

    logger.info("Calling transformatoin")
    transformation()


