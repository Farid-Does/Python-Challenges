# ISBN verifier

string = input("Enter your string: ")

def is_isbn10(string):
    string = string.replace('-', '')
    digits = string[0:-1]
    last_char = string[-1]

    format_conditions = (
        len(string) == 10
        and digits.isdigit()
        and (last_char.isdigit() or last_char == "X")
    )

    if not format_conditions:
        return False

    if last_char == "X":
        last_value = 10
    else:
        last_value = int(last_char)

    total = sum(int(digits[i]) * (10 - i) for i in range(9)) + last_value * 1

    return total % 11 == 0


    