__author__ = 'lukaszlampart'

from tkinter import *
import movementengine

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
        """paramters of the window of the game loaded from the config file
        """
        self.height=iheight
        self.width=iwidth
        """Canvas drawing graphics of the game
        """
        self.canvas = Canvas(self.frame, bg=bgcolor,width=self.width,height=self.height)
        self.canvas.pack()

        """movement handler object
        """
        self.moveEngine=movementengine.mapMovement(self.height, self.width)

        self.root.mainloop()
        """ flag responsible for importing assets into the game as this cannot be made
        during initialization"""
        self.graphsFlag=False
        """ list of images imported into the game
        dictionary could be another and probably better option"""
        self.image=[]

    def loadImage(self):
        self.image.append(PhotoImage(file="graphics/game_graph.gif"))

    def init(self):
        if self.graphsFlag is False:
            self.graphsFlag=True
            self.root.after(10,self.init)
        else:
            self.loadImage()
            self.run()

    def paint(self):
        self.canvas.delete(ALL)
        self.canvas.create_image(self.height/2-100,self.width/2-100,anchor=NW,image=self.image[0])


    def run(self):
        self.paint()
        self.root.after(10,self.run)




