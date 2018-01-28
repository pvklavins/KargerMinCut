# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 11:29:07 2018

@author: PK
"""

## A node is a object from a graph with multiple edges
## It may also contain other nodes that have been combined into it

class node(object):
    def __init__(self, name, loe):
        self.name = name
        self.loe = loe
        self.lonodes = [name]   #every node starts with just itself, add 
                                #more nodes as it becomes a supernode  
        self.numE = len(self.getLoe())


    def getName(self):
        return self.name
    def getLonodes(self):
        return self.lonodes
    def getLoe(self):
        return self.loe
    def getNumE(self):
        return self.numE
    
    def setLonodes(self,lon):
        self.lon = lon
    def setLoe(self, loe):
        self.loe = loe
        self.setNumE(len(self.getLoe()))
    def setNumE(self,numE):
        self.numE = numE
    
    # REQUIRES: another node
    # EFFECTS: This
    def combineNodes(self, other):
        lon1 = self.getLonodes()
        lon2 = other.getLonodes()
        lonFinal = lon1
        loe1 = self.getLoe()
        loe2 = other.getLoe()
        loeFinal = []
        for edge in loe1:
            if edge not in lon2:
                loeFinal.append(edge)
        for edge in loe2:
            if edge not in lon1:
                loeFinal.append(edge)
        self.setLoe(loeFinal)
        
        
        for node in other.lonodes:
            lonFinal.append(node)
        self.setLonodes(lonFinal)

