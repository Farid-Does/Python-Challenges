# Isogram exercise

string = input ().replace (" ", "")
s_dict = {}
for char in string:
    s_dict.setdefault (char, 0)

def is_isogram (string):
    for key in string:
        s_dict [key] += 1
    return all(v <= 1 for v in s_dict.values())

    
print ( is_isogram (string) )