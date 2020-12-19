import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('car.png')
carImg2 = pygame.image.load('car2.png')
Ball_Img = pygame.image.load('ball.png')
    
def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def car2(x,y):
    gameDisplay.blit(carImg2, (x,y))

def Ball(x,y):
    gameDisplay.blit(Ball_Img, (x,y))

x =  (display_width * 0.5)
y = (display_height * 0.5)	#1
x2 =  (display_width * 0.5)
y2 = (display_height * 0.8)	#1
x_ball =(display_width * 0.45)
y_ball =(display_height * 0.4)
x_change = 0
y_change = 0
x2_change = 0
y2_change = 0
ball_x_change = 0
ball_y_change = 0
#spawn = False
car_speed = 0
car2_speed = 0
ball_speed = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0
        ######################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x2_change = -5
            elif event.key == pygame.K_d:
                x2_change = 5
            elif event.key == pygame.K_w:
                y2_change = -5
            elif event.key == pygame.K_s:
                y2_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                x2_change = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                y2_change = 0
        ######################
    ##
    x += x_change
    y += y_change
    x2 += x2_change
    y2 += y2_change
    ##         
    gameDisplay.fill(white)
    if abs(x+5-x_ball-65)<=5+65 and abs(y+100-y_ball-65)<=100+65:
        if x_ball-x>0:
            ball_x_change = 5
        else:
            ball_x_change = -5
        if y_ball-y>0:
            ball_y_change = 5	#-(x_ball+64)=-x_ball-64
        else:
            ball_y_change = -5
    if abs(x2+5-x_ball-65)<=5+65 and abs(y2+100-y_ball-65)<=100+65:
        if x_ball-x2>0:
            ball_x_change = 5
        else:
            ball_x_change = -5
        if y_ball-y2>0:
            ball_y_change = 5
        else:
            ball_y_change = -5
    x_ball += ball_x_change
    y_ball += ball_y_change

    if x_ball > display_width:
        x_ball=ball_x_change=-5
    if x_ball < 0:
        x_ball = display_width
    if y_ball > display_height:
        ball_y_change=-5
    if y_ball < 0:
        ball_y_change = 5
        
    car(x,y)
    car2(x2, y2)
    Ball(x_ball,y_ball)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()