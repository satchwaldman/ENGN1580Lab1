# Game prototype 

# screen
# two teams
# each team has a slider for how much power they allocate towards their signal vs their opponents noise signal 
# each team also has options for the noise profile they can select for their opponent
# (optional) each team can also change their correct signal 1 byte code

# import pygame

# # activate the pygame library .
# # initiate pygame and give permission
# # to use pygame's functionality.
# pygame.init()

# # create the display surface object
# # of specific dimension..e(500, 500).
# win = pygame.display.set_mode((500, 500))

# # set the pygame window name
# pygame.display.set_caption("Moving rectangle")

# # object current co-ordinates
# x = 200
# y = 200

# # dimensions of the object
# width = 20
# height = 20

# # velocity / speed of movement
# vel = 10



# # Indicates pygame is running
# run = True

# # infinite loop
# while run:
# 	# creates time delay of 10ms
# 	pygame.time.delay(1000)
	
# 	# iterate over the list of Event objects
# 	# that was returned by pygame.event.get() method.
# 	for event in pygame.event.get():
		
# 		# if event object type is QUIT
# 		# then quitting the pygame
# 		# and program both.
# 		if event.type == pygame.QUIT:
			
# 			# it will make exit the while loop
# 			run = False
# 	# stores keys pressed
# 	keys = pygame.key.get_pressed()
	
# 	# if left arrow key is pressed
# 	if keys[pygame.K_LEFT] and x>0:
		
# 		# decrement in x co-ordinate
# 		x -= vel
		
# 	# if left arrow key is pressed
# 	if keys[pygame.K_RIGHT] and x<500-width:
		
# 		# increment in x co-ordinate
# 		x += vel
		
# 	# if left arrow key is pressed
# 	if keys[pygame.K_UP] and y>0:
		
# 		# decrement in y co-ordinate
# 		y -= vel
		
# 	# if left arrow key is pressed
# 	if keys[pygame.K_DOWN] and y<500-height:
# 		# increment in y co-ordinate
# 		y += vel
		
			
# 	# completely fill the surface object
# 	# with black colour
# 	win.fill((0, 0, 0))
	
# 	# drawing object on screen which is rectangle here
# 	pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
	
# 	# it refreshes the window
# 	pygame.display.update()

# # closes the pygame window

# pygame.quit()

# ------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button
import time
import sys
import numpy as np



fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

def animate(i):
    pullData1 = open("team1_data.txt","r").read()
    dataArray1 = pullData1.split('\n')
    xar1 = []
    yar1 = []

    pullData2 = open("team2_data.txt","r").read()
    dataArray2 = pullData2.split('\n')
    xar2 = []
    yar2 = []

    for eachLine in dataArray1:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar1.append(int(x))
            yar1.append(int(y))
    
    for eachLine in dataArray2:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar2.append(int(x))
            yar2.append(int(y))
    ax1.clear()
    ax1.plot(xar1,yar1)
    ax2.clear()
    ax2.plot(xar2,yar2)
ani = animation.FuncAnimation(fig, animate, interval=10)
# bnext = Button(axnext, 'Next')
# bnext.on_clicked(callback.next)




# fig, ax = plt.subplots()

# fig.canvas.mpl_connect('key_press_event', on_press)

# # ax.plot(np.random.rand(12), np.random.rand(12), 'go')
# xl = ax.set_xlabel('easy come, easy go')
# ax.set_title('Press a key')
plt.show()