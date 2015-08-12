

def total_for_array(array, current_sum=0):
    if len(array) == 0:
        return current_sum
    return total_for_array(array[1:], current_sum) + array[0]
