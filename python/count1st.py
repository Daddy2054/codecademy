# Write your count_first_letter function here:
def count_first_letter(dict):
    count1st = {}
    for lastname in dict:
        if lastname[0] not in count1st:
            count1st[lastname[0]] = 0
        for name in dict[lastname]:
            count1st[lastname[0]] += 1
    return count1st
            
# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}