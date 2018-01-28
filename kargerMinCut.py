# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 10:55:37 2018

@author: PK
"""
from network import network
from node import node
import random

if __name__ == "__main__":
    iterations = 200**2
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
        print(j, newCut, minCut)


#loe = listOfEdges([(1,2),(1,3),(2,1),(2,3),(2,4),(3,1),(3,2),(3,4),(4,2),(4,3),(4,5),(5,4)])
#lon = [node(1),node(2),node(3),node(4),node(5)]
#network2 = network(lon,loe)
#y = network2.minCut()

