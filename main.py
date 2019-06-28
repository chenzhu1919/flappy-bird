import sys,pygame,random
from bird import Bird
from pipe import Pipe
from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()
size = (width, height) = (int(screen_info.current_w),int(screen_info.current_h))
screen = pygame.display.set_mode(size)
background = pygame.image.load('background.png')
background = pygame.transform.scale(background,(width,height))
startPos = (width/8,height/2)

clock = pygame.time.Clock()
pipes = pygame.sprite.Group()
player = Bird(startPos)
gapSize = random.randint(80,200) #change to random
loopCount = 0

def lose():
    font = pygame.font.SysFont(None,70)
    loseground = pygame.image.load("loseground.png")
    loseground = pygame.transform.scale(loseground,(width,height))
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pipes.empty()
                    player.reset(startPos)
                    return


def main():
    global loopCount
    while True:
        clock.tick(45)
        if loopCount % 90 == 0:
            topPos = random.randint(0,height/2) - 400
            pipes.add(Pipe((width+100,topPos + gapSize +800)))
            pipes.add(Pipe((width+100,topPos),True))
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player.speed[1] = -10
        player.update()
        pipes.update()
        get_hit = pygame.sprite.spritecollide(player,pipes,False)\
            or player.rect.center[1] > height
        screen.blit(background,[0,0])
        pipes.draw(screen)
        screen.blit(player.image,player.rect)
        pygame.display.flip()
        loopCount +=1
        if get_hit:
            lose()
if __name__=="__main__":
    main()