class Point:
    '''
    A custom data type representing a point
    '''
    x = 0
    y = 0


def find_area_of_rectangle(p1, p2):
    '''
    A function to calculate area of a rectangle defined
    by two points. Expects objects of Point class
    '''

    # Get the x and y coordinates of p1 and p2
    p1xcoord = p1.x
    p1ycoord = p1.y
    p2xcoord = p2.x
    p2ycoord = p2.y

    # Calculate the length of adjacent sides
    side1length = abs(p1xcoord - p2xcoord)
    side2length = abs(p1ycoord - p2ycoord)

    # Calculate the area of the rectangle
    area = side1length * side2length

    # Return the area
    return area


'''
Program to test the code
'''
p1 = Point()
p1x = input("Enter x coordinate of first point: \n")
p1y = input("Enter y coordinate of first point: \n")
p1.x = float(p1x)
p1.y = float(p1y)

p2 = Point()
p2x = input("Enter x coordinate of second point: \n")
p2y = input("Enter y coordinate of second point: \n")
p2.x = float(p2x)
p2.y = float(p2y)

print("The area is: " + str(find_area_of_rectangle(p1, p2)))