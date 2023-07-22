#Using a function with return type
def area_return_type(radius):
    pie = 22/7
    area = pie * (radius ** 2)
    return area

for i in range(10):
    radius = float(input(f"Enter radius of circle {i+1}: "))
    Area = area_return_type(radius)
    print(f"The area of circle {i+1} is {Area:.2f}")
