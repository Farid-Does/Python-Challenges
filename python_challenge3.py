# grains problem

while True:
    try:
        square_index = int ( input ("Enter the square number: ") )
        if 1 <= square_index <= 64:
            break
        else:
            raise ValueError ("square must be between 1 and 64")
        
    except ValueError as e:
        print (e)

# returns two values : the amount of grains in the desired square and all of them.
def number_of_grains (square_index):
    square_grains = 2 ** (square_index - 1)
    square_grains_copy = square_grains
    whole_grains = square_grains

    while square_grains > 1:
        square_grains /= 2
        whole_grains += square_grains

    return f"square grains : {square_grains_copy}  whole grains : {int(whole_grains)}"

print (number_of_grains (square_index))