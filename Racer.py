import pygame  # if cannot import see install library in pycharm
pygame.init()  # important calls all init function, import doesnt call all pygame modules
import time
import random

crash_sound = pygame.mixer.Sound("Crash.wav")
#pygame.mixer.music.load("Retro.wav")


display_width = 800
display_height = 600

black = (0, 0, 0)  # RGB
white = (255, 255, 255)
red = (182, 67, 59)
firebrick = (178, 34, 34)
turq = (12, 247, 216)
grey = (14, 112, 198)
green = (59, 182, 104)
blue = (25, 99, 247)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)


pause = False

gameDisplay = pygame.display.set_mode((display_width, display_height))  # accepts a tuple as input

carImg1 = pygame.image.load('car3.png')  # loads image
pygame.display.set_caption("Racer")  # Title of window
pygame.display.set_icon(carImg1)
clock = pygame.time.Clock()  # specific game clock,keep track of time
carImg = pygame.image.load('car2.png')
backgroundimg = pygame.image.load("background_image.png").convert()  # reduces lag


def things_dodged(count):
    font = pygame.font.SysFont(None, 35)
    text = font.render("Dodged: " + str(count), True, turq)
    gameDisplay.blit(text, (5, 0))


def back_ground():
    gameDisplay.blit(backgroundimg, (-5, 0))


def car(x, y):  # function to display car
    gameDisplay.blit(carImg, (x, y))  # draw image,requires shape and tuple with x,y coordinates


def things(thingx, thingy, thingw, thingh, color):  # for objects on the road
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])  # first para is surface where to place rect


def text_objects(text, font):
    textSurface = font.render(text, True, black)  # render text,black words
    return textSurface, textSurface.get_rect()  # to get the rectangle around our text


def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 95)
    TextSurf, TextRect = text_objects(text, largeText)  # text aka Textsurf can be referenced by the rect surrounding it
    TextRect.center = ((display_width / 2), (display_height / 2))  # centers the rect,.center is a function of get_rect
    gameDisplay.blit(TextSurf, TextRect)  # to put things on screen
    pygame.display.update()  # updates the screen
    time.sleep(1)
    game_loop()

def quitgame():
    pygame.quit()
    quit()


