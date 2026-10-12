# Announcements:
# * Quiz 3 will be this Friday, October 16
#   * practice questions will be discussed Wednesday October 14
# * Lab 7 will become Lab 7 and Lab 8a
import random
import time

# Today's topic: searching (and maybe sorting)
def searching(goal_number):
    #number_list = [1, 2, 7, 19, 21, 29, 62, 91]
    number_list = [random.randint(1,200) for _ in range(100000)]

    # if number_list was sorted, could I do a sequential search any faster?
    # * I could do a binary search (more on this later)
    # * I could quit as soon as I know the number isn't in there, which
    #   may be earlier in a sorted list than an unsorted list...

    start_time = time.perf_counter_ns()
    # Search for the number x:
    
    for index, value in enumerate(number_list):
        # Basic operation to count: comparison
        if value == goal_number:
            #return index
            break
        elif goal_number < value:
            #return None
            break
    
    '''
    index = 0
    while index < len(number_list):
        if number_list[index] == goal_number:
            break
        index = index + 1
    '''

    #return None
    return time.perf_counter_ns() - start_time

def binary_search_recursive(number_list, goal_number):
    if len(number_list) == 0:
        return False
    elif len(number_list) == 1 and number_list[0] == goal_number:
        return True
    else:
        midpoint = len(number_list) // 2

        if number_list[midpoint] == goal_number:
            return True
        elif number_list[midpoint] < goal_number:
            return binary_search_recursive(number_list[midpoint+1:], goal_number)
        else:
            return binary_search_recursive(number_list[0:midpoint], goal_number)


def binary_search_iterative(number_list, goal_number):
    left = 0
    right = len(number_list) - 1

    while left <= right:
        midpoint = (right + left) // 2

        # If you've found the number, return the index
        if number_list[midpoint] == goal_number:
            return midpoint
        elif number_list[midpoint] < goal_number:
            left = midpoint
        else:
            right = midpoint

    return None


if __name__=='__main__':
    # Best case searching: 1 -- item is first element in list
    # Worst case searching: n -- item is not in list (or last thing in list)
    # Avg case searching: n/2
    #searching()

    '''
    total_time = 0
    for _ in range(100):
        total_time = total_time + searching(random.randint(1,200))

    # One takeaway: for loops execute faster in Python than while loops
    print("Average time:", (total_time / 100))
    '''

    # What if I use an "early exit" strategy with a sorted list?
    # Best case: 1 -- item is first element in list
    # Worst case: n -- item is not in list and number you're searching for is "big"
    # "early exit" only seems to help if the item is *not* in the list and
    # it isn't too "big"

    # What if we know the list is sorted and want faster than O(n)?
    # **binary search** can be quite fast (O(log n)) provided the list
    # is sorted!
    # * for n = 1024, log n = 10 -- log grows really slow
    number_list = [random.randint(1,200) for _ in range(100000)]
    number_list.sort()

    start_time = time.perf_counter_ns()
    #binary_search_recursive(number_list, random.randint(1,200))
    print(binary_search_iterative(number_list, random.randint(1,200)))
    #print(searching(random.randint(1,200)))
    print(time.perf_counter_ns() - start_time)