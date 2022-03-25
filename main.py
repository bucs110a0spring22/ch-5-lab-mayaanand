'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0) - to outline dartboard
  drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0) - to draw axes
  drawCircle(myturtle=None, radius=0) - to draw the circle
  setUpDartboard(myscreen=None, myturtle=None) - to set up the board using the above functions
  isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0) - determine if dot is in circle
  throwDart(myturtle=None)
  playDarts(myturtle=None) - a simulated game of darts between two players
  montePi(myturtle=None, num_darts=0) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time

#########################################################
#                   Your Code Goes Below                #
#########################################################
def drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0):
  '''
	draws a square centered in top left (top_left_x, top_left_y) of width (width)
	args: myturtle: (Turtle) turtle object
        width: (int) width of square
        top_left_x: (int) top left x cordinate of square
        top_left_y: (int) top left y cordinate of square
	return: None
	'''
  myturtle.up()
  myturtle.goto((top_left_x, top_left_y)) # go to top left
  myturtle.down()
  myturtle.goto((top_left_x, top_left_y-width))  # go to bottom left
  myturtle.goto((top_left_x+width, top_left_y-width)) # go to bottom right
  myturtle.goto((top_left_x+width, top_left_y))  # go to top right
  myturtle.goto((top_left_x, top_left_y))  # go to top left


def drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0):
  '''
  Draws the square 
  args: myturtle: (Turtle) turtle object
  x_start: (int) starting x coordinate
  y_start: (int) starting y coordinate
  x_end: (int) ending x coordinate
  y_end: (int) ending y coordinate
  return: none
  '''
  myturtle.up()
  myturtle.goto((x_start, y_start))
  myturtle.down()
  myturtle.goto((x_end, y_end))

def drawCircle(myturtle=None, radius=0):
  ''''''Draws the square 
  args: myturtle: (Turtle) turtle object
  radius: (int) radius of circle
  return: none
  '''
  myturtle.up()
  myturtle.goto((0, -1))
  myturtle.down()
  myturtle.circle(radius)

def isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0):
  '''Defines whether the dart lands in the circle
  args: myturtle: (Turtle) turtle object
  circle_center_x: (int) x coordinate of center of circle
  circle_center_y: (int) y coordinate of center of circle
  radius: (int) radius of circle
  return: none
  '''
  return myturtle.distance((circle_center_x,circle_center_y)) < radius
  
def setUpDartboard(myscreen, myturtle):
  ''' shows the dartboard 
  args: myscreen: (Screen) screen object
  myturtle: (Turtle) turtle object
  return: None
  '''
  drawSquare(myturtle, width=2, top_left_x=-1, top_left_y=1)
  drawLine(myturtle, -1, 0, 1, 0)
  drawLine(myturtle, 0, -1, 0, 1)
  drawCircle(myturtle, 1)

def throwDart(myturtle=None):
  ''' marks where a dart lands on the graph
  args: myturtle: (Turtle) turtle object
  return: None
  '''
  x = random.uniform(-1, 1)
  y = random.uniform(-1, 1)
  myturtle.up()
  myturtle.goto((x,y))
  myturtle.down()
  if isInCircle(myturtle, 0, 0, 1):  # Green if inside circle
    myturtle.dot(5, "green")
  else:
    myturtle.dot(5, "red")  # Red if outside circle

def playDarts(myturtle=None):
  ''' Simulates two players throwing darts in a game
  args: myturtle: (Turtle) turtle object
  return: None
  '''
  print("**** Starting Dart Game ****")
  # player 1's simulation
  print("--- Player 1 Turn ---")
  player1 = 0
  for i in range(10):
    throwDart(myturtle)
    if isInCircle(myturtle, radius=1):
      player1 += 1  # increment score
      print("Player 1 hits the dartboard!")
    else:
      print("Player 1 missed the dartboard!")
  print("--- Player 2 Turn ---")
  # player 2's simulation
  player2 = 0
  for i in range(10):
    throwDart(myturtle)
    if isInCircle(myturtle, radius=1):
      player2 += 1  # increment score
      print("Player 2 hits the dartboard!")
    else:
      print("Player 2 missed the dartboard!")

  if player1 > player2:
    print("Player 1 wins with {} darts. Player 2 had {} darts".format(player1, player2))
  elif player1 < player2:
    print("Player 2 wins with {} darts. Player 1 had {} darts".format(player2, player1))
  else:
    print("There is a tie! Both players have a score of {}".format(player1))
  print("**** End of Dart Game ****")

def montePi(myturtle=None, num_darts=0):

  incircle = 0
  for i in range(num_darts):
    throwDart(myturtle)
    if isInCircle(myturtle, radius=1):
      incircle += 1  # increment score

  return (incircle/num_darts)*4
    

#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    window.setworldcoordinates(-2,-2, 2,2)
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(myscreen=window, myturtle=darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)
        if isInCircle(myturtle=darty, radius=1):
          print("You hit the dartboard!")
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(myscreen=window, myturtle=darty)
    playDarts(myturtle=darty)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(myscreen=window, myturtle=darty)
    
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(myturtle=darty, num_darts=number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()
  

main()
