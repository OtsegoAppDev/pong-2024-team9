import pygame as pygame


def drawCenterLine():
    global screenWidth, screenHeight
    pygame.draw.line(window, white, (screenWidth//2, 0), (screenWidth//2, screenHeight))

def resetBall():
    if ballLocation[0] >= 1000:
        ballLocation[0] = 500
        ballLocation[1] = 400
    if ballLocation[0] <= 0:
        ballLocation[0] = 500
        ballLocation[1] = 400
    if ballLocation[1] <= 0:
        ballLocation[0] = 500
        ballLocation[1] = 400
    if ballLocation[1] >= 800:
        ballLocation[0] = 500
        ballLocation[1] = 400

def drawScore(font):
    global scoreA, scoreB, ballLocation, ballSpeedx, ballSpeedy, scoreC, scoreD
    
    text = font.render(str(scoreA), True, white)
    window.blit(text, (100,300))
    text = font.render(str(scoreB), True, white)
    window.blit(text, (900,300))
    text = font.render(str(scoreC), True, white)
    window.blit(text, (500,100))
    text = font.render(str(scoreD), True, white)
    window.blit(text, (500,750))
    if ballLocation[0] <= 0:
        scoreB = scoreB + 1
    if ballLocation[0] >= 1000:
        scoreA = scoreA + 1
    if ballLocation[1] >= 800:
        scoreC = scoreC + 1
    if ballLocation[1] <= 0:
        scoreD = scoreD + 1
    if scoreA == 10:
            ballSpeedx = 0
            ballSpeedy = 0
            ballLocation[1] = 350
            ballLocation[0] = 350
            text = fontB.render("Player1 wins", True, white)
            window.blit(text, (250,100))
    if scoreB == 10:
            ballSpeedx = 0
            ballSpeedy = 0
            ballLocation[1] = 350
            ballLocation[0] = 350
            text = fontB.render("Player2 wins", True, white)
            window.blit(text, (250,100))
    if scoreC == 10:
            ballSpeedx = 0
            ballSpeedy = 0
            ballLocation[1] = 350
            ballLocation[0] = 350
            text = fontB.render("Player3 wins", True, white)
            window.blit(text, (250,100))
    if scoreD == 10:
            ballSpeedx = 0
            ballSpeedy = 0
            ballLocation[1] = 350
            ballLocation[0] = 350
            text = fontB.render("Player4 wins", True, white)
            window.blit(text, (250,100))       
def MoveBall():
    global ballSpeedx, ballSpeedy, ballLocation, ball
    """
    This function will move the ball
    """
    if ballLocation[0] > screenWidth:
        ballSpeedx = -ballSpeedx
    if ballLocation[1] >= screenHeight:
        ballSpeedy = -ballSpeedy
    if ballLocation[0] <= 0:
        ballSpeedx = -ballSpeedx
    if ballLocation[1] <= 0:
        ballSpeedy = -ballSpeedy
    ballLocation[0] = ballLocation[0] + ballSpeedx
    ballLocation[1] = ballLocation[1] + ballSpeedy
    ball = pygame.draw.circle(window, white, ballLocation, radius, 0)

def MovePaddle():
    global PadASpeed, PadA, PadB, PadBSpeed, PadC, PadCSpeed, PadD, PadDSpeed
    if PadA.top <= 0:
        PadA = PadA.move(0,2)
        PadASpeed = 0
    if PadB.top <= 0:
        PadB = PadB.move(0,2)
        PadBSpeed = 0
    if PadC.topleft[0] <= 0:
        PadC = PadC.move(2,0)
        PadCSpeed = 0
    if PadD.bottomleft[0] <= 0:
        PadD = PadC.move(2,0)
        PadDSpeed = 0 
    
    if PadA.bottom >= 800:
        PadA = PadA.move(0,-2)
        PadASpeed = 0
    if PadB.bottom >= 800:
        PadB = PadB.move(0,-2)
        PadBSpeed = 0
    if PadC.topright[0] >= 1000:
        PadC = PadC.move(-2,0)
        PadCSpeed = 0
    if PadD.bottomright[0] >= 1000:
        PadD = PadD.move(-2,0)
        PadDSpeed = 0
    PadA = PadA.move (0,PadASpeed)
    pygame.draw.rect(window, white, PadA)
    PadB = PadB.move (0,PadBSpeed)
    pygame.draw.rect(window, white, PadB)
    PadC = PadC.move (PadCSpeed, 0)
    pygame.draw.rect(window, white, PadB)
    PadD = PadD.move (PadDSpeed, 0)
    pygame.draw.rect(window, white, PadB)
    PadA = PadA.move(0, PadASpeed)
    PadB = PadB.move(0, PadBSpeed)
    PadC = PadC.move(PadCSpeed, 0)
    PadD = PadD.move(PadDSpeed, 0)
    pygame.draw.rect(window, red, PadA)
    pygame.draw.rect(window, random, PadB)
    pygame.draw.rect(window, blue, PadC)
    pygame.draw.rect(window, white, PadD)
    

timer = pygame.time.Clock()

screenWidth = 1000
screenHeight = 800

window = pygame.display.set_mode([screenWidth, screenHeight])

ballSpeedx = 9
ballSpeedy = 6
black = (0,0,0)
white = (255,255,255)
random = (23,178,43)
red = (200,10,32)
blue = (0,0,200)
radius = 22
scoreA = 0
scoreB = 0
scoreC = 0
scoreD = 0
ballLocation = [500, 300]
ball = pygame.Rect(ballLocation, (radius, radius))
pygame.font.init()
font = pygame.font.Font(None,50)
fontB = pygame.font.Font(None,150)
PadA = pygame.Rect((0,250), (20,100))
PadB = pygame.Rect((980,250), (20,100))
PadC = pygame.Rect((500,0), (100,20))
PadD = pygame.Rect((500,780), (100,20))
PadASpeed = 0
PadBSpeed = 0
PadCSpeed = 0
PadDSpeed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                PadASpeed = -2
            if event.key == pygame.K_s:
                PadASpeed = 2
            if event.key == pygame.K_UP:
                PadBSpeed = -2
            if event.key == pygame.K_DOWN:
                PadBSpeed = 2
            if event.key == pygame.K_c:
                PadCSpeed = -2
            if event.key == pygame.K_b:
                PadCSpeed = 2
            if event.key == pygame.K_i:
                PadDSpeed = -2
            if event.key == pygame.K_p:
                PadDSpeed = 2
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                PadBSpeed = 0
            if event.key == pygame.K_DOWN:
                PadBSpeed = 0
            if event.key == pygame.K_w:
                PadASpeed = 0
            if event.key == pygame.K_s:
                PadASpeed = 0
            if event.key == pygame.K_c:
                PadCSpeed = 0
            if event.key == pygame.K_b:
                PadCSpeed = 0
            if event.key == pygame.K_i:
                PadDSpeed = 0
            if event.key == pygame.K_p:
                PadDSpeed = 0
        
        
    if PadA.colliderect(ball):
        ballSpeedx = -ballSpeedx
    if PadB.colliderect(ball):
        ballSpeedx = -ballSpeedx
    if PadC.colliderect(ball):
        ballSpeedy = -ballSpeedy
    if PadD.colliderect(ball):
        ballSpeedy = -ballSpeedy
    timer.tick(60)
    window.fill(black)
    drawCenterLine()
    drawScore(font)
    MoveBall()
    MovePaddle()
    pygame.display.flip()
    
    #check quit event
    #check up, down, spacebar event