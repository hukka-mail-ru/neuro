'''
Created on Jan 31, 2018

@author: hukka
'''
import math


def sigmoid(x: float):
    return 1.0 / (1.0 + math.exp(-x))


class Neuron():
    
    def __init__(self, name):        
        self.value = 0
        self.b = 0
        self.inSinapses = []
        self.outSinapses = []
        self.name = name

    def getName(self):
        return self.name
    
    def setValue(self, v: float):
        self.value = v
    
    def getValue(self):
        return self.value
    
    def setTarget(self, t: float):
        self.target = t
    
    def getTarget(self):
        return self.target
    
    def addOutSinaps(self, sinaps):
        self.outSinapses.append(sinaps)
        sinaps.setStartNeuron(self)
    
    def addInSinaps(self, sinaps):
        self.inSinapses.append(sinaps)
        sinaps.setEndNeuron(self)
        
    def getOutSinapses(self):
        return self.outSinapses
    
    def getInSinapses(self):
        return self.inSinapses

    def setdEtotal_dout(self, d):
        self.dEtotal_dout = d
        
    def getdEtotal_dout(self):
        return self.dEtotal_dout


    def setPos(self, x, y):
        self.x = x
        self.y = y
    
    def getPos(self):
        return (self.x, self.y)
     
    def setB(self, b: float):
        self.b =b

    def show(self): 
        for s in self.inSinapses:
            print("in: ", s.getWeight())
        for s in self.outSinapses:
            print("out: ", s.getWeight())
 
    def calcValue(self):
        net = self.b
        for sinaps in self.inSinapses:
            net += sinaps.getWeight() * sinaps.getStartNeuron().getValue()    
        self.value = sigmoid(net)
 
    def getDelta(self):
        return (self.value - self.target) * self.value * (1 - self.value)
    
    
    def  draw(self, graphics):
        graphics.setColor(255, 255, 255)
        if self.name == "i":
            graphics.setColor(0, 0, 255)
        elif self.name == "h":   
            graphics.setColor(255, 0, 0)
        elif self.name == "o":   
            graphics.setColor(0, 255, 0)  
            
        graphics.drawBall((self.x, self.y))