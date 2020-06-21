print("Enter number is geometric figure.Circle-1.Rectangle-2.Triangle-3")
figura=int(input())
if (figura>=1) and (figura<=3):
    if figura==1:
        radius=int(input("Enter radius: "))
        area=3.14*radius**2
    elif figura==2:
        side_A=int(input("Enter side A: "))
        side_B=int(input("Enter side B: "))
        area=side_A*side_B
    elif figura==3:
        side=int(input("Enter side of the triangle: "))
        area= side**2*1.73/4
    print("Area of the figure: ",area)    
else:
    print("incorect number!")