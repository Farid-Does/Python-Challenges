# reverse string

string = input ("Enter something: ")

def reverse_str (string):
    output = ''.join (reversed (string))
    return output

print ( reverse_str (string) )