import math 

#ask user for coordinates
x1 = float(input("enter x1: "))
y1 = float(input("enter y1: "))
x2 = float(input("enter x2: "))
y2 = float(input("enter y2: "))

#solve the distance
distance = math.sqrt(math.pow(x2-x1, 2)+math.pow(y2-y1, 2))

#display the result
print("the distance is", distance)