# Write your max_key function here:
def max_key(dict):
    maxkey = list(dict)[0]
    maxval = 0
    for key,value in dict.items():
        if value > maxval:
            maxkey = key
            maxval = value
    return maxkey        


# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"