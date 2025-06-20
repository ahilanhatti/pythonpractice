import pygame
class enemy:
    def __init__(self):
        pass
def update_physics ():
    global scroll, acc_x, acc_y, vel_x, vel_y, x, y, state
    vel_x += acc_x
    if vel_x > maxvel_x:
        vel_x = maxvel_x
    if vel_x < -maxvel_x:
        vel_x = -maxvel_x
    if state == 'on ground' and vel_x != 0.0:
        if vel_x < 0:
            vel_x += 1.0
        else:
            vel_x -= 1.0
    vel_y += acc_y
    if vel_y > maxvel_y:
        vel_y = maxvel_y
    if vel_y < -maxvel_y:
        vel_y = -maxvel_y
    x += vel_x
    rect = pygame.Rect(x,y,30,30)
    for i,block in enumerate (blocks):
        while block.colliderect(rect) == True:
            if blocktypes[i] == "bad":
                if not block.colliderect (rect.inflate(-5,-5)):
                    break
                state = 'in air'
                x=100.0
                y=100.0
                vel_x = 0.0
                vel_y = 0.0
                acc_x = 0.0
                acc_y = 10.0
                scroll = 0.0
                return
            if vel_x > 0:
                x-=1.0
            else:
                x+=1.0
            rect = pygame.Rect(x,y,30,30)
    if x < 0:
        x = 0.0
        vel_x=0.0
        acc_x=0.0
    y += vel_y
    rect = pygame.Rect(x,y,30,30)
    for i,block in enumerate (blocks):
        while block.colliderect(rect) == True:
            if blocktypes[i] == "bad":
                if not block.colliderect (rect.inflate(-5,-5)):
                    break
                state = 'in air'
                x=100.0
                y=100.0
                vel_x = 0.0
                vel_y = 0.0
                acc_x = 0.0
                acc_y = 10.0
                scroll = 0.0
                return
            if vel_y > 0:
                y-=1.0
                state = 'on ground'
            else:
                y+=1.0
            rect = pygame.Rect(x,y,30,30)
    if y>470:
        state = 'on ground'
        y=470.0
pygame.init ()
screen = pygame.display.set_mode([800,600])
blocks = []
blocktypes = []
with open ("block.text", "r") as file:
    for line in file:
        line = line.strip ()
        values = line.split ()
        left = int(values [0])
        top = int(values [1])
        width = int(values [2])
        height = int(values [3])
        block = pygame.Rect(left,top,width,height)
        blocks.append (block)
        blocktypes.append (values [4])
triangleimage = pygame.image.load ("Triangle.png")
running=True
state = 'in air'
x=100.0
y=100.0
vel_x = 0.0
vel_y = 0.0
acc_x = 0.0
acc_y = 10.0
maxvel_x = 15.0
maxvel_y = 50.0
scroll = 0.0
while running==True:
    screen.fill((192,192,192))
    if x > 400+scroll:
        scroll += x-(400+scroll)
    if x < 350+scroll:
        scroll -= 350+scroll-x
    if scroll < 0:
        scroll = 0.0
    for i,block in enumerate (blocks):
        if blocktypes [i] == "good":
            pygame.draw.rect(screen, (0,0,255), block.move(-scroll, 0))
        elif blocktypes[i] == "bad":
            # pygame.draw.rect(screen, (0,255,0), block.move(-scroll, 0))
            scaledimage = pygame.transform.scale (triangleimage, (block.width, block.height))
            screen.blit (scaledimage, block.move(-scroll, 0))
    rect = pygame.Rect(x,y,30,30)
    pygame.draw.rect(screen,(255,0,0),rect.move(-scroll,0))
    ground=pygame.Rect(0,500,800,13)
    pygame.draw.rect(screen,(0,255,0), ground)
    pygame.display.flip()
    pygame.time.delay(50)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        acc_x=-2.0
    elif keys[pygame.K_d]:
        acc_x=2.0
    else:
        acc_x = 0.0
    if keys[pygame.K_w] and state != 'in air':
        vel_y=-50.0
        state = 'in air'
    if keys[pygame.K_s]:
        y+=1.0
    update_physics ()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()