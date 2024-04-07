import pygame
from .paddle import Paddle
from .ball import Ball
from random import uniform

pygame.init()

class GameInformation:
    def __init__(self, left_hits, right_hits, left_score, right_score):
        self.left_hits = left_hits
        self.right_hits = right_hits
        self.left_score = left_score
        self.right_score = right_score

class Game:    

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    PADDLE_WIDTH, PADDLE_HEIGHT  = 20, 100
    BALL_RADIUS = 10

    SCORE_FONT = pygame.font.SysFont("comicsans", 50)
    WINING_SCORE = 10

    speed = 1

    def __init__(self, window, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        self.left_paddle = Paddle(10, self.HEIGHT//2 - self.PADDLE_HEIGHT//2, self.PADDLE_WIDTH, self.PADDLE_HEIGHT)
        self.right_paddle = Paddle(self.WIDTH - self.PADDLE_WIDTH - 10, self.HEIGHT//2 - self.PADDLE_HEIGHT//2, self.PADDLE_WIDTH, self.PADDLE_HEIGHT)
        self.Paddles = [self.left_paddle, self.right_paddle]
        self.ball = Ball(self.WIDTH//2, self.HEIGHT//2, self.BALL_RADIUS)

        self.left_score = 0
        self.right_score = 0
        self.left_hits = 0
        self.right_hits = 0
        self.window = window

    def draw(self): 
        self.window.fill(self.BLACK)

        left_score_text = self.SCORE_FONT.render(f"{self.left_score}", 1, self.WHITE)
        right_score_text = self.SCORE_FONT.render(f"{self.right_score}", 1, self.WHITE)
        self.window.blit(left_score_text, (self.WIDTH//4, left_score_text.get_width()//2))
        self.window.blit(right_score_text, (self.WIDTH//4 * 3, right_score_text.get_width()//2))

        for paddle in self.Paddles:
            paddle.draw(self.window)
        for i in range(0, self.HEIGHT, self.HEIGHT//20):
            if i % 2 == 1:
                continue
            pygame.draw.rect(self.window, self.WHITE, (self.WIDTH//2 - 2, i, 4, self.HEIGHT//30))
            
        self.ball.draw(self.window)                     
        pygame.display.update()

        
    def increase_speed(self, increase = 0.05):
        self.speed += increase
        self.ball.x_vel *= -self.speed
        self.ball.y_vel = self.ball.y_vel*self.speed + uniform(-0.1,0.1)

        self.left_paddle.VEL *= self.speed
        self.right_paddle.VEL *= self.speed

    def handle_ball_collision(self):
        next_ball_x = self.ball.x + self.ball.x_vel
        next_ball_y = self.ball.y + self.ball.y_vel

        if next_ball_y + self.ball.radius >= self.HEIGHT or next_ball_y - self.ball.radius <= 0:
            self.ball.y_vel *= -1

        if self.ball.x_vel < 0:
            if next_ball_y >= self.left_paddle.y and next_ball_y <= self.left_paddle.y + self.left_paddle.height:
                if next_ball_x - self.ball.radius <= self.left_paddle.x + self.left_paddle.width:                

                    middle_y = self.left_paddle.y + self.left_paddle.height/2
                    difference_in_y = self.ball.y - middle_y
                    reduction_factor = (self.left_paddle.height/2) / self.ball.MAX_VEL
                    self.ball.y_vel = (difference_in_y / reduction_factor) 

                    self.increase_speed(0.05)
                    self.left_hits += 1


        else:
            if next_ball_y >= self.right_paddle.y and next_ball_y <= self.right_paddle.y + self.right_paddle.height:
                if next_ball_x + self.ball.radius >= self.right_paddle.x:

                    middle_y = self.right_paddle.y + self.right_paddle.height/2
                    difference_in_y = self.ball.y - middle_y
                    reduction_factor = (self.right_paddle.height/2) / self.ball.MAX_VEL
                    self.ball.y_vel = (difference_in_y / reduction_factor)

                    self.increase_speed(0.05)
                    self.right_hits += 1



    def move_paddle(self, left=True, up=True):

        if left:
            if up and self.left_paddle.y - self.left_paddle.VEL < 0:
                return False
            if not up and self.left_paddle.y + self.PADDLE_HEIGHT > self.HEIGHT:
                return False
            self.left_paddle.move(up)
        else:
            if up and self.right_paddle.y - self.right_paddle.VEL < 0:
                return False
            if not up and self.right_paddle.y + self.PADDLE_HEIGHT > self.HEIGHT:
                return False
            self.right_paddle.move(up)

        return True

    def loop(self):
        self.ball.move()
        self.handle_ball_collision()
        if self.ball.x <= 0:
            self.right_score += 1

            self.ball.reset()
            self.left_paddle.reset()
            self.right_paddle.reset()
            self.speed = 1

        elif self.ball.x + self.ball.radius >= self.WIDTH:
            self.left_score += 1

            self.ball.reset()
            self.left_paddle.reset()
            self.right_paddle.reset()   
            self.speed = 1

        game_info = GameInformation(self.left_score, self.left_hits, self.right_hits, self.right_score)

        return game_info

    def reset(self):
        """Resets the entire game."""
        self.ball.reset()
        self.left_paddle.reset()
        self.right_paddle.reset()
        self.left_score = 0
        self.right_score = 0
        self.speed = 1

