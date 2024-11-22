import turtle
#setup
screen = turtle.Screen()
screen.bgcolor("light pink")
screen.title("Thirsty Turtle Maze")
#player's control
player = turtle.Turtle()
player.shape("turtle")
player.shapesize(2)
player.color("green")
player.penup()
player.speed(0)
player.setposition(0,-280)
player.setheading(90)

walls = []
def water():
    pond = turtle.Turtle()
    pond.speed(0)
    pond.penup()
    pond.goto(300, 290)
    pond.pendown()
    pond.setheading(90)
    pond.fillcolor("blue")
    pond.begin_fill()
    pond.circle(60, 180)
    pond.end_fill()
    pond.hideturtle()
    
    
def wall_draw(x,y,width,height):
    wall = turtle.Turtle()
    wall.speed(0)
    wall.shape("square")
    wall.color("brown")
    wall.penup()
    wall.goto(x,y)
    wall.shapesize(height,width)
    walls.append(wall)

def maze():
    water()
    #bounds
    wall_draw(-60,300,25,1)
    wall_draw(-300,0,1,30)
    wall_draw(300,0,1,30)
    wall_draw(-170,-290,12,1)
    wall_draw(170,-290,12,1)

    #struggles 
    wall_draw(-170, -10, 1, 10)
    wall_draw(25, -190, 20, 1)
    wall_draw(0,-100,10,1)
    wall_draw(50,50,1,10)
    wall_draw(140,160,10,1)
    wall_draw(-170,140,1,5)
    wall_draw(-50,200, 1,8)
    wall_draw(200,20,8,5)
    wall_draw(-200,30,10,1)
    wall_draw(100,270,5,4)
    wall_draw(0,-310,10,1)
   # wall_draw(-50, -100, 10, 5)
    #wall_draw(100, -150, 10, 5)
    #wall_draw(200, 100, 10, 5)
def collision(player,walls):
    playerx = player.xcor()
    playery = player.ycor()
    player_w = 20 * 2 
    player_h = 20 * 2 
    for wall in walls:
        wall_x = wall.xcor()
        wall_y = wall.ycor()
        wall_width = wall.shapesize()[1]*20
        wall_height = wall.shapesize()[0]*20
        wall_left = wall_x - wall_width/2
        wall_right = wall_x + wall_width/2
        wall_top = wall_y + wall_height/2
        wall_bottom = wall_y - wall_height/2
        player_left = playerx - player_w/2
        player_right = playerx + player_w/2
        player_top = playery + player_h/2
        player_bottom = playery - player_h/2

        if (player_right> wall_left and player_left<wall_right and
            player_top>wall_bottom and player_bottom<wall_top):
            return True
    return False

def reachwater():
    playx = player.xcor()
    playy = player.ycor()
    pondx = 300
    pondy = 290
    pondradius = 60
    if pondx - pondradius <= playx <= pondx + pondradius:
        if (playx - pondx)**2 + (playy - pondy)**2 <= pondradius**2 and playy >= pondy:
            return True
    return False
def reset():
    player.setheading(90)
    player.goto(0,-280)

#moving wasd controls
def up():
    player.setheading(90)
    player.forward(10)
    if collision(player,walls):
        reset()
    elif reachwater():
        print("Quenched the turtle's thirst!")
        player.color("blue")
        screen.bgcolor("white")
        reset()
def down():
    player.setheading(270)
    player.forward(10)
    if collision(player,walls):
        reset()
    elif reachwater():
        print("Quenched the turtle's thirst!")
        player.color("blue")
        screen.bgcolor("white")
        reset()
def right():
    player.setheading(0)
    player.forward(10)
    if collision(player,walls):
        reset()
    elif reachwater():
        print("Quenched the turtle's thirst!")
        player.color("blue")
        screen.bgcolor("white")
        reset()
def left():
    player.setheading(180)
    player.forward(10)
    if collision(player,walls):
        reset()
    elif reachwater():
        print("Quenched the turtle's thirst!")
        player.color("blue")
        screen.bgcolor("white")
        reset()
screen.listen()
screen.onkey(up, "w")
screen.onkey(down,"s")
screen.onkey(right,"d")
screen.onkey(left,"a")
maze()
screen.tracer(0)
while True:
    screen.update()
screen.mainloop()
