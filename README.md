## Pinball Simulation in Python

To run the Pinball program

@Programming language : python 2.4.4
@myro graphics

Website for downloading the free software :  http://wiki.roboteducation.org/Myro_Installation_Manual

2 libraries - myro and math have to be imported.

@ Everything required to run the Pinball code will get downloaded and installed once you run the .exe file.
@ right click on the Pinball.py file and "edit with IDLE"
@ press F5 on the window with the source code and then follow the prompts.


ALGORITHM DESCRIPTION - 


2 libraries have to be imported - the myro library and the math library.

The code initializes an array of frequencies of size 1000 and puts all its elements as 0.
The while loop runs as long as the user inputs 'y' as his choice to play or not and 
the rest of the code is inside the while loop.

In the while loop, first, the various function that will be used have been defined.

Then, it initializes the initial position, velocity, side of the triangle and radii of the circles.

Then there is a block of code that deals with graphics.
A window is created and the certain color variables have been defined using the variable name's rgb values.
Circles are defined using their centers and radii.
Colors are filled into the background and into the circles.
The ball is defined in the same way as the circles and color is filled in it too.

the wait(n) method makes the program wait for n seconds before executing the next line of code.
It is a method, pre defined in the myro library.



ACTION METHOD -

It makes all variables global.
sets variable condition to all three conditions joined by an or.
Then, using if, elif and else statements, it checks for either conditions indicating which circle the ball 
collides with and then the block of code in the conditional is executed.
Then it calls the method moveOut() .



After the action method,

the moveball method defines the ball's movement in the window, the start method prompts the user for
angle input and calls the action method. When the ball escapes, it calls the ball.undraw() method to 
undraw the ball.



SAMPLE OUTPUT:

Enter the angle :
300

Total number of hits : 
1

Want to play again (y/n) :
y

Enter the angle :
324

Total number of hits : 
2

Want to play again (y/n) :
n

Thank you for playing with us today! Hope to see you back soon!
