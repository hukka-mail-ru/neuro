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
 
    def calcValue(self):
        net = self.b
        for sinaps in self.inSinapses:
            net += sinaps.getWeight() * sinaps.getStartNeuron().getValue()    
        self.value = sigmoid(net)
 
iNeurons = [] 
hNeurons = [] 
oNeurons = []  



def learn(i1v: float, i2v: float, target_o1: float, target_o2: float):
    

    
    #i1.setValue(i1v)
    #i2.setValue(i2v)
    
    for h in hNeurons: 
        h.calcValue()

    for o in oNeurons: 
        o.calcValue()
    
    Etotal = 0
    for o in oNeurons:
        Etotal += 1/2 * (o.getTarget() - o.getValue())**2
      
    print("learn ", i1v, i2v, "->", target_o1, target_o2)  
    print("----------------")
    print("out_o1 %.2f" % out_o1)
    print("out_o2 %.2f" % out_o2)
    print("----------------")    
    print("Etotal %.8f" % Etotal)
    
        
    # backpropagate 
    
    delta_o1 = (out_o1 - target_o1) * out_o1 * (1 - out_o1)
    delta_o2 = (out_o2 - target_o2) * out_o2 * (1 - out_o2)
       
    dEtotal_dout_h1 = delta_o1 * w5.getWeight() + delta_o2 * w7.getWeight()
    dEtotal_dout_h2 = delta_o1 * w7.getWeight() + delta_o2 * w8.getWeight()
       
       
    dw1 = dEtotal_dout_h1 * out_h1 * (1 - out_h1) * i1.getValue()
    dw2 = dEtotal_dout_h1 * out_h1 * (1 - out_h1) * i2.getValue()
    dw3 = dEtotal_dout_h2 * out_h2 * (1 - out_h2) * i1.getValue()
    dw4 = dEtotal_dout_h2 * out_h2 * (1 - out_h2) * i2.getValue()
    
    dw5 = delta_o1 * out_h1
    dw6 = delta_o1 * out_h2
    dw7 = delta_o2 * out_h1
    dw8 = delta_o2 * out_h2
    
    
    w1.setWeight(w1.getWeight() - n * dw1)
    w2.setWeight(w2.getWeight() - n * dw2)
    w3.setWeight(w3.getWeight() - n * dw3)
    w4.setWeight(w4.getWeight() - n * dw4)
    w5.setWeight(w5.getWeight() - n * dw5)
    w6.setWeight(w6.getWeight() - n * dw6)
    w7.setWeight(w7.getWeight() - n * dw7)
    w8.setWeight(w8.getWeight() - n * dw8)
    
   
 

if __name__ == '__main__': # pragma: no cover

    b1 = .35
    b2 = 0.60            
    n = 10.0 # learning speed
   
            
    for x in range (0, 2):
        i = Neuron("i")
        i.setPos(100, 10 + 50*x)
        iNeurons.append(i)
        

    for x in range (0, 2):
        h = Neuron("h")
        h.setPos(200, 10 + 50*x)
        h.setB(b1)
        hNeurons.append(h)
    

    for x in range (0, 2):
        o = Neuron("o")
        o.setPos(300, 10 + 50*x)
        o.setB(b2)
        oNeurons.append(o)
    
    neurons = iNeurons + hNeurons + oNeurons
    
    for i in iNeurons:
        for h in hNeurons:
            f = Sinaps("f", random.random() / 2)
            i.addOutSinaps(f)
            h.addInSinaps(f)
    
    for h in hNeurons:
        for o in oNeurons:
            w = Sinaps("w", random.random() / 2)
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