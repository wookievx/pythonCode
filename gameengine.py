__author__ = 'lukaszlampart'

from tkinter import *
import movementengine
import math3d as m3d

class BasicActor(movementengine.rigidObj):
    def __init__(self,radius=5,startx=0,starty=0,startvx=0,startvy=0):
        movementengine.rigidObj.__init__(self)
        self.radius=radius
        self.x=startx
        self.y=starty
        self.velocityx=startvx
        self.velocityy=startvy

    def minx(self):
        return self.x-self.radius

    def miny(self):
        return self.y-self.radius

    def maxx(self):
        return self.x+self.radius

    def maxy(self):
        return self.y+self.radius

class PlayerChar(BasicActor):
    def __init__(self,radius=5,startx=0,starty=0,startvx=0,startvy=0):
        BasicActor.__init__(self,radius,startx,starty,startvx,startvy)
        self.leftRot=m3d.Orientation.new_rot_z(3.14/4)
        self.rightRot=m3d.Orientation.new_rot_z(6.28 - 3.14/4)

    @property
    def speedVal(self):
        return m3d.Vector(self.velocityx,self.velocityy,0).length

    @property
    def rightArmLine(self):
        return self.leftRot * m3d.Vector(self.velocityx/self.speedVal*self.radius*2,self.velocityy/self.speedVal*self.radius*2,0)

    @property
    def leftArmLine(self):
        return self.rightRot * m3d.Vector(self.velocityx/self.speedVal*self.radius*2,self.velocityy/self.speedVal*self.radius*2,0)

    def rot(self,angle=0):
        rot=m3d.Orientation.new_rot_z(angle)
        v=rot * m3d.Vector(self.velocityx,self.velocityy,0)
        self.velocityx=v[0]
        self.velocityy=v[1]

    def setVelocity(self,x,y):
        if self.x==x or self.y==y:
            self.velocityx=0
            self.velocityy=0
            return

        vector1=m3d.Vector(x-self.x,y-self.y,0)
        if vector1.length<self.radius:
            vec=vector1.normalized
            self.velocityx=vec[0]*10
            self.velocityy=vec[1]*10
        else:
            vec=vector1.normalized
            self.velocityx=(10-min(10,vector1.length/30))*vec[0]
            self.velocityy=(10-min(10,vector1.length/30))*vec[1]

        if self.velocityx==0 and self.velocityy==0:
            self.velocityx=vec[0]/10
            self.velocityy=vec[1]/10


class Game:
    def __init__(self, iheight=300, iwidth=300, bgcolor="black"):
        """part of engine behind graphics
        """
        self.root = Tk()
        self.RUN = False
        """Main frame of the game (window)
        """
        self.frame = Frame(bg=bgcolor)
        self.frame.pack()

        """
        Label
        """
        self.label=Label(self.root,text="Game")
        self.label.pack()

        self.vlabel=Label(self.root,text="Velocity:")
        self.vlabel.pack()
        """paramters of the window of the game loaded from the config file
        """
        self.height=iheight
        self.width=iwidth

        self.x=int(0)
        """Canvas drawing graphics of the game
        """
        self.canvas = Canvas(self.frame, bg=bgcolor,width=self.width,height=self.height)
        self.canvas.pack()

        """movement handler object
        """
        self.moveEngine=movementengine.mapMovement(self.height, self.width)
        """ list of images imported into the game
        dictionary could be another and probably better option"""
        self.image=[]

        """ list of moving objects in game physics interaction are performed for each of them
        """
        self.objects=[]

        self.button=Button(self.frame,bg="black",fg="white",text="Click to lock and load",command=self.init)
        self.button.pack()

        self.player=PlayerChar(30,200,200,2,1)
        self.points=int(0)
        self.root.mainloop()

    def loadImage(self):
        self.image.append(PhotoImage(file="graphics/game_graph.gif"))
        self.image.append(PhotoImage(file="graphics/j3R4B.gif"))

    def onMouseC(self,event):
        self.player.setVelocity(event.x,event.y)
        self.food=(event.x,event.y,10)

    def init(self):
        if self.RUN is False:
            """set of food drawn by the game"""
            self.food=(0,0,0) # last placed piece of food
            self.loadImage()
            self.canvas.bind("<ButtonPress-1>", self.onMouseC)
            self.vlabel['text']="velocity: " + str(self.player.speedVal)
            self.label['text']="Points: " + str(self.points)
            self.RUN=True
            self.objects.append(BasicActor(20,self.width/2,self.height/2,1,0.5))
            self.objects.append(BasicActor(40,self.width/3,self.height/3,0.5,0.5))
            self.objects.append(self.player)
            self.run()

    def paint(self):
        self.canvas.delete(ALL)
        self.canvas.create_image(self.width/2,100,image=self.image[0])
        self.canvas.create_line(self.player.x,self.player.y,self.player.x+self.player.rightArmLine[0],self.player.y+self.player.rightArmLine[1],fill="blue",width=5)
        self.canvas.create_line(self.player.x,self.player.y,self.player.x+self.player.leftArmLine[0],self.player.y+self.player.leftArmLine[1],fill="blue",width=5)
        if self.food != (0,0,0):
            self.canvas.create_oval(self.food[0]-self.food[2],self.food[1]-self.food[2],self.food[0]+self.food[2],self.food[1]+self.food[2],fill="orange")
        for actor in self.objects:
            self.canvas.create_oval(actor.minx(),actor.miny(),actor.maxx(),actor.maxy(),fill="red")


    def eraseFood(self):
        if self.food!=(0,0,0) and m3d.Vector(self.player.x-self.food[0],self.player.y-self.food[1]).length<self.player.radius+self.food[2]:
            self.food=(0,0,0)
            self.points+=1

    def end(self):
        self.RUN=False
        self.canvas.unbind("<ButtonPress-1>")

    def run(self):
        if self.RUN is True:
            self.root.after(10,self.run)
            self.eraseFood()
            for actor in self.objects:
                self.moveEngine.check_collision_with_bounds(actor)
            self.moveActors()
            self.vlabel['text']='velocity: ' + str(self.player.speedVal)
            self.label['text']='points: ' + str(self.points)
            self.paint()

    def moveActors(self):
        for actor in self.objects:
            actor.x+=actor.velocityx
            actor.y+=actor.velocityy




