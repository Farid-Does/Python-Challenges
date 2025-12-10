# leap year exercise.

try:
    year = int ( input ("Enter the desired year: ") )
except:
    print ("invalid input (must be integer).")

def leap_year (year):
    return f"Yes, {year} is a leap year." if year % 4 == 0 else f"No, {year} is not a leap year."

print ( leap_year (year) )