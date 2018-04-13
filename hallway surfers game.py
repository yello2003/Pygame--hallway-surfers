#Smarties the candy-Jessica.N,Elianna.N,Angela.Z,Amy.H
#Hallway Surfers
#The objective of the game is to help the student to escape the halls of BHS.The
#character has to complete each level in order to escape.

from gamelib import*

game=Game(800,600,"Hallway Surfers")

bk=Image("bk.jpg",game)
bk.resizeTo(800,600)
game.setBackground(bk)
title=Image("hallways.jpeg",game)
title.resizeTo(800,600)
character=Image("chicken.gif",game)
character.resizeBy(-80)
character.moveTo(250,500)
janitor=Image("janitor.png",game,use_alpha=False)
arrowkeys=Image("keys.png",game,use_alpha=False)
arrowkeys.moveTo(150,500)
arrowkeys.resizeBy(-20)
f = Font(black,30,white,"Comic Sans MS")# a Font object
i=Font(black,18,white,"Georgia")
t=Font(black,70,white,"Arial")
y=Font(black,24,black,"Comic Sans MS")
s= Font(white,24,black,"Comic Sans MS")
electro=Sound("electro.wav",1)
oof=Sound("oof.wav",2)
yay=Sound("yay.wav",3)
guitar=Sound("guitar.wav",4)
wah=Sound("wahwah.wav",5)

books=[]
for index in range(25):
    books.append(Image("books.png",game,use_alpha=False))
    books[index].moveTo(randint(50,800),randint(-1500,0))
    books[index].resizeBy(-60)
    books[index].setSpeed(4,180)

oldteacher=[]
x=-150
y=randint(400,500)

for index in range(20):
    oldteacher.append(Image("oldteacher.gif",game,use_alpha=False))  
    oldteacher[index].moveTo(x,y)
    oldteacher[index].setSpeed(4,270)
    x-=150
    
test=[]
for index in range(20):
    test.append(Image("test.png",game,use_alpha=False))
    test[index].moveTo(randint(50,800),randint(-1000,0))
    test[index].resizeBy(-85)
    test[index].setSpeed(4,180)

#Title screen
title.draw()
game.drawText("HALLWAY SURFERS",100,150,t)
game.drawText("Press S KEY TO CONTINUE",450,500,i)
game.update()
game.wait(K_s)

title.draw()
guitar.play()
game.drawText("STORY",350,50,s)
game.drawText("You are trying to escape the class and your main goal is to ",50,100,s)
game.drawText("avoid the obstacles in the hallways.",25,125,s)
game.drawText("HOW TO PLAY",300,175,s)
game.drawText("Move the character using the arrow keys. Avoid the following ",50,225,s)
game.drawText("objects or you’ll lose health points:janitor-20;teacher - 15;failed ",25,250,s)
game.drawText("test grades -10. If you reach the books, you gain 5 health points,and ",25,275,s)
game.drawText("your score increase by 1! You win by earning the score of 15 and the ",25,300,s)
game.drawText("health must be more than 0.",25,325,s)
arrowkeys.draw()

#game.drawText("Use arrow keys to move the character",25,550,i)
game.drawText("(Press SPACEBAR to Start The Game)",400,550,i)
game.update()
game.wait(K_SPACE)


#Level one-First game loop
while not game.over:
    game.processInput()
    bk.draw()
    character.draw()
    electro.play()
    game.drawText("Level1",700,550)
    
     #character controls
    if keys.Pressed[K_RIGHT]:
        character.x +=10
    if keys.Pressed[K_LEFT]:
        character.x-=10
    if keys.Pressed[K_UP]:
        character.y-=10
    if keys.Pressed[K_DOWN]:
        character.y+=10
        
    for index in range(20):
        oldteacher[index].move()
        if character.collidedWith(oldteacher[index]):
           character.health-=15
           oof.play()
           oldteacher[index].visible=False           

    for index in range(25):
        books[index].move()
        if character.collidedWith(books[index]):
            character.health+=5
            books[index].visible=False
            game.score+=1

    for index in range (20):
        test[index].move()
        if character.collidedWith (test[index]):
            character.health-=10
            test[index].visible=False

    if character.health<=0 and game.score<=15:
        game.over=True
        game.drawText("YOU LOSE!  GO TO CLASS!",200,100,f)
        electro.play(False)
        wah.play()

    if character.health>=0 and game.score>=15:
        game.over=True
        game.drawText("YOU WIN!",300,100,f)
        electro.play(False)
        yay.play()
        
    game.drawText("Health: " + str(character.health),character.x-20, character.y+50)
    game.displayScore()
    game.update(10)
