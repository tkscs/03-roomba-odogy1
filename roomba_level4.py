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

# Draw the Level 4 version of the room
window = room.draw_room(level = 4, n_alcoves = 1, radius = 5)

###
# Start your code here
 
a1 = 40 * 1
a2 = 40 * 2
a3 = 40 * 3
a4 = 40 * 4
a5 = 40 * 5
a6 = 40 * 6
a7 = 40 * 7
a8 = 40 * 8
a9 = 40 * 9
b1 = 90
b2 = 180
def why():
    left(b2)
    forward(a9)
    forward(a1)
    left(b2)

forward(a1)
right(b1)
forward(a3)

for i in range(4):
    left(b1)
    forward(a1)
    right(b1)
    forward(a1)
    left(b1)
    forward(a6)
left(b1)
forward(a7)
for a in range(2):
    left(b1)
    forward(a6)
left(b1)
forward(a5)
for a in range(3):
    left(b1)
    forward(a5)
left(b1)
forward(a4)
for a in range(3):
    left(b1)
    forward(a4)
left(b1)
forward(a3)
for a in range(3):
    left(b1)
    forward(a3)
left(b1)
forward(a2)
for a in range(3):
    left(b1)
    forward(a2)
left(b1)
forward(a1)
for a in range(2):
    left(b1)
    forward(a1)
right(b1)
forward(a2)
left(b1)
forward(a6)
left(b2)
forward(a1)
left(b1)
forward(a1)
right(b1)
forward(a1)
left(b1)
forward(a1)
left(b2)
forward(a1)
left(b1)
forward(a1)
right(b1)
forward(a2)
right(b1)
forward(a2)
left(b2)
forward(a1)
right(b1)
forward(a1)
right(b2)
forward(a2)
right(b1)
forward(a2)
right(b2)

why()
forward(a5)
right(b1)
forward(a5)
why()
 
# End your code here
###
 
window.exitonclick()