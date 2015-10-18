__author__ = 'lukaszlampart'
"""This module is responisble for loading setings, formating is yet to specify
"""


def get_dimension(name='config'):
    f = open(name, 'r')
    st = f.readline()
    return st

print (get_dimension())



