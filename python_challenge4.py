# collatz conjecture

while True:
    try:
        x = int ( input ("choose a number: ") )
        if x <= 0:
            raise ValueError ("only positive integers are allowed.")
        break
    
    except ValueError as e:
        print (e)


def is_even (n):
    return n % 2 == 0

def collatz (x):
    counter = 0
    while x != 1:
        if is_even (x):
            x /= 2
        else:
            x = 3 * x + 1
        counter += 1
    return f"{counter} rounds were performed."

print ( collatz (x) )