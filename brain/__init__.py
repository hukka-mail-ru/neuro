from brain.neuron import Neuron
from brain.sinaps import Sinaps

import random
import math

def sigmoid(x: float):
    return 1.0 / (1.0 + math.exp(-x))




class Brain():
    
    
    def deleteUselessSinapses(self):
    
        neurons = self.iNeurons + self.hNeurons + self.oNeurons
    
        for n in neurons:
            
            n.deleteUselessSinapses()
            
                    
    
    
    def teach(self, inputValues, targetValues):
        
        i = 0
        for x in inputValues:
            self.iNeurons[i].setValue(x)
            i += 1

        o = 0
        for y in targetValues:
            self.oNeurons[o].setTarget(y)
            o += 1 

    def clear(self):
        self.iNeurons = [] 
        self.hNeurons = [] 
        self.oNeurons = []   
        
    
    def create(self, i_num: int, h_num: int, o_num: int):
        self.iNeurons = self.createNeurons(Neuron.Kind.I, i_num) 
        self.hNeurons = self.createNeurons(Neuron.Kind.H, h_num)
        self.oNeurons = self.createNeurons(Neuron.Kind.O, o_num)  
        
        self.createSinapsesBetween(self.iNeurons, self.hNeurons)
        self.createSinapsesBetween(self.hNeurons, self.oNeurons)



    def createNeurons(self, kind: Neuron.Kind, number):
        
        neurons = []
        
        for x in range (0, number):
            n = Neuron(kind, x)                      
            neurons.append(n)
         
        return neurons   
      
  
    
    
    def createSinapsesBetween(self, xNeurons, yNeurons):
    
        for x in xNeurons:
            for y in yNeurons:
                w = Sinaps(random.random() / 2)
                x.addOutSinaps(w)
                y.addInSinaps(w)
            
    
    def draw(self, graphics):
        
        neurons = self.iNeurons + self.hNeurons + self.oNeurons 
        
        for n in neurons:                
            n.draw(graphics)        
    
            for s in n.getOutSinapses():            
                s.draw(graphics)    
                    

    def learn(self, learningSpeed: float):
        
    
        
        #i1.setValue(i1v)
        #i2.setValue(i2v)
        
        for h in self.hNeurons: 
            h.calcValue()
            #print("h.value", h.getValue())
    
        for o in self.oNeurons: 
            o.calcValue()
            #print("o.value", o.getValue())
        
        Etotal = 0
        for o in self.oNeurons:
            Etotal += 1/2 * (o.getTarget() - o.getValue())**2
        
        #print("Etotal",Etotal)
          
        # print("learn ", i1v, i2v, "->", target_o1, target_o2)  )
        for o in self.oNeurons: 
            print("out_o %.2f" % o.getValue())   
        print("Etotal %.8f" % Etotal)
        
            
        # backpropagate 
        
        # delta_o1 = (out_o1 - target_o1) * out_o1 * (1 - out_o1)
        #  delta_o2 = (out_o2 - target_o2) * out_o2 * (1 - out_o2)
        
        # dEtotal_dout_h1 = delta_o1 * w5.getWeight() + delta_o2 * w7.getWeight()
        # dEtotal_dout_h2 = delta_o1 * w7.getWeight() + delta_o2 * w8.getWeight()
        
        #print("getDelta " , oNeurons[0].getDelta())
        #print("getDelta " , oNeurons[1].getDelta())
        
        for h in self.hNeurons:
            dEtotal_dout = 0
            for s in h.getOutSinapses():  
                dEtotal_dout += s.getEndNeuron().getDelta() * s.getWeight()
                #print("delta " , s.getEndNeuron().getDelta())
                #print("* w " , s.getWeight())
                #print("res" , )
            h.setdEtotal_dout(dEtotal_dout)
         
        #print("dEtotal_dout_h1 " , hNeurons[0].getdEtotal_dout())
        #print("dEtotal_dout_h1 " , hNeurons[1].getdEtotal_dout()) 
         
        for h in self.hNeurons:
            
            for s in h.getInSinapses():
                
                ds = h.getdEtotal_dout() * h.getValue() *  (1 - h.getValue()) * s.getStartNeuron().getValue()
                s.setDs(ds)
                
            for s in h.getOutSinapses():   
         
                ds = s.getEndNeuron().getDelta() * h.getValue()
                s.setDs(ds)
    
        
        for h in self.hNeurons:
            
            for s in h.getInSinapses():
                
                s.setWeight(s.getWeight() - learningSpeed * s.getDs())
                
            for s in h.getOutSinapses():   
         
                s.setWeight(s.getWeight() - learningSpeed * s.getDs())
                
        return Etotal        