# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 14:43:03 2018

@author: PK
"""

from node import node
import random

## A network is a group of nodes

class network(object):
    def __init__(self, lon):
        self.lon = lon
        self.noe = self.countEdges()
    
    def getLon(self):
        return self.lon
    def getNoe(self):
        return self.noe

    def setLon(self, lon):
        self.lon = lon
        self.noe = self.countEdges()

    def countEdges(self):
        lon = self.getLon()
        total = 0
        for n in lon:
            total += n.getNumE()
        return total
    
    def getRandomEdge(self):
        randomEdge = random.randrange(0,self.getNoe())
        return randomEdge
    
    # REQUIRES: a randomly selected edge #
    # RETURNS: the selected edge
    def chooseEdge(self,spot):
        edgesLeft = spot
        for n in self.getLon():
            if edgesLeft - n.getNumE() < 0:
                node2part = n.getLoe()[edgesLeft]
                for n2 in self.getLon():
                    if node2part in n2.getLonodes():
                        return (n, n2)
            else:
                edgesLeft -= n.getNumE()
        print("error in chooseEdge")
    
    # MODIFYS: self
    def cut(self):
        lon = self.getLon()
        edgeToCut = self.getRandomEdge()
        (firstNode, secNode) = self.chooseEdge(edgeToCut)
        firstNode.combineNodes(secNode)
        lon.remove(secNode)
        self.setLon(lon)
    
    def minCut(self):
        while True:
            if len(self.getLon()) == 2:
                return int(self.getNoe()/2)
            self.cut()


#simple test node   
if __name__ == "__main__":
#    lon = [node(1,[2,3]),node(2,[1,3,4]),node(3,[1,2,4]),node(4,[2,3,5]),node(5,[4])]
#    network2 = network(lon)
#    y = network2.minCut()
#    print(y)
    
    iterations = 200
    minCut = 1000000

    for j in range(0,iterations):
        f = open("kargerMinCut.txt","r") #opens file with name of "test.txt"
        lon = []
        for line in f:
            loe = []
            los = line.split()
            first = int(los.pop(0))
            for i in range(0,len(los)):
                edge = int(los[i])
                loe.append(edge)
            lon.append(node(first,loe))

        f.close()      
        network1 = network(lon)
        newCut = network1.minCut()   
        
        if newCut < minCut:
            minCut = newCut
    print("Minimum Cut is = " + str(minCut))
