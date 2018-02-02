'''
Created on Jan 31, 2018

@author: hukka
'''
import brain

class Sinaps():
    
    def __init__(self, weight):  
        self.weight = weight
    
            
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
        
        k = brain.sigmoid(self.weight)
                
        if(k > 0.5):
            graphics.setColor((255 * k, 255 * k, 255 * k))         
            graphics.drawLine(self.startNeuron.getPos(), self.endNeuron.getPos())