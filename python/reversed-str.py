# Write your reverse_string function here:
def reverse_string(word):
    word2 = ''
    i = len(word) - 1
    while i >= 0:
        word2 = word2 + word[i]
        i -= 1
    return word2
# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print