"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Parker Jordan.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # -------------------------------------------------------------------------
    # Done: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # -------------------------------------------------------------------------

    original_x1 = rectangle.corner_1.x
    original_x2 = rectangle.corner_2.x
    original_y1 = rectangle.corner_1.y
    original_y2 = rectangle.corner_2.y

    x1 = original_x1
    x2 = original_x2
    y1 = original_y1
    y2 = original_y2
    a = rectangle.get_width()
    b = rectangle.get_height()

    for k in range(n):
        for i in range(k + 1):
            new_wall = rg.Rectangle(rg.Point(x1, y1), rg.Point(x2, y2))
            new_wall.attach_to(window)
            window.render()
            x1 = x1 + a
            x2 = x2 + a
        x1 = original_x1 - (k + 1) * 0.5 * a
        x2 = original_x2 - (k + 1) * 0.5 * a
        y1 = original_y1 - (k + 1) * b
        y2 = original_y2 - (k + 1) * b

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
