#Using a simple  function
def area(radius):
    pie = 22/7
    return pie * (radius ** 2)

for i in range(10):
    radius = float(input(f"Enter radius of circle {i+1}: "))
    Area = area(radius)
    print(f"The area of circle {i+1} is {Area:.2f}")
