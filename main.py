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

import math # added math
import matplotlib

#########################################################
#                   Your Code Goes Below                #
#########################################################

def movePen(t=None, x=0, y=0):
  '''
	move the turtle position and ensure the pen dosen't drag
  args: t: (Turtle) turtle object
        x: (int) x coordinate to move to
        y: (int) y coordinate to move to
	return: None
	'''
  t.up()
  t.goto(x, y)
  t.down()

def drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0):
  '''
	draws a square centered in top left (top_left_x, top_left_y) of width (width)
	args: myturtle: (Turtle) turtle object
        width: (int) width of square
        top_left_x: (int) top left x cordinate of square
        top_left_y: (int) top left y cordinate of square
	return: None
	'''
  movePen(myturtle, top_left_x, top_left_y)
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
  movePen(myturtle, x_start, y_start)
  myturtle.goto((x_end, y_end))
  
# Added center argument
def drawCircle(myturtle=None, radius=0, center_x=0):
  '''Draws the square 
  args: myturtle: (Turtle) turtle object
  radius: (int) radius of circle
  return: none
  '''
  movePen(myturtle, center_x, -radius)
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

class Board:
  
  def __init__(self, myturtle, scale):
    self.t = myturtle
    self.scale = scale

  def setUpDartboard(self):
    ''' shows the dartboard 
    args: myscreen: (Screen) screen object
    myturtle: (Turtle) turtle object
    return: None
    '''
    scale = self.scale
    drawSquare(self.t, width=(scale*2), top_left_x=-scale, top_left_y=scale)
    drawLine(self.t, -scale, 0, scale, 0)
    drawLine(self.t, 0, -scale, 0, scale)
    movePen(self.t, -5,0)
    drawCircle(self.t, scale, 0)

  def resetPos(self):
    movePen(self.t, -self.scale, self.scale)
  
  def playGame(self, players, rounds=1, gameType="DISTANCE"):
    self.t.clear()
    self.setUpDartboard()
    
    scores = {}  # initialize scores
    for player in players:
      scores[player] = 0
    
    for round in range(rounds):

      # Pick a random target on the grid
      (target_x,target_y) = (0,0)
      
      for player in players:
        player.throwDart(self.t, target_x, target_y, self.scale)

        if gameType == "DISTANCE":
          d = self.t.distance(target_x,target_y)
          scores[player] += self.scale-d
          print("{}'s landed {} from the center!".format(player.getName(), d))
        elif gameType == "STANDARD":
          if isInCircle(self.t, 0, 0, self.scale):
            print("{} hit the board!".format(player.getName()))
            scores[player] += 1

    winner = max(scores, key=scores.get)
    print()
    print("********* {} Match Results *********".format(gameType))
    print("Winner: {}".format(winner.getName()))
    for player,score in scores.items():
      print("{}: {} (average score per round: {})".format(player.getName(), score, score/rounds))
    print("***********************************".format(gameType))
    print()
    
class Player:

  def __init__(self, name, color, skill):
    if skill < 1 or skill > 10: raise Exception('Invalid skill level, must be 1-10')
    self.name = name
    self.skill = skill  # 1-10
    self.color = color

  def throwDart(self, myturtle, target_x, target_y, scale=1):
    ''' marks where a dart lands on the graph
    args: myturtle: (Turtle) turtle object
    return: None
    '''
    skill = 10 - self.skill
    x = random.uniform(-skill, skill)
    y = random.uniform(-skill, skill)

    shot_x = target_x + x/scale
    shot_y = target_y + y/scale
    movePen(myturtle, shot_x, shot_y)
    myturtle.dot(5, self.color)

  def getName(self):
    return self.name
    

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
    window.setworldcoordinates(-5,-5, 5,5)
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!

    player1 = Player("Maya", "red", 2)
    player2 = Player("Leah", "blue", 5)
    player3 = Player("Rocky", "green", 6)
    player4 = Player("Oliver", "purple", 8)
    players = [player1,player2,player3,player4]
  
    b = Board(darty, scale=3)
    b.playGame(players, 10, "STANDARD")
    b.playGame(players, 10, "DISTANCE")
  
    
    
    b1 = Board(darty, scale=2)
    # Loop for 10 darts to test your code
    b1.playGame([player1, player2], 10, "STANDARD")
    print("\tPart A Complete...")
    
    window.exitonclick()
  

main()