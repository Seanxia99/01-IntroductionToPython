"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Shuang Xia.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

yellow_turtle = rg.SimpleTurtle('turtle')
yellow_turtle.pen = rg.Pen ('yellow', 5)
yellow_turtle.speed = 20
size = 20
for k in range (30):
    yellow_turtle.draw_square(size)
    yellow_turtle.pen_up()
    yellow_turtle.forward(20)
    yellow_turtle.left(60)
    yellow_turtle.pen_down()
    size=size+10

brown_turtle = rg.SimpleTurtle()
brown_turtle.pen = rg.Pen ('brown', 5)
brown_turtle.speed = 30
radius = 20
for k in range (20):
    brown_turtle.draw_circle(radius)
    brown_turtle.pen_up()
    brown_turtle.left(180)
    brown_turtle.pen_down()
    radius=radius+20