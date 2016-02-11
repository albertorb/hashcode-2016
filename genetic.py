"""
Genetic algorithm for picture drawing proposed at google hashcode as practice exercise.
"""
import random
from heapq import nlargest
from score_image import score_image_with_commands

class GeneticAlgorithm:
    """
    Genetic algorithm implementation
    """

    def __init__(self, POPULATION_SIZE, GENERATIONS, MUTATION_PROB, CROSSOVER_PROB, ROWS, COLS, IMAGE):
        """
        Initialize instance
        """
        self.POPULATION_SIZE = POPULATION_SIZE
        self.GENERATIONS = GENERATIONS
        self.MUTATION_PROB = MUTATION_PROB
        self.CROSSOVER_PROB = CROSSOVER_PROB
        self.IMAGE = IMAGE
        self.COLS = COLS
        self.ROWS = ROWS
        self.OPS = (0,1,2)
        self.RANDOM_CHOICE = 20
        self.ELITE_CHOICE = 80
        self.POPULATION = []

    def init_individual(self):
        """
        initialize individual chromosome
        """
        commands = []
        for _ in range(random.randint(0,100)):
            random_op = random.randint(0,2)
            random_col = random.randint(0,self.COLS - 1)
            random_row = random.randint(0,self.ROWS - 1)
            individual = (random_op, random_row, random_col)
            if random_op == 1:
                aux_row = self.ROWS - random_row
                aux_col = self.COLS - random_col
                max_size = min(random_col, random_row, aux_col, aux_row) - 1
                if max_size > 0:
                    square_size = random.randint(0, max_size)
                else:
                    square_size = 0
                individual += (square_size, )
            if random_op == 2:
                vertical_horizontal_prob = random.randint(0,100)
                if vertical_horizontal_prob < 50:
                    random_row2 = random.randint(0, self.ROWS-1)
                    random_col2 = int(random_col)
                else:
                    random_col2 = random.randint(0, self.COLS-1)
                    random_row2 = int(random_row)
                individual += (random_row2, random_col2, )
            commands.append(individual)
        return commands

    def init_population(self):
        """
        Initialize population of chromosomes
        """
        population = [self.init_individual() for _ in range(self.POPULATION_SIZE)]
        self.POPULATION = population

    def fitness(self, commands):
        """
        Heuristic over the individuals
        """
        print commands
        score = 0
        is_perfect, score = score_image_with_commands(self.IMAGE, commands)
        score += score
        if is_perfect:
            score += 999999
        return score

    def mutation(self):
        """
        Mutate individual
        """
        prob = (self.MUTATION_PROB * self.POPULATION_SIZE) / 100
        for _ in range(int(prob)):
            chrom_indx = random.randint(0, self.POPULATION_SIZE - 1)
            chromosome = self.POPULATION[chrom_indx]
            command_indx = random.randint(0, len(chromosome) - 1)
            command = list(chromosome[command_indx])
            random_arg = random.randint(0, len(command) - 1)
            if random_arg == 0:
                new_op = random.randint(0,2)
                command[0] = new_op
            elif random.randint(0,100 < 50):
                command[random_arg] += 1
            else:
                command[random_arg] -= 1
            self.POPULATION[chrom_indx][command_indx] = command

    def crossover(self):
        """
        Generate new children
        """
        prob = (self.CROSSOVER_PROB * self.POPULATION_SIZE) / 100
        for _ in range(int(prob)):
            chrom_indx = random.randint(0, self.POPULATION_SIZE - 1)
            chromosome = self.POPULATION[chrom_indx]
            chrom_indx2 = random.randint(0, self.POPULATION_SIZE - 1)
            chromosome2 = self.POPULATION[chrom_indx2]
            pivot = random.randint(0, len(chromosome))
            part_one = chromosome[:pivot-1]
            part_two = chromosome[pivot:]
            child = part_one + part_two
            self.POPULATION.append(child)

    def selection(self):
        """
        Selects population for new generation
        """
        random_size = int((self.RANDOM_CHOICE * self.POPULATION_SIZE) / 100)
        elite_size = self.POPULATION_SIZE - random_size
        elites = nlargest(elite_size, self.POPULATION, key=self.fitness)
        randoms = random.sample(self.POPULATION, random_size)
        self.POPULATION = elites.extend(randoms)
