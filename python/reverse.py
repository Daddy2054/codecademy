# Consider, that we are given a list with a name of given_array.
def insertion_sort(given_array):
    for j in range(1, len(given_array)):
        # Variable key represents the element under consideration.
        key = given_array[j]
        i = j - 1
        # While i is not exceeding the left boundary of a list
        # And the element, which has the index of i, is greater than key.
        while i >= 0 and given_array[i] > key:
            # "Shift" the elements upwards
            # as long as the condition remains True.
            # Note, that we are just copying an element with index i to the right by one position.
            given_array[i + 1] = given_array[i]
            i = i - 1
        # Insert key into the proper position.
        given_array[i + 1] = key
    return given_array

given_array = [34,4565,567,33,567,35,68,89,234,445,67,85,3,23,5]
print(insertion_sort(given_array))