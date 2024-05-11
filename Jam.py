import turtle
import random
import time

# set up screen/background

global window1
window1 = turtle.Screen()
window1.title('Target Space Jam')
window1.setup(951, 800)
window1.bgpic('bg1.gif')
time.sleep(2)

turtle.hideturtle
global hoop
hoop = turtle.Turtle()
hoop.penup()
turtle.register_shape('hoop2.gif')
hoop.shape('hoop2.gif')
hoop.goto(0, 180)
hoop.shapesize(stretch_len=10, stretch_wid=5)

global score
global score1
score1 = 0
score = turtle.Turtle()
score.penup()
score.hideturtle()
score.goto(-385, -335)
score.write("Score: ", font=("Verdana", 30, "bold"))

global basketball
# screen updaion
window1.tracer(0)
# create a turtle object object
basketball = turtle.Turtle()

# set turtle object speed
basketball.speed(0)

# turtle object in air
basketball.penup()

# set initial position
basketball.goto(0, -180)

# move turtle object to surface
basketball.pendown()


def stop():
    exit()


# infinite loop
def launch():
    for i in range(30):
        # clear turtle work
        basketball.clear()

        # call function to draw ball
        turtle.register_shape('giphybball.gif')
        basketball.shape('giphybball.gif')

        # update screen
        window1.update()

        # forward motion by turtle object
        basketball.seth(90)
        basketball.forward(15)

        print("Ball Y-coordinate: " + str(basketball.ycor()) + " Ball X-coordinate: " + str(
            basketball.xcor()) + " Hoop Y-coordinate: " + str(hoop.ycor()) + " Hoop X-coordinate: " +
              str(hoop.xcor()))

        if (basketball.xcor() > hoop.xcor() - 50) and (basketball.xcor() < hoop.xcor() + 50) and (
                basketball.ycor() == hoop.ycor()):
            global score1
            score1 += 1
            basketball.penup()
            time.sleep(.1)
            basketball.sety(-180)
            window1.update()
            time.sleep(0.02)
            window1.update()
            score.clear()
            score.write("Score: {}".format(score1), font=("Verdana", 30, "bold"))
            break
        elif (basketball.ycor() == 210) and (basketball.xcor() != hoop.xcor()):
            basketball.penup()
            time.sleep(.1)
            basketball.sety(-180)
            window1.update
            time.sleep(0.02)
            window1.update
            break


turtle.onkey(launch, 'space')
turtle.onkey(stop, 'Escape')
turtle.listen()

# main
while True:
    window1.update()

    # hoop movement
    x = random.randint(1, 360)
    hoop.setx(hoop.xcor() + x)
    time.sleep(0.1)
    x = random.randint(1, 360)
    time.sleep(0.1)
    hoop.setx(hoop.xcor() - x)

    # border checking
    if hoop.xcor() > 150:
        hoop.setx(150)

    if hoop.xcor() < -150:
        hoop.setx(-150)

turtle.done()

