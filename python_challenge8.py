# perfect numbers

while True:
    try:
        number = int ( input ("Enter a number:") )
        if number <= 0:
            raise ValueError ("Classification is only possible for positive integers.")
        break
    except ValueError as e:
        print (e)

def classify (number):
    total = 0
    for u in range (1, int (number/2+1)):
        if number % u == 0:
            total += u
    if total == number:
        result = "This is a Perfect number."
    elif total > number:
        result = "This is a Abundant number."
    else:
        result = "This is a Deficient number."

    return result

print ( classify (number) )


    