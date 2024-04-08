import neat.checkpoint
import pygame
from Pong import Game
import neat
import os
import pickle
import visualise 

pygame.init()


pygame.display.set_caption("Pong")
FPS  = 60




class PongGame :
    def __init__(self, WIN, WIDTH, HEIGHT):
        self.game = Game(WIN, WIDTH, HEIGHT)
        self.left_paddle = self.game.left_paddle
        self.right_paddle = self.game.right_paddle
        self.ball = self.game.ball

    def test_ai(self, genome, config):
        net = neat.nn.FeedForwardNetwork.create(genome, config)

        run = True
        clock = pygame.time.Clock()

        while run:

            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.game.move_paddle(left=True, up=True)
            if keys[pygame.K_s]:
                self.game.move_paddle(left=True, up=False)

            output = net.activate((self.right_paddle.y, self.ball.y, abs(self.right_paddle.x - self.ball.x)))
            decision = output.index(max(output))

            if decision == 0:
                pass
            elif decision == 1:
                self.game.move_paddle(left=False, up=True)
            elif decision == 2:
                self.game.move_paddle(left=False, up=False)

                
            self.game.loop()
            self.game.draw(True, True)
            pygame.display.update()

            if self.game.left_score == self.game.WINING_SCORE or self.game.right_score == self.game.WINING_SCORE:

                if self.game.left_score == self.game.WINING_SCORE:
                    win_text = "Left Player Wins"
                else:
                    win_text = "Right Player Wins"
                text = self.game.SCORE_FONT.render(win_text, 1, self.game.WHITE)
                self.game.WIN.blit(text, (self.game.WIDTH//2 - text.get_width()//2, self.game.HEIGHT//2 - text.get_height()//2))
                pygame.display.update()
                pygame.time.delay(2000)

                self.game.reset()
                
        pygame.quit()

    def train_ai(self, genome1, genome2, config):
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, config)

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            output1 = net1.activate((self.left_paddle.y, self.ball.y, abs(self.left_paddle.x - self.ball.x)))
            decsion1 = output1.index(max(output1))
            
            if decsion1 == 0:
                pass
            elif decsion1 == 1:
                self.game.move_paddle(left=True, up=True)
            elif decsion1 == 2:
                self.game.move_paddle(left=True, up=False)

            output2 = net2.activate((self.right_paddle.y, self.ball.y, abs(self.right_paddle.x - self.ball.x)))
            decision2 = output2.index(max(output2))
            
            if decision2 == 0:
                pass
            elif decision2 == 1:
                self.game.move_paddle(left=False, up=True)
            elif decision2 == 2:
                self.game.move_paddle(left=False, up=False)


            game_info = self.game.loop()
            
            self.game.draw(False, True)
            pygame.display.update()

            if game_info.left_score >= 1 or game_info.right_score >= 1 or game_info.left_hits >= 50:
                self.calculate_fitness(genome1, genome2, game_info)
                run = False
                break

    def calculate_fitness(self, genome1, genome2, game_info):
        genome1.fitness += game_info.left_hits
        genome2.fitness += game_info.right_hits

def eval_genomes(genomes, config):
    WIDTH, HEIGHT = 800, 600
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    for i ,(genome_id1, genome1) in enumerate(genomes):
        if i == len(genomes) - 1:
            break
        genome1.fitness = 0

        for genone_id2, genome2 in genomes[i+1:]:
            genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
            game = PongGame(WIN, WIDTH, HEIGHT)
            game.train_ai(genome1, genome2, config)

def run_neat(config):
    p = neat.Checkpointer.restore_checkpoint("neat-checkpoint-1")
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    winner = p.run(eval_genomes, 50)
    with open("winner.pkl", "wb") as f:
        pickle.dump(winner, f)
    # Visualize the winner network.
    visualise.draw_net(config, winner, True)

def test_ai(config):
    with open("winner.pkl", "rb") as f:
        winner = pickle.load(f)

    WIDTH, HEIGHT = 800, 600
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    game = PongGame(WIN, WIDTH, HEIGHT)
    game.test_ai(winner, config )

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")

    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)
    
    #run_neat(config)
    test_ai(config)

    # with open("winner.pkl", "rb") as f:
    #     winner = pickle.load(f)

    # visualise.draw_net(config, winner, True)