def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        back_ground()
        #message_display("YOU CRASHED")
        largeText = pygame.font.Font("freesansbold.ttf", 95)
        pygame.draw.rect(gameDisplay,firebrick,(25,230,750,120))
        TextSurf, TextRect = text_objects("YOU CRASHED!",largeText)  # text aka Textsurf can be referenced by the rect surrounding it
        TextRect.center = ((display_width / 2), (display_height / 2))  # centers the rect,.center is a function of get_rect
        gameDisplay.blit(TextSurf, TextRect)  # to put things on screen

        button("PLAY AGAIN", 250, 450, 125, 50, green, bright_green,game_loop)  #dont want to restart game loop
        button("EXIT", 425, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()  # updates the screen
        clock.tick(15)  #makes the loop for 15 secs
        #pygame.time.wait(1000)
        #intro = False

def button(msg,x,y,w,h,inactivecolor, activecolor,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()  #if left button is clicked the o become 1 (1,0,0) from (0,0,0)

    # #buttons
    if x + w > mouse[0] > x and y + h > mouse[1] > y:  # mouse within the rect
        pygame.draw.rect(gameDisplay, activecolor, (x, y, w, h))  # x,y,width,height
        if  click[0] == 1 and action != None:
            action()  #make the variable into a function game_loop = game_loop()
    else:
        pygame.draw.rect(gameDisplay, inactivecolor, (x, y, w, h))  # x,y,width,height




    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def paused():

    pygame.mixer.music.pause()

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        back_ground()
        largeText = pygame.font.Font("freesansbold.ttf", 95)
        pygame.draw.rect(gameDisplay,firebrick,(225,230,350,120))
        TextSurf, TextRect = text_objects("Paused",largeText)  # text aka Textsurf can be referenced by the rect surrounding it
        TextRect.center = ((display_width / 2), (display_height / 2))  # centers the rect,.center is a function of get_rect
        gameDisplay.blit(TextSurf, TextRect)  # to put things on screen

        button("CONT", 275, 450, 100, 50, green, bright_green,unpause)  #dont want to restart game loop
        button("EXIT", 425, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()  # updates the screen
        clock.tick(5)  #makes the loop for 15 secs
        #pygame.time.wait(1000)
        #intro = False

def unpause():
    pygame.mixer.music.unpause()
    global pause
    pause = False

def game_intro():
    intro = True
    pygame.mixer.music.load("Yeah.wav")
    pygame.mixer.music.play(-1)  # -1 to play music infinitely

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        back_ground()
        largeText = pygame.font.Font("freesansbold.ttf", 95)
        pygame.draw.rect(gameDisplay,blue,(265,230,280,120))
        TextSurf, TextRect = text_objects("Racer",largeText)  # text aka Textsurf can be referenced by the rect surrounding it
        TextRect.center = ((display_width / 2), (display_height / 2))  # centers the rect,.center is a function of get_rect
        gameDisplay.blit(TextSurf, TextRect)  # to put things on screen

        button("START", 275, 450, 100, 50, green, bright_green,game_loop)
        button("EXIT", 425, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()  # updates the screen
        clock.tick(5)  #makes the loop for 15 secs
        #pygame.time.wait(1000)
        #intro = False


def game_loop():
    global pause
    pygame.mixer.music.load("Retro.wav")
    pygame.mixer.music.play(-1) #-1 to play music infinitely
    x = (display_width * 0.45)
    y = (display_height * .75)

    x_change = 0

    thing_startx = random.randrange(0, 737)
    thing_starty = -600  # off-screen so that they can move down
    thing_width = random.randrange(100, 500)  # create random boxes
    thing_height = 100
    thing_speed = 7

    gameExit = False  # car crashed
    dodged = 0

    # Main game loop, car can do things when it havent crash
    while not gameExit:

        # event handling loop
        for event in pygame.event.get():  # gets all events that are happening on screen per frame per second
            if event.type == pygame.QUIT:  # if event is Quit, aka someone pressed X
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -8
                elif event.key == pygame.K_RIGHT:
                    x_change = 8
                    # xchange will carry on adding even when key not pressed so do key up
                elif event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        # game logic, example collision
        if x >= 737:
            x = 737
            crash()
        if x <= 0:
            x = 0
            crash()

        if thing_starty > display_height:  # box goes offscreen
            thing_starty = 0 - thing_height  # to make box immediately show up not at 0 but offscreen
            thing_startx = random.randrange(0, 737)
            thing_width = random.randrange(100, 500)  # create random boxes
            dodged += 1
            if dodged > 2:
                thing_speed = 9
            elif dodged > 5:
                thing_speed = 10
            elif dodged > 7:
                thing_speed = 12

        # collision check
        if y < thing_starty + thing_height:  # the bottom left corner of the box crosses the top right range of car

            if thing_startx - 12 < x < thing_startx + thing_width:  # 12 is car width, and car height
                crash()

        # print(event)  #prints all events,not important
        back_ground()
        # gameDisplay.fill(white) #fill background first,before car

        # draw rect'
        things(thing_startx, thing_starty, thing_width, thing_height, grey)
        # now only want to change y since moving on y, not x or change shape
        thing_starty += thing_speed

        car(x, y)  # calling car function to draw car
        things_dodged(dodged)  # call out the dodged function
        pygame.display.update()  # updates the screen
        clock.tick(60)  # fps, runs through the loop at 60 times in one second, taxing, how often while loop should run

game_intro()
game_loop()
pygame.quit()  # end pygame instance
quit()  # exit python
