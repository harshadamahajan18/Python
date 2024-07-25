# Install an external module

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()

import pygame
pygame.init()
screen = pygame.display.set_mode([500, 500])
running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
   screen.fill((255, 255, 255))
   pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
   pygame.display.flip()
pygame.quit()