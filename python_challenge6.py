# raindrops exercise

while True:
    try:
        number = int ( input ("Enter a number: ") )
        break
    except ValueError as e:
        print (e)

def check_the_number (number):
    divisors = (3, 5, 7)

    if number % 3 == 0 and number % 5 != 0 and number % 7 != 0:
        result = "Pling"
    elif number % 5 == 0 and number % 3 != 0 and number % 7 != 0:
        result = "Plang"
    elif number % 7 == 0 and number % 3 != 0 and number % 5 != 0:
        result = "Plong"
    elif all ( number % n != 0 for n in divisors ):
        result = str (number)

    return result


print (check_the_number (number) )