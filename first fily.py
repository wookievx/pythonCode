__author__ = 'lukaszlampart'
"""This module is responisble for loading setings, formating is yet to specify
It launches the game if config file has good formating
"""
import gameengine

def get_dimension(name='config'):
    f = open(name, 'r')
    st = f.readline()
    opt_1,opt_2 = st.split(';')
    name,value = opt_1.split(':')
    sname,svalue = opt_2.split(':')
    return value,svalue

tuplea=get_dimension()
auto=gameengine.Game(iheight=int(tuplea[0]),iwidth=int(tuplea[1]),bgcolor="black")

auto.init()


print (get_dimension())



