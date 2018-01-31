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
    
    for h in hNeurons:
        dEtotal_dout = 0
        for o in oNeurons:
            dEtotal_dout += o.getDelta() * h.getSinapsTo(o).getWeight()
        h.setdEtotal_dout(dEtotal_dout)
     
     
   # for i in iNeurons:
   #     for s in i.getOutSinapses():
   #         ds = 
       
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
        i = neuron.Neuron("i")
        i.setPos(100, 10 + 50*x)
        iNeurons.append(i)
        

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