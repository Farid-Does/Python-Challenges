# Triangle

a = float ( input ("Enter side a: ") )
b = float ( input ("Enter side b: ") )
c = float ( input ("Enter side c: ") )

def is_triangle (a, b, c):
    return ( a + b >= c and a + c >= b and b + c >= a ) and all ( x > 0 for x in [a, b, c] )

def triangle_type (a, b, c):
    if a == b == c:
        result = "equilateral triangle"

    elif a != b and b != c and a != c:
        result = "scalene triangle"

    else:
        result = "isosceles triangle"
    
    return result

if is_triangle (a, b, c):
    print (triangle_type (a, b, c))
else:
    print ("these values can't form a triangle.")
