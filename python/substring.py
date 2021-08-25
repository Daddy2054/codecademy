# Write your substring_between_letters function here:
def substring_between_letters(word,start,end):
    s = word.find(start)
    e = word.find(end)
    if s < 0 or e < 0:
        return word
    else:
        return word[s+1:e] 


# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"