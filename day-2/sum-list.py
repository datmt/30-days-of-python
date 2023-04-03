def sum_list(numbers):
    # initialize a variable to store the sum
    total = 0

    # loop through the list and add each number to the total
    for number in numbers:
        total += number

    # return the final total
    return total


print("Sum of list from 1 to 5: " + str(sum_list([1, 2, 3, 4, 5])))
print("Sum of list from 5 to 10: " + str(sum_list([5, 6, 7, 8, 9, 10])))
