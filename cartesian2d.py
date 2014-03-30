import math

def distance(x_start,y_start,x_fin,y_fin):
    delta_x = float(x_fin - x_start)
    delta_y = float(y_fin - y_start)
    return math.sqrt((delta_x * delta_x) + (delta_y * delta_y))

def slope(x_start,y_start,x_fin,y_fin):
    delta_x = float(x_fin - x_start)
    delta_y = float(y_fin - y_start)
    return (delta_y / delta_x)

def y_intercept(x_start,y_start,x_fin,y_fin):
    return (y_fin - x_fin * slope(x_start,y_start,x_fin,y_fin))

def x_intercept(x_start,y_start,x_fin,y_fin):
    return(-(y_intercept(x_start,y_start,x_fin,y_fin) / slope(x_start,y_start,x_fin,y_fin)))
