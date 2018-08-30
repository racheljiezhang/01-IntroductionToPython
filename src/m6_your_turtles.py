"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Rachel ZHang.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################
import rosegraphics as rg
###############################################################################
# TODO: 2.
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
window = rg.TurtleWindow()

lenin = rg.SimpleTurtle('circle')
stalin = rg.SimpleTurtle('square')
putin = rg.SimpleTurtle('triangle')
mao = rg.SimpleTurtle('circle')

lenin.pen = rg.Pen('white', 1)
stalin.pen = rg.Pen('white', 1)

lenin.backward(300)
lenin.left(90)
lenin.forward(100)
lenin.pen = rg.Pen('red', 3)
lenin.backward(200)
lenin.forward(100)
lenin.right(90)
lenin.forward(100)
lenin.left(90)
lenin.forward(100)
lenin.backward(200)

stalin.backward(150)
stalin.left(90)
stalin.forward(100)
stalin.pen = rg.Pen('blue', 3)
stalin.backward(200)
stalin.forward(200)
stalin.right(90)
stalin.forward(100)
stalin.backward(100)
stalin.right(90)
stalin.forward(100)
stalin.left(90)
stalin.forward(75)
stalin.backward(75)
stalin.right(90)
stalin.forward(100)
stalin.left(90)
stalin.forward(100)

putin.pen = rg.Pen('yellow', 3)
putin.left(90)
putin.forward(100)
putin.backward(200)
putin.right(90)
putin.forward(100)

mao.pen = rg.Pen('white', 0)
mao.forward(150)
mao.right(90)
mao.forward(100)
mao.pen = rg.Pen('green', 3)
mao.backward(200)
mao.left(90)
mao.forward(100)
mao.right(90)
mao.forward(100)
mao.right(90)
mao.forward(100)

window.close_on_mouse_click()
