#Copy the contents from http://arcade.academy/examples/move_keyboard.html#move-keyboard and see if you can figure out what is going on. Add comments to any uncommented lines



"""
This simple animation example shows how to move an item with the keyboard.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_keyboard
"""

import arcade           #what makes python know we want to be running this on arcade

#sets the desired pixel height and width of the arcade screen that is desplayed
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Move Keyboard Example"  #titles the window
MOVEMENT_SPEED = 3                      # sets the desired speed of the ball


class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)  #explains to the program what the values of the numbers and text we enter later for the ball in their place that it will apply to these functions

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            #these are all explained by the comment left by the creator

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)     #applies a color to the screen with the pre-existing color options in arcade

        # Create our ball
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN)  #sets all the desired values into the funtion slots we talk about earlier on line 34

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()   #what tells the arcade window to appear when we run it
        self.ball.draw()        #what puts the ball onto the screen when we run the program

    def update(self, delta_time):
        self.ball.update()      #gives imput updates to the program as we move this about the screen at what ever delta_time is

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED      #defines that when the left key is pushed, it will make the ball move negatively along the x axis
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED       #defines that when the right key is pushed, it will make the ball move positively along the x axis
        elif key == arcade.key.UP:    
            self.ball.change_y = MOVEMENT_SPEED       #defines that when the up key is pushed, it will make the ball move positively along the y axis
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED      #defines that when the down key is pushed, it will make the ball move negatively along the y axis

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:     
            self.ball.change_x = 0                              #this defines that if the ball moves at all along the x axis, the x value will change accordingly
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0                              #this defines that if the ball moves at all along the y axis, the y value will chnage accordingly


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)   #what creates the window given the values we defined for it earlier
    arcade.run()                             #what makes the whole program start up


if __name__ == "__main__":  #this is also probably a needed self aware funtion that tells the program if this is called main, then it should be running main
    main()