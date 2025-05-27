import pygame
def update_physics ():
    global acc_x, acc_y, vel_x, vel_y, x, y, state
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
    while block.colliderect(rect) == True:
        if vel_x > 0:
            x-=1.0
        else:
            x+=1.0
        rect = pygame.Rect(x,y,30,30)
    y += vel_y
    rect = pygame.Rect(x,y,30,30)
    while block.colliderect(rect) == True:
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
with open ("block.text", "r") as file:
    line = file.readline ()
    line = line.strip ()
    values = line.split ()
    left = int(values [0])
    top = int(values [1])
    width = int(values [2])
    height = int(values [3])
block = pygame.Rect(left,top,width,height)
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
while running==True:
    screen.fill((192,192,192))
    pygame.draw.rect(screen, (0,0,255), block)
    rect = pygame.Rect(x,y,30,30)
    pygame.draw.rect(screen,(255,0,0),rect)
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