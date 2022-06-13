import pygame as pyg
import os
import random

WIDTH, HEIGHT = 640,360
WIN = pyg.display.set_mode((WIDTH,HEIGHT))
pyg.display.set_caption("MathQuest")
pyg.font.init()
TEXT = pyg.font.SysFont('Arial', 20)
END_TEXT = pyg.font.SysFont('Arial', 30)

FPS = 60

LEVEL = pyg.transform.scale(pyg.image.load(os.path.join('Assets','level.png')), (640,360))
PLAYER = pyg.transform.scale(pyg.image.load(os.path.join('Assets','player.png')),(40,60))
MATHQUEST = pyg.transform.scale(pyg.image.load(os.path.join('Assets','mathquest.png')),(178,30))
TITLE = pyg.image.load(os.path.join('Assets','title.png'))
END =  pyg.image.load(os.path.join('Assets','score_screen.png'))

ENEMY = None

WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)

#Events

TIME_UP = pyg.USEREVENT + 1


def draw_window(player,monster,playerAnswer,score,timeLeft):
    WIN.blit(LEVEL, (0,0))
    WIN.blit(PLAYER, (player.x,player.y))
    WIN.blit(MATHQUEST, (10,10))
    WIN.blit(monster.image, (monster.coords.x,monster.coords.y))
    question = TEXT.render(
        str(monster.question), 1, WHITE
    )
    if playerAnswer == "":
         answer = TEXT.render(
        "_", 1, RED
    )
    else:
        answer = TEXT.render(
            str(playerAnswer), 1, RED
        )
    theScoreTitle = TEXT.render(
        "SCORE: ", 1, WHITE
    )
    theScore = TEXT.render(
        str(score),1, GREEN
    )
    timeTitle = TEXT.render(
        "TIME LEFT: ", 1, WHITE
    )
    timer = TEXT.render(
        str(timeLeft), 1, WHITE
    )
    WIN.blit(timeTitle, (player.x - 70, 320))
    WIN.blit(timer, (player.x + 40, 320))
    WIN.blit(theScoreTitle, (100,45))
    WIN.blit(theScore, (180, 45))
    WIN.blit(question, (355, 320))
    WIN.blit(answer,(450, 320))
    pyg.display.update()

def draw_end(score):
    WIN.blit(END,(0,0))
    theScore = END_TEXT.render(
        str(score), 1, GREEN
    )
    WIN.blit(theScore, (424,202))
    pyg.display.update()

class Enemy:
    def __init__(self):
        result = random.randint(1,3)
        if result == 1 :
            x = random.randint(1,10)
            y = random.randint(1,10)
            self.question = F'{x} x {y} = '
            self.answer = x * y
            self.text = "MULTIPLICATION MUSHROOM!"
            self.alive = True
            self.coords = pyg.Rect(400,210,54,78)
            self.image = pyg.transform.scale(pyg.image.load(os.path.join('Assets/Enemies','shroom.png')),(54,78))

        if result == 2 :
            x = random.randint(1,15)
            y = random.randint(1,15)
            self.question = F'{x} - {y} = '
            self.answer = x - y
            self.text = "SUBTRACTION SKELETON!"
            self.alive = True
            self.coords = pyg.Rect(400,230,54,60)
            self.image = pyg.transform.scale(pyg.image.load(os.path.join('Assets/Enemies','skeleton.png')),(54,60))

        if result == 3 :
            x = random.randint(1,15)
            y = random.randint(1,15)
            self.question = F'{x} + {y} = '
            self.answer = x + y
            self.text = "ADDITION GOBLIN!"
            self.alive = True
            self.coords = pyg.Rect(400,230,54,59)
            self.image = pyg.transform.scale(pyg.image.load(os.path.join('Assets/Enemies','goblin.png')),(54,59))
            

def handle_input(keys_pressed,playerAnswer):
    if keys_pressed[pyg.K_0]:
        playerAnswer += "0"
    if keys_pressed[pyg.K_1]:
        playerAnswer += "1"
    if keys_pressed[pyg.K_2]:
        playerAnswer += "2"
    if keys_pressed[pyg.K_3]:
        playerAnswer += "3"
    if keys_pressed[pyg.K_4]:
        playerAnswer += "4"    
    if keys_pressed[pyg.K_5]:
        playerAnswer +=  "5" 
    if keys_pressed[pyg.K_6]:
        playerAnswer += "6"  
    if keys_pressed[pyg.K_7]:
        playerAnswer +=  "7" 
    if keys_pressed[pyg.K_8]:
        playerAnswer +=  "8"  
    if keys_pressed[pyg.K_9]:
        playerAnswer +=  "9"  
    if keys_pressed[pyg.K_MINUS]:
        playerAnswer += "-"

    if keys_pressed[pyg.K_BACKSPACE]:
        if playerAnswer != "":
            playerAnswer = playerAnswer[:-1]

    return playerAnswer

def draw_title():
    WIN.blit(TITLE, (0,0))
    pyg.display.update()

def main():
    player = pyg.Rect(190,228,30,20)
    score = 0
    run = True
    clock = pyg.time.Clock()
    playerAnswer = str("")
    monster = Enemy()
    menu = True
    done = False
    while run:
        clock.tick(FPS)


        ## Main Menu Here ##
        while menu:
            draw_title()
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    run=False
                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_RETURN:
                        menu=False
                        #Start timer when game begins.
                        start_ticks=pyg.time.get_ticks()
        ## Main Menu END ##



        ## Main Game ##

        timeLeft = round(30 - (pyg.time.get_ticks()-start_ticks)/1000, 1)

        if timeLeft <= 0 :
            done = True
        

        for event in pyg.event.get():

            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_RETURN:
                    if int(playerAnswer) == monster.answer :
                        score +=1
                        playerAnswer = ""
                        monster = Enemy()
                        
                keys_pressed = pyg.key.get_pressed()
                playerAnswer = handle_input(keys_pressed,playerAnswer)

            if event.type == pyg.QUIT:
                run=False

        print(playerAnswer)
        if not done:
            draw_window(player,monster,playerAnswer,score,timeLeft)
        else: draw_end(score)
        

main()