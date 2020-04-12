##################################################
# Name:
# Collaborators:
# Est Time Spent (hrs):
##################################################

import arcade

class Prob2():
    '''
    Class to display and move a circle about the screen using 
    mouse control.

    All the needed inputs for any method can be found in the documentation:
    https://arcade.academy/arcade.html?highlight=arcade%20window#arcade.Window

    A list of potential mouse presses is:
    arcade.MOUSE_BUTTON_LEFT, arcade.MOUSE_BUTTON_RIGHT, arcade.MOUSE_BUTTON_MIDDLE

    A list of potential key presses can be found here:
    https://arcade.academy/arcade.key.html

    '''

    def __init__():
        '''
        Creates the necessary window into which everything is drawn.

        Inputs:
         - width (int): the width of the window
         - height (int): the height of the window
         - title (str): the name of the window

        Returns:
         - (window obj): a handle for this window object
        '''
        pass


    def on_draw():
        '''
        Function responsible for drawing anything to the screen.
        Should always start the render and then draw any graphical
        primitives.

        Inputs:
         - self (window obj): this window obj
        Returns:
         - none
        '''
        pass

    def on_mouse_motion():
        '''
        Function which is run whenever the mouse is moved in the window.

        Inputs:
         - x (float): x position of the mouse
         - y (float): y position of the mouse
         - dx (float): change in x since last run of method
         - dy (float): change in y since last run of method

        Returns:
         - None
        '''
        pass

    def on_mouse_press():
        '''
        Function which is run whenever a mouse key is pressed.

        Inputs:
            - x (float): x position of the mouse
            - y (float): y position of the mouse
            - button (int): what button was pressed
            - modifiers (int): if shift, ctrl, alt etc were held down

        Returns:
            - None
        '''
        pass

    def on_key_press():
        '''
        Function which is run whenever any key is pressed.

        Inputs:
            - key (int): the key that was hit. See key lookup table linked at top
            - modifiers (int): if shift, ctrl, etc were held down
        Returns:
            - None
        '''
        pass



def main():
    '''
    Simple function to create the necessary window object and keep the window open.
    '''
    window = Prob2(500, 500, 'Problem 2')
    arcade.run()


# And here we will run main
if __name__ == '__main__':
    main()
