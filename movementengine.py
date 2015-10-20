__author__ = 'lukaszlampart'

""" Object for simple collision detection with walls
"""
class rigid_obj:
    def __init__(self):
        self.x=0
        self.y=0
        self.velocityx=0
        self.velocityy=0

    def minx(self):
        return self.x

    def miny(self):
        return self.y

    def maxx(self):
        return self.x

    def maxy(self):
        return self.y

    """Methods handling collision ith other objects:
    they should be given the proper integer value of
    the size of "intersection" of two objects
    """

    def invx(self,overmove=0):
        self.x-=overmove
        self.velocityx=-self.velocityx


    def invy(self,overmove=0):
        self.y-=overmove
        self.velocityy=-self.velocityy


class mapMovement:
    def __init__(self,height=300,width=300):

        self.minx=0
        self.miny=0

        self.height=height
        self.width=width

        """Reduandant variables for cleaner code
        """
        self.maxx=self.minx+self.width
        self.maxy=self.miny+self.height


    """
    Method checking collision with bounds and signaling it to the colliding object
    """
    def check_collision_with_bounds(self,object=rigid_obj()) -> bool:
        flag =False
        if object.minx()<self.minx:
            object.velocityx=-object.velocityx
            object.invx(object.minx()-self.minx)
            flag=True

        if object.maxx()>self.maxx:
            object.velocityx=-object.velocityx
            object.invx(object.maxx()-self.maxx)
            flag=True

        if object.miny()<self.miny:
            object.velocityy=-object.velocityy
            object.invy(object.miny()-self.miny)
            flag=True

        if object.maxy()>self.maxy:
            object.velocityy=-object.velocityy
            object.invy(object.maxy()-self.maxy)
            flag=True

        return flag
