# Write your values_that_are_keys function here:
def values_that_are_keys(dict):
    values_keys = []
    for value in dict.values():
        for key in dict:
            if key == value:
                values_keys.append(value)
    return values_keys        

# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]