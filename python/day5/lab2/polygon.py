from abc import ABC, abstractmethod


class FourSideShape():

    def __init__(self,shapename):
        self.name=shapename

    def getArea(self):
        pass
    
    def getPertimerter(self):
        pass

