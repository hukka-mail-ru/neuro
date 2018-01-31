'''
Created on Jan 31, 2018

@author: hukka
'''

import pygame
import random

import neuron
import sinaps

 
iNeurons = [] 
hNeurons = [] 
oNeurons = []  



def learn():
    

    
    #i1.setValue(i1v)
    #i2.setValue(i2v)
    
    for h in hNeurons: 
        h.calcValue()

    for o in oNeurons: 
        o.calcValue()
    
    Etotal = 0
    for o in oNeurons:
        Etotal += 1/2 * (o.getTarget() - o.getValue())**2
    
      
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
    
    
    for h in hNeurons:
        dEtotal_dout = 0
        for s in h.getOutSinapses():  
            dEtotal_dout += s.getEndNeuron().getDelta() * s.getWeight()
        h.setdEtotal_dout(dEtotal_dout)
     
     
    for h in hNeurons:
        
        for s in h.getInSinapses():
            
            ds = h.getdEtotal_dout() * h.getValue() *  (1 - h.getValue()) * s.getStartNeuron().getValue()
            s.setDs(ds)
            
        for s in h.getOutSinapses():   
     
            ds = s.getEndNeuron().getDelta() * h.getValue()
            s.setDs(ds)

    
    for h in hNeurons:
        
        for s in h.getInSinapses():
            
            s.setWeight(s.getWeight() - n * s.getDs())
            
        for s in h.getOutSinapses():   
     
            s.setWeight(s.getWeight() - n * s.getDs())
               

    
   
 

if __name__ == '__main__': # pragma: no cover

    b1 = .35
    b2 = 0.60            
    n = 10.0 # learning speed
   
            
    for x in range (0, 2):
        i = neuron.Neuron("i")
        i.setPos(100, 10 + 50*x)
        iNeurons.append(i)
     

    print("d", iNeurons[0].getValue())    

    for x in range (0, 2):
        h = neuron.Neuron("h")
        h.setPos(200, 10 + 50*x)
        h.setB(b1)
        hNeurons.append(h)
    

    for x in range (0, 2):
        o = neuron.Neuron("o")
        o.setPos(300, 10 + 50*x)
        o.setB(b2)
        oNeurons.append(o)
    
    neurons = iNeurons + hNeurons + oNeurons
    
    for i in iNeurons:
        for h in hNeurons:
            f = sinaps.Sinaps("f", random.random() / 2)
            i.addOutSinaps(f)
            h.addInSinaps(f)
    
    for h in hNeurons:
        for o in oNeurons:
            w = sinaps.Sinaps("w", random.random() / 2)
            h.addOutSinaps(w)
            o.addInSinaps(w)
     
          
    for x in range(1, 200):
    
        print("ONE")
        iNeurons[0].setValue(1)
        iNeurons[1].setValue(1)
        
        oNeurons[0].setTarget(0)
        oNeurons[1].setTarget(1)
                
        learn()
        
        print("TWO")
        iNeurons[0].setValue(1)
        iNeurons[1].setValue(1)
        
        oNeurons[0].setTarget(1)
        oNeurons[1].setTarget(1)
                
        learn()       
        #    learn(1, 0, 1, 0)
             
          
             
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
            if s.getWeight() < 0:
                color = (10, 10, 10)
            elif s.getWeight() > 1:
                color = (255, 255, 255)
            else:
                color = (255 * s.getWeight(), 255 * s.getWeight(), 255 * s.getWeight())      
                
            print("color:", 255 * s.getWeight())         
            pygame.draw.line(screen, color, s.getStartNeuron().getPos(), s.getEndNeuron().getPos())

    
    pygame.display.flip()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                done = True 