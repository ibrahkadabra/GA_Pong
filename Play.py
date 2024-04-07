import pygame
from Pong import Game

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
FPS  = 60

game = Game(WIN, WIDTH, HEIGHT)
run = True
clock = pygame.time.Clock()

while run:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        game.move_paddle(left=True, up=True)
    if keys[pygame.K_s]:
        game.move_paddle(left=True, up=False)
    if keys[pygame.K_UP]:
        game.move_paddle(left=False, up=True)
    if keys[pygame.K_DOWN]:
        game.move_paddle(left=False, up=False)
        
    game.draw()
    game.loop()
    if game.left_score == game.WINING_SCORE or game.right_score == game.WINING_SCORE:

        if game.left_score == game.WINING_SCORE:
            win_text = "Left Player Wins"
        else:
            win_text = "Right Player Wins"
        text = game.SCORE_FONT.render(win_text, 1, game.WHITE)
        WIN.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
        pygame.display.update()
        pygame.time.delay(2000)

        game.reset()
        
pygame.quit()