__author__ = 'lukaszlampart'
"""This module is responisble for loading setings, formating is yet to specify
It launches the game if config file has good formating
"""
import gameengine
import math3d as m3d

def get_dimension(name='config'):
    f = open(name, 'r')
    st = f.readline()
    opt_1,opt_2 = st.split(';')
    name,value = opt_1.split(':')
    sname,svalue = opt_2.split(':')
    return value,svalue

r=m3d.Orientation.new_rot_z(3.14/4)

v=m3d.Vector(1,0,0)
print(r * v)

p=gameengine.PlayerChar(20,0,0,5,0)
print(str(p.leftArmLine[0])+" "+str(p.leftArmLine[1]))
print(p.speedVal)

tuplea=get_dimension()
auto=gameengine.Game(iheight=int(tuplea[0]),iwidth=int(tuplea[1]),bgcolor="yellow")


print (get_dimension())



