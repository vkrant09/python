#Using a parameterized function with return type:
def area_return_type_parameterized(radius, pie):
    area = pie * (radius ** 2)
    return area

pie = 22/7
for i in range(10):
    radius = float(input(f"Enter radius of circle {i+1}: "))
    Area = area_return_type_parameterized(radius, pie)
    print(f"The area of circle {i+1} is {Area:.2f}")
