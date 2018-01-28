# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 11:29:07 2018

@author: PK
"""

class node(object):
    def __init__(self, name):
        self.name = name
        self.lonodes = [name] #every node starts with just itself

    def getName(self):
        return self.name
    def getLonodes(self):
        return self.lonodes
    def setLonodes(self,lon):
        self.lon = lon
    def combineNodes(self, other):
        nodeslist = self.getLonodes()
        for node in other.lonodes:
            nodeslist.append(node)
