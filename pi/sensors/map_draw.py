import pygame

scale = 10
def get_map_pygame(sizex, sizey):
    pygame.init()
    map_sizeX = sizex*scale
    map_sizeY = sizey*scale
    screen = pygame.display.set_mode([map_sizeX, map_sizeY])
    pygame.display.set_caption("Draw the map")

    keep_going = True
    marker = (0, 255, 255)
    radius = 5
    points = []
    
    while keep_going:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
              spot = event.pos
              points.append([spot[0]/scale,(map_sizeY-spot[1])/scale])
              pygame.draw.circle(screen, marker, spot, radius)
              
        pygame.display.update()

    pygame.quit()
    return points