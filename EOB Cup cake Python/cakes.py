def find_smallest(array):
    smallest = array[0]

    for count in range(len(array)):
        if array[count] < smallest:
            smallest = array[count]
    
    return smallest



def average(array):
    total = 0
    for count in range(len(array)):
        total += array[count]
    average = total / len(array)
    return average



def occurrence(array, number):
    count_occurrence = 0
    for count in range(len(array)):
        if array[count] == number:
            count_occurrence += 1
    return count_occurrence



def contains_element(array, number):
    for count in range(len(array)):
        if array[count] == number:
            return True
    return False








numbers = [10, 20, 30, 40, 50, 20, 10, 80, 90]

print("Smallest:", find_smallest(numbers))
print("Average:", average(numbers))
print("Occurrence of 20:", occurrence(numbers, 20))
print("Contains 100?", contains_element(numbers, 100))
