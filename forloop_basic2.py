# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(nums_list):
    for idx in range(len(nums_list)):
        nums_list[idx] > 0:
        nums_list[idx] = "big"
    return nums_list
    

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(nums_list):
    count = 0
    for idx in range(len(nums_list)):
        nums_list[idx] > 0:
        count += 1
    last_idx = len(nums_list)-1
    nums_list[last_idx] = count
    return nums_list    


# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sum_total(nums_list):
    sum = 0
for idx in range (len(nums_list)):
    sum += nums_list[idx]
    return sum

# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
def average(nums_list):
    sum = 0
for idx in range (len(nums_list)):
    sum += nums_list[idx]
    return sum/len(nums_list)


# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(nums_list):
    return len(nums_list)


# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(nums_list):
    if len(nums_list) == 0:
        return false
    else:
        min = nums_list[0]
        for idx in range (len(nums_list)):
            if nums_list[idx] < min:
            min = nums_list[idx]
    return min 
print(minimum([]))


# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(nums_list):
    if len(nums_list) == 0:
        return false
    else:
        max = nums_list[0]
    for idx in range (len(nums_list)):
        if nums_list[idx] < max:
            max = nums_list[idx]
    return max
print(maximum([]))


# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(nums_list):
    sum = sum_total(nums_list)
    avg = average(nums_list)
    min = minimum(nums_list)
    max = maximum(nums_list)
    len = length(nums_list)
    analysis = {
        'sumTotal': sum, 
        'average': avg, 
        'minimum' : min, 
        'maximum': max,
        'length': len, 
    }
    return analysis

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
