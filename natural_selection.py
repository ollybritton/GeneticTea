import math
from lib import brewery
from colorama import Fore
import pickle


def natural_selection(population):

    """Defines the new generation of a population of teas as that half of the
    generation that has higher fitness values, i.e. higher rankings from the user."""

    population_size = len(population.generation)
    next_population_size = math.floor(population_size / 2)

    new_generation = sorted(population.generation, key=lambda x: x.rate, reverse=True)[0:next_population_size]

    population.generation = new_generation


def save_population(population):

    """Saves the evaluated population as is for later use."""

    with open('save', 'wb') as f:
        pickle.dump(population, f)
        print("\n\n POPULATION SAVED \n\n")


def load_population():

    """Loads the last saved population."""

    with open('save', "rb") as f:
        population = pickle.load(f)
        print("\n\n POPULATION LOADED \n\n")

    return population


def main():

    """Main function. Offers to load a previous population or to generate a new
    one. Makes the population subject of the evolutionary model by displaying
    it, asking for user's rank, selecting the most fitted individuals,
    reproducing them and mutating their offspring and displaying the new
    generation to be ranked. Repeates the process until it boils down to
    one remaining cup of tea.

    Saves the population as is on each loop."""

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
        litter.mutation()
        litter.generation_num += 1

    litter.optimal_tea()


main()
