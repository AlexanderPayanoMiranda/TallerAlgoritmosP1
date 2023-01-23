import math

AB = float(input())
BC = float(input())

result = round(math.degrees(math.atan(AB/BC)))

print(result, end=chr(176))