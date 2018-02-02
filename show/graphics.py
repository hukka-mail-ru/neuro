'''
Created on Feb 2, 2018

@author: hukka
'''
import pygame


class Graphics():
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 400))
        
   
    def drawBall(self, pos):
        (x, y) = pos
        pygame.draw.circle(self.screen, self.color, pos, 10)
        pygame.draw.circle(self.screen, (255,255,255), (x-4,y-4), 2)     
        
        
    def drawLine(self, pos1, pos2):    
        pygame.draw.line(self.screen, self.color, pos1, pos2)    
        
    def setColor(self, color):
        self.color = color       
        
    def flip(self):        
        pygame.display.flip()   
        
    def waitForKey(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    done = True
                      
    def clearScreen(self):                    
        self.screen.fill((0,0,0))
        
        