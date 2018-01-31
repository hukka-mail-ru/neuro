'''
Created on Jan 31, 2018

@author: hukka
'''
import math
import sys
import pygame
import random

def sigmoid(x: float):
    return 1.0 / (1.0 + math.exp(-x))


class Sinaps():
    
    def __init__(self, name, weight):  
        self.weight = weight
        self.name = name
    
    def getName(self):
        return self.name
            
    def getWeight(self):
        return self.weight
    
    def setWeight(self, w):
        self.weight = w
        
    def setStartNeuron(self, neuron):
        self.startNeuron = neuron  
            
    def getStartNeuron(self):
        return self.startNeuron  
    
    
    def setEndNeuron(self, neuron):
        self.endNeuron = neuron          
    
    def getEndNeuron(self):
        return self.endNeuron  

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
 
    def getOut(self):
        net = self.b
        for sinaps in self.inSinapses:
            net += sinaps.getWeight() * sinaps.getStartNeuron().getValue()    
        self.value = sigmoid(net)
        return self.value
 

if __name__ == '__main__': # pragma: no cover

    b1 = .35
    b2 = 0.60            
    n = 10.0 # learning speed
   
    iNeurons = [] 
    for x in range (0, 5):
        i = Neuron("i")
        i.setPos(100, 10 + 50*x)
        iNeurons.append(i)
        
    hNeurons = [] 
    for x in range (0, 3):
        h = Neuron("h")
        h.setPos(200, 10 + 50*x)
        h.setB(b1)
        hNeurons.append(h)
    
    oNeurons = [] 
    for x in range (0, 5):
        o = Neuron("o")
        o.setPos(300, 10 + 50*x)
        o.setB(b2)
        oNeurons.append(o)
    
    neurons = iNeurons + hNeurons + oNeurons
    
    for i in iNeurons:
        for h in hNeurons:
            f = Sinaps("f", random.random() / 3)
            i.addOutSinaps(f)
            h.addInSinaps(f)
    
    for h in hNeurons:
        for o in oNeurons:
            w = Sinaps("w", random.random() / 3)
            h.addOutSinaps(w)
            o.addInSinaps(w)
     
             
    ''' output ''' 
     
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    

    for n in neurons:
        
        color = (255, 255, 255)
        if n.getName() == "i":
            color = (255, 255, 255)
        elif n.getName() == "h":   
            color = (255, 255, 0)
        elif n.getName() == "o":   
            color = (255, 0, 255)  
            
        (x, y) = n.getPos()
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 10, 10))
        for s in n.getOutSinapses():
            color = (255 * s.getWeight(), 255 * s.getWeight(), 255 * s.getWeight())           
            pygame.draw.line(screen, color, s.getStartNeuron().getPos(), s.getEndNeuron().getPos())

    
    pygame.display.flip()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                done = True 