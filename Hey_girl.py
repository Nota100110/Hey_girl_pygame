import pygame #always import pygame

pygame.init() #always initialise 

gameDisplay = pygame.display.set_mode((800,600)) #window

pygame.display.set_caption('Hey girl') #caption name

clock = pygame.time.Clock() #specific game clock, only time it comes out of clock is when crashed

crashed = False

#this is while crashed = false
while not crashed:
    for event in pygame.event.get(): #'event' all list of events i.e. mouse/keyboard
        if event.type == pygame.QUIT:
            crashed = True 

        #print (event) #will only work for single frame

    pygame.display.update() #or flip - can put in paramter () and will update
                            #otherwise updates entire window/ flip does all surface
    clock.tick(60)

pygame.quit()               #this is to quit
quit()
    
    
    


