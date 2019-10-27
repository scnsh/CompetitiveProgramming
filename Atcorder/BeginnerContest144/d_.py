import math

a, b, x = map(int, input().split())

if a*a*b/2 > x:
    theta = math.atan((2*x)/(b*b*a))
    print(90 - math.degrees(theta))
else:
    theta = math.atan((2*(a*a*b-x))/(a*a*a))
    print(math.degrees(theta))
