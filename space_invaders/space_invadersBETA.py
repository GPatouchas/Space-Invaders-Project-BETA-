# Space invaders game


import turtle
import math
import platform


#screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("~/Desktop/space_invaders/backround.gif")
wn.tracer(0)

#Register the shapes
wn.register_shape("~/Desktop/space_invaders/invader.gif")
wn.register_shape("~/Desktop/space_invaders/player.gif")


#drawing border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300) 
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)

border_pen.hideturtle()

#Set the score to 0
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 275)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()


#Creating the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("~/Desktop/space_invaders/player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
player.speed = 0

#choose a number of enemies
number_of_enemies = 30
#creating empty list
enemies = []

#add enemies to the list
for i in range(number_of_enemies):
    #creating enemy
    enemies.append(turtle.Turtle())

enemy_start_x = -225
enemy_start_y = 250
enemy_number = 0
    
for enemy in enemies:
    enemy.color("red")
    enemy.shape("~/Desktop/space_invaders/invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (50 * enemy_number)
    y = enemy_start_y 
    enemy.setposition(x, y)
    # Update the enemy number
    enemy_number += 1
    if enemy_number == 10:
        enemy_start_y -= 50
        enemy_number = 0


enemyspeed = 0.1

#creating blaster
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletpeed = 5

#define bullet state
#ready = ready to fire
#fire = bullet is firing
bulletstate = "ready"


#Moving function for left arrow key
def move_left():
    player.speed = -3


#Moving function for right arrow key

def move_right():
    player.speed = 3


def move_player():
    x = player.xcor()
    x = x + player.speed
    if x < -280:
        x = -280
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    #Declare bullets as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #move the bullet top the just above the player
        x = player.xcor()
        y = player.ycor() +10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False




#keyboard bindings
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet, "space")



#Main game loop
while True:
    wn.update()
    move_player()

    for enemy in enemies:

        #Moving enemy
        x = enemy.xcor()
        x = x + enemyspeed
        enemy.setx(x)

        #move the enemy back and down
        if enemy.xcor() > 280:
            #Move all enemies down
            for e in enemies:
                y = e.ycor()
                y = y - 40
                e.sety(y)
            #change enemy direction
            enemyspeed *= -1
        
        
        if enemy.xcor() < -280:
            #Move all enemies down
            for e in enemies:
                y = e.ycor()
                y = y - 40
                e.sety(y)
            #change enemy direction
            enemyspeed *= -1

        #check for a collision beyween bullet and enemy
        if isCollision(bullet,enemy):
            
            #reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #Reset the enemy
            enemy.setposition(0, 10000)
            #Update the score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        if isCollision(player, enemy):
            
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletpeed
        bullet.sety(y)

    #check if bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

