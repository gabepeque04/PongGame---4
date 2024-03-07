import pygame  # Import the pygame library
import sys  # Import the sys module

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400  # Set the width and height of the game window
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 60  # Set the dimensions of the paddles
BALL_SIZE = 15  # Set the diameter of the ball
FPS = 60  # Set the frame rate per second
WHITE = (255, 255, 255)  # Define the color white
BLACK = (0, 0, 0)  # Define the color black
TIMER_DURATION = 60  # Set the duration of the timer in seconds
TARGET_SCORE = 10  # Set the target score for winning

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")  # Set the title of the game window

# Create a clock object for controlling the frame rate
clock = pygame.time.Clock()

# Define the initial positions of the paddles
player1_paddle = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2_paddle = pygame.Rect(WIDTH - 30 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Define the initial position and speed of the ball
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed = [5, 5]

# Initialize scores and timer
player1_score = 0
player2_score = 0
timer = TIMER_DURATION * FPS  # Convert seconds to frames

# Initialize a font object for rendering text
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:  # Start the main loop
    for event in pygame.event.get():  # Iterate through each event
        if event.type == pygame.QUIT:  # Check if the user wants to quit
            running = False  # Set running to False to exit the loop

    keys = pygame.key.get_pressed()  # Get the state of all keyboard keys
    # Move player 1 paddle up and down based on keyboard input
    if keys[pygame.K_w] and player1_paddle.top > 0:
        player1_paddle.y -= 5
    if keys[pygame.K_s] and player1_paddle.bottom < HEIGHT:
        player1_paddle.y += 5
    # Move player 2 paddle up and down based on keyboard input
    if keys[pygame.K_UP] and player2_paddle.top > 0:
        player2_paddle.y -= 5
    if keys[pygame.K_DOWN] and player2_paddle.bottom < HEIGHT:
        player2_paddle.y += 5

    # Move the ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Check for collisions with the top and bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]  # Reverse the vertical direction of the ball

    # Check for collisions with the paddles
    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_speed[0] = -ball_speed[0]  # Reverse the horizontal direction of the ball

    # Check if player 1 scores
    if ball.left <= 0:
        player2_score += 1  # Increment player 2 score
        # Check if player 2 wins
        if player2_score >= TARGET_SCORE:
            winner_text = font.render("Player 2 Wins!", True, WHITE)  # Render the winning message
            screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2))
            pygame.display.flip()  # Update the display
            pygame.time.wait(3000)  # Wait 3 seconds before quitting
            running = False  # Exit the loop
        ball.x = WIDTH // 2 - BALL_SIZE // 2  # Reset the ball position
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
    # Check if player 2 scores
    elif ball.right >= WIDTH:
        player1_score += 1  # Increment player 1 score
        # Check if player 1 wins
        if player1_score >= TARGET_SCORE:
            winner_text = font.render("Player 1 Wins!", True, WHITE)  # Render the winning message
            screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2))
            pygame.display.flip()  # Update the display
            pygame.time.wait(3000)  # Wait 3 seconds before quitting
            running = False  # Exit the loop
        ball.x = WIDTH // 2 - BALL_SIZE // 2  # Reset the ball position
        ball.y = HEIGHT // 2 - BALL_SIZE // 2

    screen.fill(BLACK)  # Fill the screen with black color
    pygame.draw.rect(screen, WHITE, player1_paddle)  # Draw player 1 paddle
    pygame.draw.rect(screen, WHITE, player2_paddle)  # Draw player 2 paddle
    pygame.draw.ellipse(screen, WHITE, ball)  # Draw the ball

    # Render scores
    player1_text = font.render(f"Player 1: {player1_score}", True, WHITE)
    player2_text = font.render(f"Player 2: {player2_score}", True, WHITE)
    screen.blit(player1_text, (20, 20))  # Draw player 1 score
    screen.blit(player2_text, (WIDTH - player2_text.get_width() - 20, 20))  # Draw player 2 score

    # Render timer
    timer_text = font.render(f"Timer: {timer // FPS}", True, WHITE)
    screen.blit(timer_text, (WIDTH // 2 - timer_text.get_width() // 2, 20))  # Draw the timer

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

    # Countdown timer
    timer -= 1
    if timer <= 0:
        winner_text = font.render("Time's up!", True, WHITE)  # Render the time's up message
        screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()  # Update the display
        pygame.time.wait(3000)  # Wait 3 seconds before quitting
        running = False  # Exit the loop

pygame.quit()  # Quit Pygame
sys.exit()  # Exit the program
