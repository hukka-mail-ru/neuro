'''
Created on Jan 31, 2018

@author: hukka
'''


import random

import show
import brain

 
      
 

if __name__ == '__main__': # pragma: no cover

    b1 = .35
    b2 = 0.60            
    n = 10.0 # learning speed
   
    iNeurons = []
    hNeurons = [] 
    oNeurons = []  
            
    for x in range (0, 2):
        i = brain.Neuron("i")
        i.setPos(100, 10 + 50*x)
        iNeurons.append(i)
     

   # print("d", iNeurons[0].getValue())    

    for x in range (0, 4):
        h = brain.Neuron("h")
        h.setPos(200, 10 + 50*x)
        h.setB(b1)
        hNeurons.append(h)
    

    for x in range (0, 2):
        o = brain.Neuron("o")
        o.setPos(300, 10 + 50*x)
        o.setB(b2)
        oNeurons.append(o)
    
    neurons = iNeurons + hNeurons + oNeurons
    
    
    
    for i in iNeurons:
        for h in hNeurons:
            f = brain.Sinaps("f", random.random() / 2)
            i.addOutSinaps(f)
            h.addInSinaps(f)
    
    for h in hNeurons:
        for o in oNeurons:
            w = brain.Sinaps("w", random.random() / 2)
            h.addOutSinaps(w)
            o.addInSinaps(w)
            
    '''
    
    iNeurons[0].outSinapses[0].weight = .15   
    iNeurons[1].outSinapses[0].weight  = .20
    iNeurons[0].outSinapses[1].weight  = .25 
    iNeurons[1].outSinapses[1].weight  = .30 
    hNeurons[0].outSinapses[0].weight  = .40 
    hNeurons[1].outSinapses[0].weight  = .45 
    hNeurons[0].outSinapses[1].weight  = .50 
    hNeurons[1].outSinapses[1].weight = .55
    '''
    print(iNeurons[0].outSinapses[0].getWeight())    
    print(iNeurons[0].outSinapses[1].getWeight())  
    print(iNeurons[1].outSinapses[0].getWeight())  
    print(iNeurons[1].outSinapses[1].getWeight())  
    print(hNeurons[0].outSinapses[0].getWeight())  
    print(hNeurons[0].outSinapses[1].getWeight())  
    print(hNeurons[1].outSinapses[0].getWeight())  
    print(hNeurons[1].outSinapses[1].getWeight())      
              
    for x in range(1, 200):
    
        print("ONE")
        iNeurons[0].setValue(1)
        iNeurons[1].setValue(1)
        
        oNeurons[0].setTarget(0)
        oNeurons[1].setTarget(1)
                
        brain.learn(hNeurons, oNeurons, n)
        
        print("TWO")
        iNeurons[0].setValue(1)
        iNeurons[1].setValue(0)
        
        oNeurons[0].setTarget(1)
        oNeurons[1].setTarget(0)
                
        brain.learn(hNeurons, oNeurons, n)    
         
        #    learn(1, 0, 1, 0)
             
          
             
    ''' output ''' 
     
    graphics = show.Graphics()

    for n in neurons:                
        n.draw(graphics)        

        for s in n.getOutSinapses():            
            s.draw(graphics)
            

    graphics.flip()    
    graphics.waitForKey()

