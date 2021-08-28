# Write your unique_values function here:
def unique_values(dict):
    unique = []
    for value in dict.values():
        if value not in unique:
            unique.append(value)
    return len(unique) 

# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1