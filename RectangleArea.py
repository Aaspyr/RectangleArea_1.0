print("Program calculate the area of the rectangle")
pole = False
while not pole:
    a = int(input("Write length side a: "))
    b = int(input("Write length side b: "))
    p = a*b
    if (p > 0):
        print ("Area of the rectangle: ", p)
        pole = True
    else:
        print ("Write correct data!")
