"""
"""
from genetic import GeneticAlgorithm

image = [[False for __ in xrange(50)] for _ in xrange(80)]
g = GeneticAlgorithm(100, 10, 5, 30, 50, 80, image)
g.init_population()
g.crossover()
g.mutation()
g.selection()
