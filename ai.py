from invasion_game import Game
import pygame
import neat
import os
import pickle
import time

class Invasion_Game:
    def __init__(self, window, width, height):
        self.game = Game(window, width, height)  

    def test_ai(self, genome, config):
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        
        last_shot = time.time()

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            output = net.activate((self.game.enemy.x, self.game.enemy.y, self.game.player.angle))
            decision = output.index(max(output))

            if decision == 0:
                pass
            elif decision == 1:
                self.game.player.rotate(True)
            elif decision == 2:
                self.game.player.rotate(False)

            if time.time() >= last_shot + 0.1:
                self.game.player.shoot()
                last_shot = time.time()

            game_info = self.game.loop()

            self.game.draw()
            pygame.display.update()
            pygame.time.Clock().tick(120)
        
        pygame.quit()

    def train_ai(self, genome, config):
        init_time = time.time()
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        
        last_shot = time.time()

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            output = net.activate((self.game.enemy.x, self.game.enemy.y, self.game.player.angle))
            decision = output.index(max(output))

            if decision == 0:
                pass
            elif decision == 1:
                self.game.player.rotate(True)
            elif decision == 2:
                self.game.player.rotate(False)

            if time.time() >= last_shot + 0.1:
                self.game.player.shoot()
                last_shot = time.time()

            game_info = self.game.loop()

            self.game.draw()
            pygame.display.update()
            #pygame.time.Clock().tick(120)

            if time.time() >= init_time + 1:
                self.calculate_fitness(genome, game_info)
                break
        
    def calculate_fitness(self, genome, game_info):
        genome.fitness += game_info.score


def eval_genomes(genomes, config):
    width, height = 700, 500
    window = pygame.display.set_mode((width, height))

    for i, (genome_id, genome) in enumerate(genomes):
        genome.fitness = 0
        for j in range(4):
            game = Invasion_Game(window, width, height)
            game.train_ai(genome, config)

def run_neat(config):
    p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-33')
    #p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(50))

    winner = p.run(eval_genomes, 550)
    with open("best.pickle", "wb") as f:
        pickle.dump(winner, f)


def test_ai(config):
    width, height = 700, 500
    window = pygame.display.set_mode((width, height))
    
    with open("best.pickle", "rb") as f:
        winner = pickle.load(f)
    
    game = Invasion_Game(window, width, height)
    game.test_ai(winner, config)

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    run_neat(config)
    #test_ai(config)