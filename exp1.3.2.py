#Using a parameterized function:
def area(radius, pie):
    return pie * (radius ** 2)

pie = 22/7
for i in range(10):
    radius = float(input(f"Enter radius of circle {i+1}: "))
    Area = area(radius, pie)
    print(f"The area of circle {i+1} is {Area:.2f}")
