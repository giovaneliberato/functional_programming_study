

add_numbers = int.__add__

def combine_arrays(array1, array2, final_array=None):
    final_array = final_array or []

    if len(array1) == 0 and len(array2) == 0:
        return final_array

    final_array.append([array1[0], array2[0]])
    return combine_arrays(array1[1:], array2[1:], final_array)

def average_for_array(array):
    return average(total_for_array(array), len(array))

def average(total, count):
    return total / count

def total_for_array(array, current_sum=0):
    if len(array) == 0:
        return 0
    return reduce(add_numbers, array)

def pluck(array, attr):
    return map(get(attr), array)

def get(attr):
    return lambda item: item[attr]
