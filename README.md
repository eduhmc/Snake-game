# Snake-game
I am Eduardo Huerta-Mercado, I recreated the Snake Game in Python3 using Sublime Text and importing Pygame
Final Project-Snake

For my final project I made the snake game in Python; using Python3, sublime text and importing Pygame. The game involves a snake and an apple, the snake must eat the apple; however, each time it does, the apple changes location. As the snake eats more apples it becomes larger, making it difficult to control it. If the snake hits itself or goes out of boundaries, the game ends. 

List of features
1.	Determining Futures of snake – Importing Pygame in order to see the game graphically. Constructing an algorithm that increases the length of the snake for every “apple” eaten; using lists.  And if snake touches itself or goes out of the boundaries of the board, the game will be over. The snake will be manipulated with the key arrows.
2.	Random placement of apple - Constructing an algorithm that places an apple randomly but without ever touching the snake. If the snake touches the apple, then the apple should be placed on another location. Each time the snake touches the apple, the score (global variable) will increase.
3.	Board representation – I have drawn a board with the Pygame features and I set it for the color to be black. Our board works as a coordinate system. I have created an algorithm that makes the board have a gridwidth, a gridheight and a gridsize. Thanks to this the snake will hit the apple perfectly, meaning that the snake movements will always fit with the apple random position. 

Description of lists/dictionaries and script/local variables

I have imported the module random. I have also used tuples to create the board and to create the random coordinates of the apple, which change after the snake eats the apple thanks to the random module.  Then I have used lists in order to create our snake, specifically to create the head of the snake which is the first green rectangle that appears on the board when the game starts. Because is a list each time the snake eats the apple the list grows. I made this by using the append function. Then I have used both global and local variables. I created global variables above the game code. One of MY global variables is the score that changes by 1 each time the snake eats an apple. Furthermore, I have find the way to graphically portray the score on the board so the player is aware of his score. Other global variables are the snake width, snake height, apple width, apple height. Throughout the whole game I have designed local variables that help with the direction, the snake color, the apple color, etc. I have set both the global and local variables to different types, for instance integers, strings and Booleans. 

The list can be found within the snake class below the init function. I have equaled the list to the body. Each time the list grow it can be seen under the add_body function. As I said before, all the global variables are placed at the beginning of the game and the local variables can be found within the whole game code. For example, the cur variable that gives us the head of the snake can be found under the move function. 
