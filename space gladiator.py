 
from gamelib import*#imports the game library of classes and functions
game = Game(1000,800,"space gladiator")#game object
bk = Image("space.jpg",game)#image object
bk.resizeTo(1000,800)
alien = Animation("alien.gif",4,game,55,55,frate=6,use_alpha= False)
alien.resizeBy(350)
alien.setSpeed(3,90)#set speed in order to move
spaceman = Animation("space man.jpg",6,game,196,196,frate=6,use_alpha= False)
spaceman.resizeBy(-50)
spaceman.setSpeed(0,0) 
monster = Animation("monster.gif",1,game,512,384,frate=6,use_alpha= False)
monster.setSpeed(2,30) 
monster.resizeBy(10)
fireball = Animation("fireball.jpg",4,game,128,128,frate=4,use_alpha= False)
fireball.visible = False
youwin = Image("game over.png",game,use_alpha= False)
#Title Screen
logo = Image("logo.png",game,use_alpha= False)#opening screen variable
bk.draw()
logo.draw()
gameover = Image("game over.png",game)
youwin = Image("you win.png",game)
youwin.resizeBy(-50)
game.drawText("Press the SPACE BAR to start",100,270)#pass the variable f
game.update()
game.wait(K_SPACE)

  
    #Level 1
game.over = False #if False, opens next level
while not game.over:#while loop runs until game is over
    game.processInput()
    bk.draw()
    alien.move(True)
    spaceman.move(True)
    fireball.move()


    if alien.collidedWith(spaceman):#if statement
        spaceman.health-=0.5#action if true
        
        
        
    if fireball.collidedWith(alien):
            alien.health -= 5
            alien.moveTo(randint(100,700),randint(100,700))
            if alien.health < 1:
                game.over = True
  # spaceman Control
    if keys.Pressed[K_SPACE]:
        fireball.moveTo(spaceman.x+100, spaceman.y)
        fireball.setSpeed(24,270)
        fireball.visible = True
    if keys.Pressed[K_UP]:
        spaceman.move(True)
        spaceman.y -= 8
    if keys.Pressed[K_DOWN]:
        spaceman.move(True)
        spaceman.y += 8
    if keys.Pressed[K_RIGHT]:
        spaceman.move(True)
        spaceman.x += 8
    if keys.Pressed[K_LEFT]:
        spaceman.move(True)
        spaceman.x -= 8
    if spaceman.health < 0.1:
        alien.setSpeed(0,0)
        spaceman.visible = False
        gameover.draw()
        game.drawText("Press the SPACE BAR to quit",400,500)#pass the variable f
        game.update()
        game.wait(K_SPACE)
        if keys.Pressed[K_SPACE]:
            game.over = True
    if alien.health < 0.1:
        alien.setSpeed(0,0)
        alien.visible = False
        youwin.draw()
        game.drawText("Press the SPACE BAR level 2",400,500)#pass the variable f
        game.update()
        game.wait(K_SPACE)
        if keys.Pressed[K_SPACE]:
            game.over = True    



         
    game.drawText("Health: " + str(spaceman.health),spaceman.x - 20,spaceman.y + 100)
    game.drawText("Health: " + str(alien.health),alien.x - 20,alien.y + 100)
    game.update(60)


    
 #Level 2
game.over = False
while not game.over and spaceman.health > 1:
    game.processInput() 
    #game.clearBackground(cyan)
    game.drawText("Level 2", 200,200)
    bk.draw() 
    spaceman.draw()
    monster.draw()
    monster.move() 
    fireball.move() 

    
    if monster.collidedWith(spaceman):#if statement
        spaceman.health-=1#action if true
        
        
        
    if fireball.collidedWith(monster):
            monster.health -= 5
            monster.moveTo(randint(100,700),randint(300,700))
            if monster.health < 1:
                game.over = True

  # spaceman Control
    
    if keys.Pressed[K_UP]:
        spaceman.move(True)
        spaceman.y -= 8
    if keys.Pressed[K_DOWN]:
        spaceman.move(True)
        spaceman.y += 8
    if keys.Pressed[K_RIGHT]:
        spaceman.move(True)
        spaceman.x += 8
    if keys.Pressed[K_LEFT]:
        spaceman.move(True)
        spaceman.x -= 8
    if spaceman.health < 0.1:
        monster.setSpeed(0,0)
        spaceman.visible = False
        gameover.draw() 
        game.drawText("Press the SPACE BAR to quit",400,500)#pass the variable f
        game.update()
        game.wait(K_SPACE)
        if keys.Pressed[K_SPACE]:
            game.over = True
    if monster.health < 0.1:
        monster.setSpeed(0,0)
        monster.visible = False
        youwin.draw()
        game.drawText("Press to end game",400,500)#pass the variable f
        game.update()
        game.wait(K_SPACE)
        if keys.Pressed[K_SPACE]:
            game.over = True    

    if keys.Pressed[K_SPACE]:
        fireball.moveTo(spaceman.x+100, spaceman.y)
        fireball.setSpeed(24,270)
        fireball.visible = True

    game.drawText("Health: " + str(spaceman.health),spaceman.x - 20,spaceman.y + 100)
    game.drawText("Health: " + str(monster.health),monster.x - 20,monster.y + 100)
    game.update(60)
    
game.quit()
#ending screen



       



     
 
