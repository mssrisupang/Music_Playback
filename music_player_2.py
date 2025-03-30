import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300)) #20. Pygame — Playing music
done = False
white = (255,255,255)
pygame.mixer.music.load("StarWars60.wav")
font = pygame.font.SysFont("Arial", 14)
text1=font.render(" PLAY ", True, white)
text2=font.render(" PAUSE ", True, white)
text3=font.render(" STOP ", True, white)
rect1 = text1.get_rect(topleft=(10,10))
rect2 = text2.get_rect(topleft= (100,10))
rect3 = text3.get_rect(topleft= (200,10))
bg = (127,127,127)
psmode=True
screen = pygame.display.set_mode((400,300))
screen.fill(bg)
while not done:
   for event in pygame.event.get():
      screen.blit(text1, rect1)
      pygame.draw.rect(screen, (255,0,0),rect1,2)
      screen.blit(text2, rect2)
      pygame.draw.rect(screen, (255,0,0),rect2,2)
      pygame.draw.rect(screen, (255,0,0),rect3,2)
      screen.blit(text3, rect3)

      if event.type == pygame.QUIT:
         done = True
      if event.type == pygame.MOUSEBUTTONDOWN:
         if rect1.collidepoint(event.pos):
            pygame.mixer.music.play()
         if rect2.collidepoint(event.pos):
            if psmode==True:
               pygame.mixer.music.pause()
               psmode=False
            else:
               if psmode==False:
                  pygame.mixer.music.unpause()
                  psmode=True
            if rect3.collidepoint(event.pos):
               pygame.mixer.music.stop()
   pygame.display.update()