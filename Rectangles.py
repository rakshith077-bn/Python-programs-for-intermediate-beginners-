class Point:

    class Rectangle:

        def find_center(rect):
            p=Point()
            p.x = rect.corner.x + rect.width/2
            p.y = rect.corner.y + rect.height/2 
            return p
    
    def resize(rect, w, h):
        
        rect.width +=w
        rect.height +=h
    
    def print_point(p):
        
        print("(%g,%g)"%(p.x, p.y))
        box = Rectangle() #create Rectangle object
        box.corner=Point() #define an attribute corner for box
        box.width=100 #set attribute width to box
        box.height=200 #set attribute height to box
        box.corner.x=0 #corner itself has two attributes x and y
        box.corner.y=0 #initialize x and y to 0
        print("Original Rectangle is:")
        print("width=%g, height=%g"%(box.width, box.height))
        
        center = find_center(box)
        print("The center of rectangle is:")
        print(center)
        
        resize(box,50,70)
        print("Rectangle after resize:")
        print("width=%g, height=%g"%(box.width, box.height))
        
        center = find_center(box)
        print("The center of resized rectangle is:")
        print(center)