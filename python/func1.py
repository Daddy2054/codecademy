def contains(big_string, little_string):
  if little_string in big_string:
    return True
  else:  
    return False  

def common_letters(string_one, string_two):
  str1 = list(string_one)
  str2 = list(string_two)
  str3 = []
  for ch1 in str1:
    for ch2 in str2:
      if ch1 not in str3 and ch1 == ch2:
        str3.append(ch1)
  return str3      
        
#common_letters('banana', 'apple')        

def username_generator (first_name, last_name):
  if len(first_name) < 3 :
    if len(last_name) < 4:
      return first_name + last_name
    else:  
      return first_name + last_name[:4]
  elif len(last_name) < 4:
    return first_name[:3] + last_name
  return first_name[:3] + last_name[:4]

#username = username_generator (first_name, last_name)  

''' Now for the temporary password, they want the function to take 
the input user name and shift all of the letters by one to the right, 
so the last letter of the username ends up as the first letter and so forth. 
For example, if the username is AbeSimp, then the temporary password generated 
should be pAbeSim.'''

def password_generator(username):
    str1 = list(username)
    str2 = str1.pop()
    return str2 +''.join(str1)
    

print(password_generator('AbeSimp'))



