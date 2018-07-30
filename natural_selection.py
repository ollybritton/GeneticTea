import math
from lib import brewery
from colorama import Fore


def natural_selection(population):

    population_size = len(population.generation)
    next_population_size = math.floor(population_size / 2)

    new_generation = sorted(population.generation, key=lambda x: x.rate, reverse=True)[0:next_population_size]
    # la nueva generación serán los x especímenes con la puntuación más alta,
    # donde x representa el tamaño de la nueva generación (x = cur_gen / 2).

    population.generation = new_generation


def main():

    choise = input(Fore.GREEN + """Do you have a generation brewing already?
    Type 'y' to load the last generation or n to start a new one.""")

    if choise is "n":

        litter = brewery.Population()
        generation_num = 1

        while True:  # while the optimal tea is not breed.

            print("\n -------- GENERATION " + str(generation_num) + " --------\n")

            if len(litter.generation) <= 1:
                break

            litter.display_population()
            litter.rank_population()
            natural_selection(litter)
            litter.crossover()
            generation_num += 1

        litter.optimal_tea()


main()
