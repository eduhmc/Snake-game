import pygame
import sys
import random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((500,500))
surface = pygame.Surface(screen.get_size())
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

#Global Variables
velocity = 4
A_height = 10
A_width =10
S_height = 10
S_width = 10
moving = True
counter = True
counter2 = False
x2 = 0
y2 = 0
score = 0
GRIDSIZE=10
GRID_WIDTH = 500 / GRIDSIZE
GRID_HEIGHT = 500 / GRIDSIZE

#GAMECODE
class apple(object):
	def __init__(self):
		self.position = (0,0)
		self.color = (255,0,0)
		self.randomize()

	def randomize(self):
		#Select a random position to the apple
		self.position = (random.randint(0, GRID_WIDTH-1) * GRIDSIZE, random.randint(0, GRID_HEIGHT-1) * GRIDSIZE)

	def draw(self, surf):
		#Draw the apple on a random position on the screen
		r = pygame.Rect((self.position[0], self.position[1]), (GRIDSIZE, GRIDSIZE))
		pygame.draw.rect(surf, self.color, r)

class snake(object):

	def __init__(self, x_value, y_value, direction_value):
		self.body = [[x_value, y_value]]
		self.direction = direction_value
		self.score = 0

	def get_x(self):
		#Gets the x coordinate of the snake's head
		return self.body[0][0]
	
	def get_y(self):
		#Gets the y coordinate of the snake's head
		return self.body[0][1]

	def get_last(self):
		#Gets the x and y coordinates of the snake's last rectangle on the body
		return self.body[-1]


	def location(self):
		self.draw()
	

	def left(self):
	#Changes snake direction to left and doesn't let it move right 
		if self.direction != "RIGHT":
			self.direction = "LEFT"
	def right(self):
	#Changes snake direction to right and doesn't let it move left
		if self.direction != "LEFT":
			self.direction = "RIGHT"
	def up(self):
	#Changes snake direction to up and doesn't let it move to down
		if self.direction != "DOWN":
			self.direction = "UP"
	def down(self):
	#Changes snake direction to down and doesn't let it move up
		if self.direction != "UP":
			self.direction = "DOWN"

	def move(self):
		cur = self.body[0]
		if self.direction == "LEFT":
			x = -1
			y=  0
		if self.direction == "RIGHT":
			x = 1
			y=  0
		if self.direction == "UP":
			x = 0
			y=  -1
		if self.direction == "DOWN":
			x = 0
			y=  1
		self.length = 1
		new = (((cur[0]+(x*10)) % 510), (cur[1]+(y*10)) % 510)
		#Allow the snake to move following the head and not all the body at the same time
		if len(self.body) > 2 and new in self.body[2:]:
			 global crash
			 crash = True
		else:
			self.body.insert(0, new)
			if len(self.body) > self.length:
				 self.body.pop()


	def draw(self):
		#Draws the snake on the screen as a rectangle
		for square in self.body:
			pygame.draw.rect(screen, (0, 128,0,), (square[0], square[1], S_width, S_height))



	def add_body(self):
		if self.direction == "DOWN":
			#Add square up in snake's body
			self.body.append([self.get_last()[0], self.get_last()[1] - S_height])
		if self.direction == "UP":
			#Add square down in snake's body
			self.body.append([self.get_last()[0], self.get_last()[1] + S_height])
		if self.direction == "RIGHT":
			#Add square left in snake's body
			self.body.append([self.get_last()[0] - S_width, self.get_last()[1]])
		if self.direction == "LEFT":
			#Add square right in snake's body
			self.body.append([self.get_last()[0] + S_width, self.get_last()[1]])
	

def collision(snake,apple):
#Check if the position of the head of the snake is on the same position as the apple
	counter = False
	if (snake.get_x()== apple.position[0] and snake.get_y() == apple.position[1]):
		counter = True

	if (counter == True): 
		apple.randomize()
		counter = False
		snake.add_body()
		snake.score += 1
	
	

				
	
#GAME LOOP			
x_value = 50
y_value = 50
crash = False
apple = apple()
#Set the apple class to be called apple
adam = snake(50, 50, "DOWN")
#Set the snake class to be called adam

while not crash:
	pygame.time.delay(10)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crash = True

	#Allows the user to move the snake with the key arrows
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and adam.get_x() > 0:
		adam.left()	
	if keys[pygame.K_RIGHT] and adam.get_x() < 485:
		adam.right()
	if keys[pygame.K_UP] and adam.get_y() > 0:
		adam.up()
	if keys[pygame.K_DOWN] and adam.get_y() < 485:
		adam.down()
	


	
	screen.fill((0,0,0))
	apple.draw(screen)
	adam.move()
	adam.location()
	collision(adam,apple)


	#Verify if the snake goes out of boundries
	if  adam.get_x() < 0 or adam.get_x() > 490 or adam.get_y() < 0 or adam.get_y() > 490:
		crash = True
	#Verify if the head of the snake collides with the rest of the body
	for bodyPart in adam.body[1:]:
		if (bodyPart[0]== adam.get_x() and bodyPart[1] == adam.get_y()):
			crash = True

	pygame.display.set_caption("Snake - Score: " + str(adam.score))
	pygame.display.flip()	
	pygame.display.update()
	clock.tick(60)



pygame.quit()
