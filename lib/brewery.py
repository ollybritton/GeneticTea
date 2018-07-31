
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
         "RuPaul", "Bastos", "Aires claros", "Buena Mezcla", "Certidumbre", "Faulkner",
         "Joyce", "Chesterton", "Wilde", "Wordsworth"]

pre_names = ["de ", "Gran ", "por ", "desde ", "para "] # this are in spanish :)

chosen_names = []


class Tea ():

    """Class that defines a tea through a chromosome that contains the genes of its
    sweetness, ingredients and brew time.

    A tea is a single specimen of the population to be evaluated."""

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

        self.chromosome = {0: self.ing_a, 1: self.ing_b, 2: self.ing_c, 3: self.am_a,
                      4: self.am_b, 5: self.am_c, 6: self.sweetnes, 7: self.brew_time}

    def __str__(self):

            tea_str = (Style.BRIGHT + Fore.RED + "   Name: " + Fore.CYAN + self.name
                       + "\n\n" + Fore.GREEN + "   Ingredients: \n\n"
                       + "      - " + str(self.chromosome[3]) + " " + self.chromosome[0] + "\n"
                       + "      - " + str(self.chromosome[4]) + " " + self.chromosome[1] + "\n"
                       + "      - " + str(self.chromosome[5]) + " " + self.chromosome[2] + "\n\n"
                       + Fore.RED + "   Sweetness : " + str(self.chromosome[6]) + "\n"
                       + "   Brew Time: " + str(self.chromosome[7])
                       + "\n\n--- --- --- --- --- --- --- --- ---\n")

            return tea_str

    def random_name(self):

        """Provides a random name for the instance of the Tea class."""

        num = random.randint(0, 3)
        name = random.choice(names)

        while name in chosen_names:
            name = random.choice(names)

        if num is 3:
            name = random.choice(pre_names) + name

        chosen_names.append(name)

        return name

    def define_ingredient(self):

        """Defines an ingredient for the instance of the Tea class such that is
        not repeated nor already used on the instance."""

        ingr = random.choice(ingredients)

        try:
            while ingr == self.ing_a or ingr == self.ing_b:
                ingr = random.choice(ingredients)

        except AttributeError:
            return ingr

        return ingr


class Population ():

    """Class that defines the population of teas to be evaluated. This population
    is a list of individuals named "generation". The generation is reduced to its
    half each time the fitness of its individuals is evaluated."""

    def __init__(self):

        self.generation = self.cast_tea_generation()
        self.generation_num = 1

    def display_population(self):

        """Displays the teas in a pretty way for the user to see their
        attributes."""

        for individual in self.generation:
            print(str(individual) + "\n")

    def cast_tea_generation(self):

        """Casts a generation of teas randomly to serve as a first generation of
        teas."""

        generation = []

        for i in range(10):
            generation.append(Tea())

        return generation

    def crossover(self):

        """Reproduces each specimen of the most fitted ones with a random couple
        chosen among the most fitted individuals as well. An individual that
        has reproduced already will not reproduce again, except with the last
        tea of the generation (otherwise the last tea will have no couple and
        won't reprouce at all).

        The crossover process is done by selecting two random points

        x, y,

        of the chromosome and exchanging every gene between x and y from the specimen
        to the couple and from the couple to the specimen."""

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

                old_spec_chromosome = specimen.chromosome[i]

                specimen.chromosome[i] = couple.chromosome[i]
                couple.chromosome[i] = old_spec_chromosome

                # for each gen of the fragment of the chromosome that will be
                # exchanged, exchange those of the specimen with those of the couple
                # and those of the couple with those of the specimen.

    def mutate_brew_time(self, brew_time):

        """The mutation of the brew time needed a lot of if statements to
        determine how much could be added or substracted from the brew time
        of a tea without going beyond the limits (1 and 5).

        For instance, of a brew time value of 4 we can substract any random
        value from 3 to 1, but we can only add 1 without going beyond the limit
        (which is 5). Of a brew time value of 1, we can substract nothing but
        we can add any value from 1 to 4.

        In few words, this function prevents the brew time to mutate beyond
        its limits."""

        bool = random.randint(0, 1)

        if brew_time is 3:

            if bool is 1:
                brew_time += random.randint(1, 2)
            elif bool is 0:
                brew_time -= random.randint(1, 2)

        elif brew_time is 4:

            if bool is 1:
                brew_time += 1
            elif bool is 0:
                brew_time -= random.randint(1, 3)

        elif brew_time is 5:

            brew_time -= random.randint(1, 4)

        elif brew_time is 2:

            if bool is 1:
                brew_time += random.randint(1, 3)
            elif bool is 0:
                brew_time -= 1

        elif brew_time is 1:
            brew_time += random.randint(1, 4)

    def mutation(self):

        """Puts every specimen of the generation under a chance of mutation.

        For reasons explained on the readme document, there's a 40% chances
        of a mutation on a non-crucial gen (those that define ammount of
        ingredients and brew time of the tea), while only 5% chances of mutation
        on crucial genes (those that define the ingredients of the tea.)"""

        if len(self.generation) > 2:  # If this are not the two last individuals.
                                    # Prevents the final tea from being mutated.

            for tea in self.generation:

                dice = random.randint(0, 100)

                if dice >= 60:

                    # mutate non-crucial genes

                    gen = random.randint(3, 7)
                    print("\n\nNON CRUCIAL GEN MUTATED ON \n", tea)
                    print("MUTATED GEN IS ", tea.chromosome[gen])

                    if gen is 7:

                        brew_time = tea.chromosome[gen]
                        self.mutate_brew_time(brew_time)

                    else:

                        tea.chromosome[gen] = random.randint(1, 100) / 100

                elif dice >= 54 and dice < 60:

                    # mutate crucial genes

                    gen = random.randint(0, 2)
                    print("\n\nCRUCIAL GEN MUTATED ON \n", tea)
                    tea.chromosome[gen] = random.choice(ingredients)

    def rank_population(self):

        """Expects an input from the user to rank the teas with the introduced
        values from 0 to 9, each value written in such a way that it's seperated
        from its adjacents by a comma:

        x,y,n,m...

        The first value is the fitness of the first tea, the second of the second
        tea, and so on."""

        tea_rates = []

        rating = input(Fore.GREEN + """     Rate the teas with values from 0 to 9,
        where 0 is disgusting and 9 is perfect. Write each value separated only
        by a coma (no space), like n,m,x,y... and so. Make sure you rate every tea!

        Press "e" to exit at any time. The current generation of teas will be stored
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

        """Displays the optimal tea with a happy message."""

        print("\n ----- OPTIMAL TEA! -----\n")
        print(self.generation[0])
        print("\n Enjoy it!")
