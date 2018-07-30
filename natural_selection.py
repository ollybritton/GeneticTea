import math
from lib import brewery
from colorama import Fore
import pickle


def natural_selection(population):

    population_size = len(population.generation)
    next_population_size = math.floor(population_size / 2)

    new_generation = sorted(population.generation, key=lambda x: x.rate, reverse=True)[0:next_population_size]
    # la nueva generación serán los x especímenes con la puntuación más alta,
    # donde x representa el tamaño de la nueva generación (x = cur_gen / 2).

    population.generation = new_generation


def save_population(population):

    with open('save', 'wb') as f:
        pickle.dump(population, f)
        print("\n\n POPULATION SAVED \n\n")


def load_population():

    with open('save', "rb") as f:
        population = pickle.load(f)
        print("\n\n POPULATION LOADED \n\n")

    return population


def main():

    choise = input(Fore.GREEN + """Do you have a generation brewing already?
    Type 'y' to load the last generation or "n" to start a new one.""")

    if choise is "n":

        litter = brewery.Population()

    if choise is "y":

        litter = load_population()

    while True:  # while the optimal tea is not breed.

        print("\n -------- GENERATION " + str(litter.generation_num) + " --------\n")

        save_population(litter)

        if len(litter.generation) <= 1:
            break

        litter.display_population()
        litter.rank_population()
        natural_selection(litter)
        litter.crossover()
        litter.generation_num += 1

    litter.optimal_tea()


main()
