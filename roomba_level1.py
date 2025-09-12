# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import left, forward, backward
import room

# Draw the Level 1 version of the room
window = room.draw_room(level = 1)

###
# Start your code here
 
for i in range(2):
    forward(160)
    left(90)
    forward(42)
    left(90)
    forward(160)
    left(270)
    forward(42)
    left(270)
forward(160)
left(270)
for i in range(4):
    forward(42)
left(270)
forward(160)
left(180)
 
# End your code here
###
 
window.exitonclick()