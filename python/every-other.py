# Write your every_other_letter function here:
def every_other_letter(word):
    word2 = ''
    i = 0; 
    for letter in word:
        if i % 2 == 0:
            word2 = word2 + letter
        i += 1 
    return word2

# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 