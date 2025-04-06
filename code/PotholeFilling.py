"""
File: PotholeFilling.py
Name: Andre
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
from StepUp import *

def go_in():
    """
    pre-condition:Karel is at the upper left of the pothole facing east
    post-condition:Karel is in the pothole facing south
    """
    move()
    turn_right()
    move()

def go_out():
    """
    pre-condition:Karel is in the pothole facing south
    post-condition:Karel is at the upper left of the pothole facing east
    """
    for i in range(2):
        turn_left()
    move()
    turn_right()
    move()

def main():
    """
    TODO:
    """
    pass
    for i in range(3):
        go_in()
        put_99()
        go_out()


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
