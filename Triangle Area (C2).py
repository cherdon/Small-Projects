class Coordinate:
    '''
    A custom data type representing a point
    '''
    x = 0
    y = 0


def area_of_triangle(p1, p2, p3):
    '''
    A function to calculate area of a rectangle defined
    by two points. Expects objects of Point class
    '''

    # Get the x and y coordinates of p1 and p2
    p1xcoord = p1.x
    p1ycoord = p1.y
    p2xcoord = p2.x
    p2ycoord = p2.y
    p3xcoord = p3.x
    p3ycoord = p3.y

    # Calculate the length of sides
    side1length = ((p2.y - p1.y) ** 2 + (p2.x - p1.x) ** 2) ** 0.5
    side2length = ((p3.y - p1.y) ** 2 + (p3.x - p1.x) ** 2) ** 0.5
    side3length = ((p3.y - p2.y) ** 2 + (p3.x - p2.x) ** 2) ** 0.5
    s = (side1length + side2length + side3length)/2
    c = (s * (s - side1length) * (s - side2length) * (s - side3length)) ** 0.5
    return round(c,2)



'''
Program to test the code
'''
p1 = Coordinate()
p1.x = float(input("Enter x coordinate of first point: \n"))
p1.y = float(input("Enter y coordinate of first point: \n"))


p2 = Coordinate()
p2x = float(input("Enter x coordinate of second point: \n"))
p2y = float(input("Enter y coordinate of second point: \n"))


p3 = Coordinate()
p3x = float(input("Enter x coordinate of third point: \n"))
p3y = float(input("Enter y coordinate of third point: \n"))


print("The area is: " + str(area_of_triangle(p1, p2, p3)))