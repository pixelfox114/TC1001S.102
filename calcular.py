import math

def triangle(b, a):
    area = round((b * a) / 2,2)
    perimeter = round(b + a + math.sqrt(b**2 + a**2),2)
    return area, perimeter

def circle(r):
    area = round(math.pi * (r ** 2),2)
    circumference = round(2 * math.pi * r,2)
    return area, circumference

def rectangle(b, a):
    area = round((b * a),2)
    perimeter = round(2 * (b + a), 2)
    return area, perimeter

