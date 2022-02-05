# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#													   		#
#			     Python Raycasting (Unstable)	    		#
#			          Developer: Carbon				        #
#													   		#
#               No longer under development...				#
#														    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Imports: #

from src.window import *
from src.variables import *
from src.frame import *
from src.movement import *
from src.functions import *

# Icon:
setGameIcon('wall/wall.png')

# Game Window: #

display = Window(screenWidth, screenHeight)

# Game Assets: #

# Sky:
sky = loadGameImage('sky/sky.png')
sky = convert3DArray(resizeImage(sky, (360, verticalRes * 2))) / 255

# Floor: 
floor = loadGameImage('floor/floor.png')
floor = convert3DArray(floor) / 255

# Wall:
wall = loadGameImage('wall/wall.png')
wall = convert3DArray(wall) / 255

# Crosshair:
crosshair = loadGameImage('crosshair/crosshair.png')

# Game Loop: #

while(display.gameRunning):
	updateWindowTitle("Raycasting: ", fpsHandler.get_fps())
	toggleMouseCursorOff()

	# Create Frame:
	frame =  updateFrame(positionX, positionY, rotation, frame, sky, floor, wall)

	# Convert & Scale Frames:
	surface = convertToSurface(frame)
	surface = resizeImage(surface, (800, 600))

	# Display Frames: 
	display.draw(surface, (0, 0))
	display.draw(crosshair, (380, 250))
	drawText(display.window, "Health: 100", (255, 0, 0), 20, 580) # Example
	drawText(display.window, "Armour: 100", (0, 0, 255), 180, 580) # Example

	# Update Display:
	display.updateDisplay()

	# Movement: #
	positionX, positionY, rotation = handleMovement(positionX, positionY, rotation, fpsHandler.tick() / 500, wallSet)
	resetMousePosition()

# Quit: #
destroyGame()
