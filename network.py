# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 14:43:03 2018

@author: PK
"""

from node import node
from listOfEdges import listOfEdges

class network(object):
    def __init__(self, lon, loe):
        self.lon = lon
        self.loe = loe
            
    def getLon(self):
        return self.lon
    def getLoe(self):
        return self.loe
    def cut(self):
        loe = self.getLoe()
        lon = self.getLon()
        newCut = loe.getRandomEdge()
        firstNode = newCut[0]
        secNode = newCut[1]
        #print("combine nodes: " + str(firstNode) + " and " + str(secNode))
        for i in lon:
            if firstNode in i.getLonodes():
                for j in lon:
                    if secNode in j.getLonodes():
                        i.combineNodes(j)
                        lon.remove(j)
                        loe.clearSelfLoops(i.getLonodes())
                        break
                break
        
    def minCut(self):
        while True:
            if len(self.getLon()) == 2:
                return int(len(self.getLoe().getLoe())/2)
            self.cut()


