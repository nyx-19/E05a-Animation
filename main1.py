#Copy the contents from http://arcade.academy/examples/move_mouse.html#move-mouse and see if you can figure out what is going on. Add comments to any uncommented lines



"""
This simple animation example shows how to move an item with the mouse, and
handle mouse clicks.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_mouse
"""

import arcade     #what tells python that we are wanting to run this on arcade and not in the python terminal

#sets the desired pixel width and heigh for the screen that apprears 
SCREEN_WIDTH = 640         
SCREEN_HEIGHT = 480        
SCREEN_TITLE = "Move Mouse Example"   #titles the arcade window


class Ball:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)  #tells the program exactly what the numbers and values we will enter later will apply to when we create the ball


class MyGame(arcade.Window):

    def __init__(self, width, height, title):  #takes information from above that has been defined and places it together.

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY) #sets the background color given the files that arcade already has to chose from

        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()   #what tells the arcade window to appear when we run it
        self.ball.draw()        #what puts the ball onto the screen when we run the program

    def on_mouse_motion(self, x, y, dx, dy):      #i am confused where the dx and dy velocities are used in the lines below
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball.position_x = x        #tracks the ball's x location and assigns the x position to wherever the x imput from the mouse is
        self.ball.position_y = y        #tracks the ball's y location and assigns the y position to whereever the y imput from the mouse is

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        print(f"You clicked button number: {button}") #communicates to the user when a specific button is pushed and tells which one
        if button == arcade.MOUSE_BUTTON_LEFT:          # defines that if the left mouse button is pushed, the ball will change color to black
            self.ball.color = arcade.color.BLACK        # this line is explained in line above

    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT: #when the button is let go, the left click on mouse, it returns the color back to it's original state
            self.ball.color = arcade.color.AUBURN   #line explained above


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE) #it's allll contected
    arcade.run()     #tells arcade to start up


if __name__ == "__main__":      #i'm guessing this is a nessesarry self-awareness function so that it knows if this program is called main, then it should be running main
    main()