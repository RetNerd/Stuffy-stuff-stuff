import numpy
import GA2
from testsq import testsq

# Number of the weights we are looking to optimize.
num_weights = 1

sol_per_pop = 20
num_parents_mating = 2

# Defining the population size.
pop_size = (sol_per_pop,num_weights) # The population will have sol_per_pop chromosome where each chromosome has num_weights genes.
#Creating the initial population.
new_population = numpy.random.uniform(low=-10.0, high=10.0, size=pop_size)
#print(new_population)

num_generations = 50
for generation in range(num_generations):
	print("Generation : ", generation)
	# Measing the fitness of each chromosome in the population.
	fitness = GA2.cal_pop_fitness(new_population)

	# Selecting the best parents in the population for mating.
	parents = GA2.select_mating_pool(new_population, fitness, num_parents_mating)

	# Generating next generation using crossover.
	offspring_crossover = GA2.crossover(parents, offspring_size=(pop_size[0]-parents.shape[0], num_weights))
	#print(offspring_crossover)

	# Adding some variations to the offsrping using mutation.
	offspring_mutation = GA2.mutation(offspring_crossover)
	#print(offspring_mutation)

	# Creating the new population based on the parents and offspring.
	new_population[0:parents.shape[0], :] = parents
	new_population[parents.shape[0]:, :] = offspring_mutation

	# The best result in the current iteration.
	print("Best result : ", numpy.min(GA2.cal_pop_fitness(new_population)))

# Getting the best solution after iterating finishing all generations.
#At first, the fitness is calculated for each solution in the final generation.
fitness = GA2.cal_pop_fitness(new_population)
# Then return the index of that solution corresponding to the best fitness.
best_match_idx = numpy.where(fitness == numpy.min(fitness))

if isinstance(best_match_idx, list):
	best_match_idx = best_match_idx[0]

print("Best solution : ", new_population[best_match_idx, :])
print("Best solution fitness : ", fitness[best_match_idx])

testsq(new_population[best_match_idx, :][0][0])
