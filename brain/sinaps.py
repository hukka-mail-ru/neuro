'''
Created on Jan 31, 2018

@author: hukka
'''

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
    
        
    def setDs(self, d):
        self.ds = d
        
    def getDs(self):
        return self.ds
    
    def draw(self, graphics):
        if self.weight < 0:
            graphics.setColor((10, 10, 10))
        elif self.weight > 1:
            graphics.setColor((255, 255, 255))
        else:
            graphics.setColor((255 * self.weight, 255 * self.weight, 255 * self.weight))      

        graphics.drawLine(self.startNeuron.getPos(), self.endNeuron.getPos())