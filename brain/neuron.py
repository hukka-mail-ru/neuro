'''
Created on Jan 31, 2018

@author: hukka
'''

import enum
import brain


class Neuron():
    
    class Kind(enum.Enum):
        I = 1
        H = 2
        O = 3
    
    def __init__(self, kind: Kind, number):        
        self.value = 0
        self.b = 0
        self.inSinapses = []
        self.outSinapses = []
        self.kind = kind
        
        if self.kind == Neuron.Kind.I:
            self.x = 100
            self.color = (0, 0, 255)
            
        elif self.kind == Neuron.Kind.H:   
            self.x = 200
            self.color = (255, 0, 0)
            
        elif self.kind == Neuron.Kind.O:   
            self.x = 300
            self.color = (0, 255, 0) 
            
        self.y = 10 + 50 * number
        
            

    def getKind(self):
        return self.kind
    
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
        self.value = brain.sigmoid(net)
 
    def getDelta(self):
        return (self.value - self.target) * self.value * (1 - self.value)
    
    
    def  draw(self, graphics):
        graphics.setColor(self.color)           
        graphics.drawBall((self.x, self.y))