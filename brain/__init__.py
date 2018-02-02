from brain.neuron import Neuron
from brain.sinaps import Sinaps

import random
import math

def sigmoid(x: float):
    return 1.0 / (1.0 + math.exp(-x))



def createNeurons(kind: Neuron.Kind, number):
    
    neurons = []
    
    for x in range (0, number):
        n = Neuron(kind, x)                      
        neurons.append(n)
     
    return neurons   



def createSinapsesBetween(xNeurons, yNeurons):

    for x in xNeurons:
        for y in yNeurons:
            w = Sinaps(random.random() / 2)
            x.addOutSinaps(w)
            y.addInSinaps(w)
            
            

def learn(hNeurons, oNeurons, learningSpeed: float):
    

    
    #i1.setValue(i1v)
    #i2.setValue(i2v)
    
    for h in hNeurons: 
        h.calcValue()
        #print("h.value", h.getValue())

    for o in oNeurons: 
        o.calcValue()
        #print("o.value", o.getValue())
    
    Etotal = 0
    for o in oNeurons:
        Etotal += 1/2 * (o.getTarget() - o.getValue())**2
    
    #print("Etotal",Etotal)
      
    # print("learn ", i1v, i2v, "->", target_o1, target_o2)  
    print("----------------")
    for o in oNeurons: 
        print("out_o %.2f" % o.getValue())
    print("----------------")    
    print("Etotal %.8f" % Etotal)
    
        
    # backpropagate 
    
    # delta_o1 = (out_o1 - target_o1) * out_o1 * (1 - out_o1)
    #  delta_o2 = (out_o2 - target_o2) * out_o2 * (1 - out_o2)
    
    # dEtotal_dout_h1 = delta_o1 * w5.getWeight() + delta_o2 * w7.getWeight()
    # dEtotal_dout_h2 = delta_o1 * w7.getWeight() + delta_o2 * w8.getWeight()
    
    #print("getDelta " , oNeurons[0].getDelta())
    #print("getDelta " , oNeurons[1].getDelta())
    
    for h in hNeurons:
        dEtotal_dout = 0
        for s in h.getOutSinapses():  
            dEtotal_dout += s.getEndNeuron().getDelta() * s.getWeight()
            #print("delta " , s.getEndNeuron().getDelta())
            #print("* w " , s.getWeight())
            #print("res" , )
        h.setdEtotal_dout(dEtotal_dout)
     
    #print("dEtotal_dout_h1 " , hNeurons[0].getdEtotal_dout())
    #print("dEtotal_dout_h1 " , hNeurons[1].getdEtotal_dout()) 
     
    for h in hNeurons:
        
        for s in h.getInSinapses():
            
            ds = h.getdEtotal_dout() * h.getValue() *  (1 - h.getValue()) * s.getStartNeuron().getValue()
            s.setDs(ds)
            
        for s in h.getOutSinapses():   
     
            ds = s.getEndNeuron().getDelta() * h.getValue()
            s.setDs(ds)

    
    for h in hNeurons:
        
        for s in h.getInSinapses():
            
            s.setWeight(s.getWeight() - learningSpeed * s.getDs())
            
        for s in h.getOutSinapses():   
     
            s.setWeight(s.getWeight() - learningSpeed * s.getDs())
            
    return Etotal        