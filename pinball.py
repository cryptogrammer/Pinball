from math import *
from myro import *

# Utkarsh Garg
# GT ID 902904045
# Math 2605 Project 1: Pinball Project
# The program simulates a pinball game with a ball released from the center of a
# triangle, with three circles of equal radii at its vertices.
# The ball is launhed with unit velocity and speed remains constant.
# Collisions are considemaroon elastic, hence no loss of energy is accounted for.

choice = "y"
i = 0
frequency = []
for i in range(1000):
    frequency = frequency + [0]
while choice == "y":
    def vector_sum(vector1,vector2):
        length = len(vector1)								# Calculates the lenght of vector1
        answer = []									# Initializes an empty list
        for i in range(0,length):
            answer = answer + [vector1[i] + vector2[i]]	                        	# Loops through and adds element-wise the vectors.
        return answer

    def vector_difference (vector1,vector2):
        length = len (vector1)								# Calculates the lenght of vector1
        answer = []									# Initializes an empty list
        for i in range(0,length):
            answer = answer + [vector1[i] - vector2[i]]		                        # Loops through and subtracts the vectors element-wise.
        return answer

    def dot_product (vector1,vector2):						        # Defines a function to calculate dot product of two vectors.
        return_value = 0
        for i in range (0,len(vector1)):					
            return_value = return_value + vector1[i]*vector2[i]                 	# Caluclates the dot product as x1*x2 + y1*y2
        return return_value

    def scalar_and_vector (k, v):							# Defines multiplication of a vector by a scalar
        answer = []
        for i in range(0,len (v)):
            answer = answer + [k*v[i]]
        return answer

    def intersect (c,r,x,v):								# Defines the intersect method which checks if time > 0	
        c_minus_x = vector_difference(c,x)					        # or not. If both time and the Discriminant satisfy the 
        v_dot_c_minus_x = dot_product (v,c_minus_x)			                # requimaroon conditions, the function returns the time and 
        if v_dot_c_minus_x <= 0:							# it returns True. Else, it returns False.
            return [False,"no solution, case 1"]
        else:
            D = v_dot_c_minus_x**2 - dot_product(c_minus_x,c_minus_x) + r**2
            if D <= 0:
                return [False,"no solution, case 2"]
            elif D > 0:
                time = v_dot_c_minus_x - D**0.5
                return [True,time]

    def reflect(c,x,v):									# Defines the reflect function which calculates the
        c_minus_x = vector_difference(c,x)					        # velocity after reflection from any one of the circles.
        k = (2.0)*(dot_product(v,c_minus_x))/(dot_product(c_minus_x,c_minus_x))
        change = scalar_and_vector (k, c_minus_x)
        reflectedVelocity = vector_difference (v,change)		
        return reflectedVelocity							# returns velocity of the ball as a vector after reflection.

    v = [0,0]									        # Velocity at origin.
    x = [0,0]									        # Initial position of the ball.
    hits = 0									        # Initializing hits.
    lastHit = 0										# Initializing lastHit
    s = 60									        # Side of the equilateral triangle.
    r = 20									        # Radius of the circles the ball bouncess off of.
    c2 = [s/2, (-1)*s*(3**0.5)/6]							# Defining the coordinates of the centres of the circles
    c1 = [(-1)*s/2, (-1)*s*(3**0.5)/6]			        			# in terms of the side length of the triangle.
    c0 = [0,s/(3**0.5)]
    window = GraphWin("Pinball graphics!", 300,300)                      		# Constructing a windowdow for the pinball game
    window.setCoords (-149,-149,150,150)					        # Defines coordinates of the upper and lower corners of the windowdow.
    purple = color_rgb (160,32,240)							# Defining various colors by their rgb values.
    maroon = color_rgb (176,48,96)
    gold = color_rgb(255,215,0)
    white = color_rgb(255,255,255)
    black = color_rgb (20,20,20)
    window.setBackground(purple)						        # Sets the color of the background to purple
    circle0 = Circle(Point (c0[0],c0[1]), r)		                		# Defines the first Circle by its coordinates and radius.
    circle1 = Circle(Point (c1[0],c1[1]), r)				                # Defines the second Circle by its coordinates and radius.	
    circle2 = Circle(Point (c2[0],c2[1]), r)				                # Defines the third Circle by its coordinates and radius.
    circle0.setFill(maroon)								# Fills the circles with a pre-defined color
    circle1.setFill(gold)								# Fills the circles with a pre-defined color
    circle2.setFill(black)							        # Fills the circles with a pre-defined color
    circle0.draw(window)								# Draws the fist circle in the window
    circle1.draw(window)								# Draws the second circle in the window
    circle2.draw(window)								# Draws the third circle in the window	
    ball = Circle(Point(0,0), 3)							# Defines the ball object
    ball.setFill(white)									# Colors theball object	
    ball.draw(window)									# Draws the ball object	
    wait(1.5)										# Adds a delay of 1.5 seconds before the next line of  
											# code is executed.
    def action():									# Defines the main function that will move the ball
        global x, v,s,r,hits,lastHit,c2,c1,c0,ball					# All variables have been made global so that they can 	
                									# interchangably be accessed from inside and outside the function.
                    									# These are all variables that have been used in the 
                                                                                        # function definitions above.
                                                                                        
        condition = intersect(c0,r,x,v)[0] or intersect(c1,r,x,v)[0] or intersect(c2,r,x,v)[0]
        while (condition):			        				# While any one of the intersect functions for the circles 
            if intersect(c0,r,x,v)[0]:  						# returns True, continue.
                time = intersect(c0,r,x,v)[1]
                deltac_minus_x = scalar_and_vector(time,v)
                x = vector_sum(x,deltac_minus_x)                                        # Updates x as x = x + v*t
                moveBall(ball, deltac_minus_x)                                          # Moves the ball as per the updated x
                hits = hits + 1                                                         # Updates the number of hits
                lastHit = 0                                                             # Sets lastHit to 0
                v = reflect(c0,x,v)                                                     # Sets v equal to the new reflected velocity
                condition = intersect(c1,r,x,v)[0] or intersect(c2,r,x,v)[0]            # Updates the condition for th while loop
            elif intersect(c1,r,x,v)[0]:
                time = intersect(c1,r,x,v)[1]                                           # Does all the same things based on different conditions
                deltac_minus_x = scalar_and_vector(time,v)
                x = vector_sum(x,deltac_minus_x)
                moveBall(ball, deltac_minus_x)
                hits += 1
                lastHit = 1
                v = reflect(c1,x,v)
                condition = intersect(c0,r,x,v)[0] or intersect(c2,r,x,v)[0]
            elif intersect(c2,r,x,v)[0]:                                                # Does all the same things based on different conditions
                time = intersect(c2,r,x,v)[1]
                deltac_minus_x = scalar_and_vector(time,v)
                x = vector_sum(x,deltac_minus_x)
                moveBall(ball, deltac_minus_x)
                hits += 1
                lastHit = 2
                v = reflect(c2,x,v)
                condition = intersect(c0,r,x,v)[0] or intersect(c1,r,x,v)[0]
        moveOut()

    def moveBall (object,deltac_minus_x):
        for i in range (0,99):
            object.move(deltac_minus_x[0]/100,deltac_minus_x[1]/100)
            wait (0.02)

    def start():                                                                        # Defines the method that prompts the user for the angle they want to
        global v                                                                        # play the game with.
        angle = input("Enter the angle:\n")
        v = [cos(float(angle)*pi/180),sin(float(angle)*pi/180)]
        action()
        ball.undraw()                                                                   # Erases the ball after it escapes.
            
    def moveOut():
        global v
        global x
        global ball
        deltac_minus_x = scalar_and_vector(170,v)
        moveBall(ball, deltac_minus_x)

    start()										# Calls the function start()
    print "Total number of hits: ",									
    print hits										# Prints the number of total hits
    frequency[hits] = frequency[hits]  + 1
    wait(1)										# Waits 1 second before closing the window and prompting the 
    window.close()									# user if he wants to play again or not.
    print frequency[hits]
    choice = raw_input( "Want to play again? (y/n)\n")	        			# Prompts the user.	
print "Thank you for playing with us today! Hope to see you back soon!"			# If choice is no, the while loop is exited and this print 
											# statement is executed.
