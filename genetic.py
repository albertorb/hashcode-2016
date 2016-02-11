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
        self.COLS = COLS
        self.ROWS = ROWS
        self.OPS = (0,1,2)
        self.RANDOM_CHOICE = 20
        self.ELITE_CHOICE = 80

    def init_individual(self):
        """
        initialize individual chromosome
        """
        random_op = random.randint(0,2)
        random_col = random.randint(0,self.COLS)
        random_row = random.randint(0,self.ROWS)
        individual = (random_op, random_col, random_row)
        if random_op == 1:
            max_values = [int(self.ROWS/random_row), int(self.COLS/random_col)]
            square_size = random.randint(0, min(max_values))
            individual += (square_size, )
        if random_op == 2:
            vertical_horizontal_prob = random.randint(0,100)
            if vertical_horizontal_prob < 50:
                random_row2 = random.randint(0, self.ROWS)
                random_col2 = int(random_col)
            else:
                random_col2 = random.randint(0, self.COLS)
                random_row2 = int(random_row)
            individual += (random_row2, random_col2, )
        return individual

    def init_population(self):
        """
        Initialize population of chromosomes
        """
        population = [init_individual for _ in range(self.POPULATION_SIZE)]
        return population

    def fitness(self, inidividual):
        """
        Heuristic over the individuals
        """
        score = 0
        is_perfect, score = score_image_with_commands(self.IMAGE, commands)
        score += score
        if is_perfect:
            score += 999999
        return score

    def mutation(self, population):
        """
        Mutate individual
        """
        prob = (self.MUTATION_PROB * self.POPULATION_SIZE) / 100
        for _ in range(int(prob)):
            chrom_indx = random.randint(0, len(self.POPULATION_SIZE - 1))
            chromosome = population[chrom_indx]
            command_indx = random.randint(0, len(chrom_indx))
            command = list(chromosome[command_indx])
            random_arg = random.randint(0, len(command))
            if random_arg == 0:
                new_op = random.randint(0,2)
                command[0] = new_op
            elif random.randint(0,100 < 50):
                command[random_arg] += 1
            else:
                command[random_arg] -= 1
            population[chrom_indx][command_indx] = command

    def crossover(self, population):
        """
        Generate new children
        """
        prob = (self.CROSSOVER_PROB * self.POPULATION_SIZE) / 100
        for _ in range(int(prob)):
            chrom_indx = random.randint(0, len(self.POPULATION_SIZE - 1))
            chromosome = population[chrom_indx]
            chrom_indx2 = random.randint(0, len(self.POPULATION_SIZE - 1))
            chromosome2 = population[chrom_indx2]
            pivot = random.randint(0, len(self.POPULATION_SIZE - 1))
            part_one = chromosome[:pivot-1]
            part_two = chromosome[pivot:]
            child = part_one.extend(part_two)
            population.append(child)

    def selection(self, population):
        """
        Selects population for new generation
        """
        random_size = int((self.RANDOM_CHOICE * self.POPULATION_SIZE) / 100)
        elite_size = self.POPULATION_SIZE - random_size
        elites = nlargest(elite_size, population, key=fitness)
        randoms = random.sample(population, random_size)
        population = elites.extend(randoms)
