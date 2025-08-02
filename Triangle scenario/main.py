from triangle import Triangle
def main():
    # Create an instance of Triangle with sides 3, 4, and 5
    triangle = Triangle(3, 4, 5)
    
    # Calculate the area of the triangle
    area = triangle.area()
    
    # Print the area
    print(f"The area of the triangle is: {area}")