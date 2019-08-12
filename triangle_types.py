# Enter the sides of a traingle and determine which type of triangle it is
# Isoceles triangle: Two sides are the same
# Scalene triangle: All sides are different
# Equilateral triangle: All sides are the same
a = int(raw_input("The length of side a = "))
b = int(raw_input("The length of side b = "))
c = int(raw_input("The length of side c = "))
 
if a != b and b != c and a != c:
        print("This is a scalene triangle")
elif a == b and b == c:
  print("This is an equilateral triangle, all sides are the same")
else:
  print("This is an isoceles triangle.")
