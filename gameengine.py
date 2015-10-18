__author__ = 'lukaszlampart'

from tkinter import *


class Game:
    def __init__(self, iheight=300, iwidth=300, bgcolor="black"):
        self.root = Tk()
        self.RUN = False

        self.frame = Frame(bg=bgcolor)
        self.frame.pack()

        self.height=iheight
        self.width=iwidth

        self.canvas = Canvas(self.frame, bg=bgcolor,width=self.width,height=self.height)
        self.canvas.pack()

        self.root.mainloop()

        self.graphsFlag=False

        self.image=[]

    def load_image(self):
        self.image.append(PhotoImage(file="graphics/game_graph.gif"))

    def init(self):
        if self.graphsFlag is False:
            self.graphsFlag=True
            self.root.after(10,self.init)
        else:
            self.load_image()
            self.run()

    def paint(self):
        self.canvas.delete(ALL)
        self.canvas.create_image(self.height/2-100,self.width/2-100,anchor=NW,image=self.image[0])

    def run(self):
        self.paint()
        self.root.after(10,self.run)




