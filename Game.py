import pygame
def update_physics ():
    global acc_x, acc_y, vel_x, vel_y, x, y
    vel_x += acc_x
    if vel_x > maxvel_x:
        vel_x = maxvel_x
    if vel_x < -maxvel_x:
        vel_x = -maxvel_x
    vel_y += acc_y
    if vel_y > maxvel_y:
        vel_y = maxvel_y
    if vel_y < -maxvel_y:
        vel_y = -maxvel_y
    x += vel_x
    y += vel_y
    if y>470:
        y=470.0
pygame.init ()
screen = pygame.display.set_mode([800,600])
running=True
x=100.0
y=100.0
vel_x = 0.0
vel_y = 0.0
acc_x = 0.0
acc_y = 10.0
maxvel_x = 15.0
maxvel_y = 70.0
while running==True:
    screen.fill((192,192,192))
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
    if keys[pygame.K_w]:
        vel_y=-50.0
    if keys[pygame.K_s]:
        y+=1.0
    update_physics ()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()