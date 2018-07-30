
import random
import math
from colorama import Fore, Style

ingredients = ["peppermint", "peperina", "ginger", "apple slices", "lemon juice",
               "lemon zest", "orange juice", "orange zest",
               "honey", "chamomile", "cinnamon", "black pepper", "garlic",
               "clove", "oregano", "rosemary"]

names = ["Coleridge", "Whitman", "Blake", "Thomas", "Frost", "Borges", "Cervantes",
         "Shakespeare", "Montaigne", "Vallejo", "Sun-Tzu", "Daniela", "Guevara",
         "Zapata", "Materno", "Beckford", "Torquato", "Otoño", "Invierno", "Verano",
         "RuPaul", "Bastos", "Aires claros", "Buena Mezcla", "Certidumbre"]

pre_names = ["de ", "Gran ", "por ", "desde ", "para "]

chosen_names = []


class Tea ():

    def __init__(self):

        self.name = self.random_name()
        self.ing_a = self.define_ingredient()
        self.ing_b = self.define_ingredient()
        self.ing_c = self.define_ingredient()
        self.am_a = random.randint(10, 100) / 100
        self.am_b = random.randint(1, 100) / 100
        self.am_c = random.randint(1, 100) / 100
        self.sweetnes = random.randint(1, 100) / 100
        self.brew_time = random.randint(2, 5)
        self.rate = 0

        self.genes = {0: self.ing_a, 1: self.ing_b, 2: self.ing_c, 3: self.am_a,
                      4: self.am_b, 5: self.am_c, 6: self.sweetnes, 7: self.brew_time}

    def __str__(self):

            tea_str = (Style.BRIGHT + Fore.RED + "   Name: " + Fore.CYAN + self.name
                       + "\n\n" + Fore.GREEN + "   Ingredients: \n\n"
                       + "      - " + str(self.genes[3]) + " " + self.genes[0] + "\n"
                       + "      - " + str(self.genes[4]) + " " + self.genes[1] + "\n"
                       + "      - " + str(self.genes[5]) + " " + self.genes[2] + "\n\n"
                       + Fore.RED + "   Sweetness : " + str(self.genes[6]) + "\n"
                       + "   Brew Time: " + str(self.genes[7])
                       + "\n\n--- --- --- --- --- --- --- --- ---\n")

            return tea_str

    def random_name(self):

        num = random.randint(0, 3)
        name = random.choice(names)

        while name in chosen_names:
            name = random.choice(names)

        if num is 3:
            name = random.choice(pre_names) + name

        chosen_names.append(name)

        return name

    def define_ingredient(self):

        ingr = random.choice(ingredients)

        try:
            while ingr == self.ing_a or ingr == self.ing_b:
                ingr = random.choice(ingredients)

        except AttributeError:
            return ingr

        return ingr


class Population ():

    def __init__(self):

        self.generation = self.cast_tea_generation()

    def display_population(self):

        for individual in self.generation:
            print(str(individual) + "\n")

    def cast_tea_generation(self):

        generation = []

        for i in range(10):
            generation.append(Tea())

        return generation

    def crossover(self):

        already_coupled = []

        if len(self.generation) > 1:

            for specimen in self.generation:

                # por each specimen of the generation

                couple = random.choice(self.generation)
                safe_count = 0

                while couple is specimen or couple in already_coupled:
                    couple = random.choice(self.generation)
                    safe_count += 1

                    if safe_count > 10:
                        couple = random.choice(self.generation)
                        while couple == specimen:
                            couple = random.choice(self.generation)
                        break

                # asign a couple that's not the specimen itself nor an already
                # reproduced individual.

            already_coupled.extend([specimen, couple])

            cross_point_a, cross_point_b = random.randint(0, 4), random.randint(1, 5)

            while cross_point_b < cross_point_a or cross_point_a == cross_point_b:
                cross_point_b = random.randint(1, 5)

            # asign cross_points: the genes from which point to which point of
            # the chromosome will be exchanged.

            for i in range(cross_point_a, cross_point_b):

                old_spec_chromosome = specimen.genes[i]

                specimen.genes[i] = couple.genes[i]
                couple.genes[i] = old_spec_chromosome

                # for each gen of the fragment of the chromosome that will be
                # exchanged, exchange those of the specimen with those of the couple
                # and those of the couple with those of the specimen.

    def rank_population(self):

        tea_rates = []

        rating = input(Fore.GREEN + """     Rate the teas with values from 0 to 9,
        including decimals, such as 6.3 or 7.5. Write each value separated only
        by a coma (no space), like n,m,x,y... and so. Make sure you rate every tea!

        Press e to exit at any time. The current generation of teas will be stored
        and you'll be able to pick up from where you left it whenever you want!\n\n""")

        rating = rating.replace(",", "")

        if rating is not "e":

            if len(rating) < len(self.generation):
                print("You rated ", len(rating), "teas and there were ", len(self.generation))

            for number in rating:
                tea_rates.append(int(number))

            indexer = 0
            for i in tea_rates:

                self.generation[indexer].rate = tea_rates[indexer]
                indexer += 1

            tea_rates.clear()

        else:

            exit()

    def optimal_tea(self):

        if len(self.generation) <= 1:

            print("\n ----- OPTIMAL TEA! -----\n")
            print(self.generation[0])
            print("\n Enjoy it!")

            return True

        return False
