Final Project Space shooter

my video url: https://www.youtube.com/watch?v=DpiWAiJuK6U

Description:

The game is a retro space shooter!
As a kid i was totally fascinated of this concept, so i rebuilt that kind of game.
The animated space ships (player and enemies) are self drawn with an unfinished look, to make it look more retro. What is there, not to love?

The code overview:

Imports necessary modules: pygame, sys, time, and random.
Initializes Pygame and sets up the window with a caption "Final Project Space Shooter".
Defines various constants and loads images and sounds used in the game.
Defines functions for updating the game elements and displaying them on the screen.

Defines the main game loop in the main() function, where player movement, UFO movement, bullet handling, collision detection, and game state changes are managed.
Checks for events, such as quitting the game or key presses.
Handles player movement based on keyboard input.

Manages UFO movement, creation, and removal.
Handles collisions between the player and UFOs, updating the player's health (COUNTER).
Manages bullets, their movement, and collision with UFOs.
Updates the game screen using the update() function.

Movement:
I set the movement key bindings simple and the possibility to play it with one, or two hands.

W = Up
S = Down
A = Left
D = Right

SPACE = Shoot

Key components:

Main Game Loop: The core of the game resides in the main game loop. This loop regulates the game's flow, managing events, updating entity positions, handling user input, and refreshing the display at a consistent frame rate.

Game Initialization: Pygame is initialized, and essential elements like the window dimensions, background image, and audio files are set up. The window is configured with a captivating space backdrop, creating an immersive visual experience.

Game Entities: The game features several entities, including the player's ship, UFOs, bullets, and accompanying sound effects. The player's ship responds to user input for navigation.

UFOs and Collisions: UFOs of varying designs descend from the top of the screen at random intervals.
The code handles collision detection between the player's ship and UFOs.
Upon collision, the player's hull power (COUNTER) is decremented, providing a feedback mechanism for damage sustained.

Bullet Handling: The player can fire bullets by pressing the spacebar. Bullets are depicted as small, elongated images, and their position is tracked to facilitate collision detection.
Bullet firing is subject to a cooldown period to prevent rapid consecutive shots.

Score Tracking: Points are awarded to the player for successfully hitting UFOs. A scoring system is implemented to keep track of the player's progress, providing a tangible measure of success. The maximum highscore is 2001 (Nostalgic thoughts).

Game Over and Victory: The game incorporates distinct visual cues for game over and victory scenarios. When the player's hull power reaches zero, signifying defeat, a game over screen is displayed along with an accompanying sound effect.
Conversely, upon accumulating a substantial score, a victory screen is presented to celebrate the player's achievement.

In this straightforward yet engaging space shooter game, players must skillfully navigate their ship, employing evasive maneuvers to avoid direct contact with encroaching enemy UFOs.
Alternatively, they can strategically engage and eliminate these adversaries through precise shooting, all in pursuit of achieving the coveted high score. Immerse yourself in this cosmic battle, where every decision counts. Have a blast and relish the exhilarating experience of playing!
