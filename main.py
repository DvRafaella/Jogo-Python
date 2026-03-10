import pygame

print('setup started')
pygame.init()
window = pygame.display.set_mode((800, 600))
print('setup ended')

print('loop started')
while True:
    #check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()#close window
            quit()#end pygame







