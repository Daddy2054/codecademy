# Write your make_spoonerism function here:
def make_spoonerism( word1, word2):
    let1 = word1[0]
    let2 = word2[0]
    word1 = word1.strip(let1)
    word2 = word2.strip(let2)
    return let2 + word1 + ' ' + let1 + word2
# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a