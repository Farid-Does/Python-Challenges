# Bob exercise

string = input("what do you want? ").rstrip()

def bob(string):
    if len(string) == 0:
        answer = "Fine. Be that way!"
    elif string.isupper() and string.endswith("?"):
        answer = "Calm down, I know what I'm doing!"
    elif string.isupper():
        answer = "Whoa, chill out!"
    elif string.endswith("?"):
        answer = "Sure."
    else:
        answer = "Whatever."

    return answer

print(bob(string))
