import pygame as pygame


def drawCenterLine():
    global screenWidth, screenHeight
    pygame.draw.line(window, white, (screenWidth//2, 0), (screenWidth//2, screenHeight))

def drawScore(font):
    global scoreA, scoreB, ballLocation, ballSpeedx, ballSpeedy
    
    text = font.render(str(scoreA), True, white)
    window.blit(text, (200,300))
    text = font.render(str(scoreB), True, white)
    window.blit(text, (700,300))
    if ballLocation[0] <= 0:
        scoreB = scoreB + 1
    if ballLocation[0] >= 1000:
        scoreA = scoreA + 1
    if scoreA == 10:
            ballSpeedx = 0
            ballSpeedy = 0
            ballLocation[0] = 350
            text = fontB.render("Player1 wins", True, white)
            window.blit(text, (200,100))
    if scoreB == 10:
            ballSpeedx = 0
            ballSpeedy = 0
            ballLocation[0] = 350
            text = fontB.render("Player2 wins", True, white)
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
    if ballLocation[0] < 0:
        ballSpeedx = -ballSpeedx
    if ballLocation[1] <= 0:
        ballSpeedy = -ballSpeedy
    ballLocation[0] = ballLocation[0] + ballSpeedx
    ballLocation[1] = ballLocation[1] + ballSpeedy
    ball = pygame.draw.circle(window, white, ballLocation, radius, 0)

def MovePaddle():
    global PadASpeed, PadA, PadB, PadBSpeed
    if PadA.top <= 0:
        PadA = PadA.move(0,2)
        PadASpeed = 0
    if PadB.top <= 0:
        PadB = PadB.move(0,2)
        PadBSpeed = 0
    if PadA.bottom >= 600:
        PadA = PadA.move(0,-2)
        PadASpeed = 0
    if PadB.bottom >= 600:
        PadB = PadB.move(0,-2)
        PadBSpeed = 0    
    PadA = PadA.move (0,PadASpeed)
    pygame.draw.rect(window, white, PadA)
    PadB = PadB.move (0,PadBSpeed)
    pygame.draw.rect(window, white, PadB)
    PadA = PadA.move(0, PadASpeed)
    PadB = PadB.move(0, PadBSpeed)
    pygame.draw.rect(window, red, PadA)
    pygame.draw.rect(window, random, PadB)

timer = pygame.time.Clock()

screenWidth = 1000
screenHeight = 600

window = pygame.display.set_mode([screenWidth, screenHeight])

ballSpeedx = 101
ballSpeedy = 6
black = (0,0,0)
white = (255,255,255)
random = (23,178,43)
red = (200,10,32)
radius = 22
scoreA = 0
scoreB = 0
ballLocation = [500, 300]
ball = pygame.Rect(ballLocation, (radius, radius))
pygame.font.init()
font = pygame.font.Font(None,50)
fontB = pygame.font.Font(None,150)
PadA = pygame.Rect((0,250), (20,100))
PadB = pygame.Rect((980,250), (20,100))
PadASpeed = 0
PadBSpeed = 0


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
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                PadBSpeed = 0
            if event.key == pygame.K_DOWN:
                PadBSpeed = 0
            if event.key == pygame.K_w:
                PadASpeed = 0
            if event.key == pygame.K_s:
                PadASpeed = 0
        
        
    if PadA.colliderect(ball):
        ballSpeedx = -ballSpeedx
    if PadB.colliderect(ball):
        ballSpeedx = -ballSpeedx
    timer.tick(60)
    window.fill(black)
    drawCenterLine()
    drawScore(font)
    MoveBall()
    MovePaddle()
    pygame.display.flip()
    
    #check quit event
    #check up, down, spacebar event