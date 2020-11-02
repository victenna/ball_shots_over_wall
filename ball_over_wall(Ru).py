import turtle,time,math
wn=turtle.Screen()
wn.setup(1200,900)
wn.bgpic('canva.gif')
turtle.tracer(1,0)
t=[]
image=['player.gif','ball.gif','vector.gif']
for i in range(6):
    t.append(turtle.Turtle())
    t[i].up()
    t[i].hideturtle()
    if i<3:
        wn.addshape(image[i])
        t[i].shape(image[i])

t[0].goto(-350,-200)   #player
t[0].showturtle()

t[1].goto(-325,-77)  #ball
ball_position=t[1].position()

t[2].goto(-450,70)  #vector image
t[2].showturtle()

t[3].shape('square')   #  wall
t[3].shapesize(25,0.5)
t[3].color('gainsboro')
t[3].goto(180,-70)
t[3].showturtle()
wall_position=t[3].position()
print('wall',wall_position)

tclone=t[3].clone()  #plate
tclone.goto(500,-310)
tclone.shapesize(1,2)
tclone.color('blue')

t[4].shape('square')   #road
t[4].shapesize(0.6,55)
t[4].goto(0,-318)
t[4].showturtle()
       
pi=math.pi
g=9.81
delta=0.15
t[0].speed(0)
t[1].speed(0)
Y=-500
dY=10
score=0
FONT=('Times New Roman',20,'bold')
Score=turtle.Turtle()  #счет
Score.hideturtle()

for q in range (30):
    t[1].clear()
    t[1].up()
    time.sleep(0.1)
    t[1].showturtle()
    tt=0
    eps=30*(q%10)
    t[0].goto(-350+eps,-200)
    t[1].goto(-325+eps,-77)
    Vo=100
    theta=float(wn.textinput('Броски мячем','Введите угол theta'))
    Vox=Vo*math.cos(pi*theta/180)
    Voy=Vo*math.sin(pi*theta/180)
    t[1].setheading(theta)
    t[1].down()
    t[1].color('blue')
    n=0
    while n==0:
        X=Vox*tt
        Y=Voy*tt-g*tt*tt/2
        Vx=Vox
        Vy=Voy-g*tt
        ball_angle=math.atan(Vy/Vx)*180/math.pi
        wallx=t[1].xcor()
        wally=t[1].ycor()
        if ball_angle<-5 and wallx>160 and wallx<180 and wally<180:
            n=1
            t[1].clear()
            t[1].hideturtle()
            time.sleep(1)
        if theta <48 and t[1].xcor()>170:
            print('ball_position=',ball_position)
            n=1
            t[1].clear()
            t[1].hideturtle()
            time.sleep(1)
        if Y<-218:
            n=1
            t[1].clear()
        deltax=abs(t[1].xcor()-tclone.xcor())
        deltay=abs(t[1].ycor()-tclone.ycor())
        if deltax<40 and deltay<40:
            n=1
            score=score+1
            Score.clear()
        Score.write('Счет='+str(score),font=FONT)
        time.sleep(0.01)
        tt=tt+delta
        t[1].setposition(X-325+eps,Y-77)
        ball_position=t[1].position()
        
        
        
