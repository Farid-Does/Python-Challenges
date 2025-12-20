# darts exercise
from math import sqrt

while True:
    try:
        x = float(input("Enter the x coordinate of the dart: "))
        y = float(input("Enter the y coordinate of the dart: "))
        break

    except ValueError as e:
        print (e)


def distance_calculation (x, y):
    distance = sqrt ( x ** 2 + y ** 2 )
    return distance


def score ():
    distance = distance_calculation (x, y)
    if distance > 10:
        score = 0
    elif 5 < distance <= 10:
        score = 1
    elif 1 < distance <= 5:
        score = 5
    elif distance <= 1:
        score = 10

    return score


print (score () )














