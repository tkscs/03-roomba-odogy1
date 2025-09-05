# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(7)

# Draw the Level 2 version of the room
window = room.draw_room(level = 2)

###
# Start your code here
length = 160 * 3 + 75

for i in range(9):
    forward(length)
    left(90)
    forward(40)
    left(90)
    forward(length)
    right(90)
    forward(40)
    right(90)
forward(length)
left(90)
forward(40)
left(90)
forward(length)
left(90)
forward(40 * 19)
left(90)
 
 
# End your code here
###
 
window.exitonclick()