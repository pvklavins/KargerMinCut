# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 14:55:24 2018

@author: PK
"""



class listOfEdges(object):
    def __init__(self, loe):
        self.loe = loe
        #list of edges is a list of tuples
    
    def getLoe(self):
        return self.loe
    def setLoe(self, loe):
        self.loe = loe
    
    def getLength(self):
        return len(self.getLoe())
    


    def clearSelfLoops(self,lon):
        okayLoe = []
        for e in self.getLoe():
            if e[0] not in lon or e[1] not in lon:
                okayLoe.append(e)
        self.setLoe(okayLoe)


    

