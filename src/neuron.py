'''
Created on Jan 29, 2018

@author: hukka
'''
import math
import sys

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


    def addSinapses(self, inSinapses, outSinapses):
        
        for s in inSinapses:
            self.inSinapses.append(s)   
            s.setEndNeuron(self)
                 
        for s in outSinapses:
            self.outSinapses.append(s)
            s.setStartNeuron(self)

     
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
 
i1 = Neuron("i1")   
i2 = Neuron("i2")     
h1 = Neuron("h1")
h2 = Neuron("h2")
o1 = Neuron("o1")
o2 = Neuron("o2")
 
b1 = .35
b2 = 0.60            
n = 10.0 # learning speed


def learn(i1v: float, i2v: float, target_o1: float, target_o2: float):
    
    i1.setValue(i1v)
    i2.setValue(i2v)
    
        
    out_h1 = h1.getOut()
    out_h2 = h2.getOut()

    out_o1 = o1.getOut()
    out_o2 = o2.getOut()
    
    Etotal = 1/2 * (target_o1 - out_o1)**2 + 1/2 * (target_o2 - out_o2)**2
      
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
    
            

# test
if __name__ == '__main__': # pragma: no cover
    

    w1 = Sinaps("w1", .15)
    w2 = Sinaps("w2", .20) 
    w3 = Sinaps("w3", .25) 
    w4 = Sinaps("w4", .30) 
    w5 = Sinaps("w5", .40) 
    w6 = Sinaps("w6", .45)
    w7 = Sinaps("w7", .50)
    w8 = Sinaps("w8", .55)
    
    i1.addSinapses([], [w1, w3])
    i2.addSinapses([], [w2, w4])
    
    h1.addSinapses([w1, w2], [w5, w7])
    h2.addSinapses([w3, w4], [w6, w8])
    h1.setB(b1)
    h2.setB(b1)
     
    o1.addSinapses([w5, w6], [])
    o2.addSinapses([w7, w8], []) 
    o1.setB(b2)
    o2.setB(b2)
        


    for x in range(1, 1000):
    
    #   print(x)
    
        learn(1, 1, 0, 1)
    #    learn(1, 0, 1, 0)
        
        
        learn(1, 1, 1, 1)    