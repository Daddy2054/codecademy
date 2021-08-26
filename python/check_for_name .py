# Write your check_for_name function here:
def check_for_name(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if str2 in str1:
        return True
    return False

# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False