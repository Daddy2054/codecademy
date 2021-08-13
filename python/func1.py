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
  return str(str3)      
        
common_letters('banana', 'apple')        