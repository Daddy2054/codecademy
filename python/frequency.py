# Write your frequency_dictionary function here:
def frequency_dictionary(strings_list):
    dict = {}
    for i in range(0,len(strings_list)):
        if strings_list[i] in list(dict):
            dict[strings_list[i]] += 1
        else:
            dict[strings_list[i]] = 1    
    return dict

# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}