# coding=utf-8

""" A genetic algorithm to brew the perfect cup of tea. """

import random, heapq, math, time

class colors:
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    reset = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
    blue = '\033[94m'

adjectives = ["Wonderous", "Heroic", "Bold", "Daring", "Epic", "Fearless", "Courageous", "Grand", "Gallant", "Gusty", "Nobel", "Dauntless", "Fire-Eating", "Dragon-Slaying", "Unafraid", "Lion-Hearted", "Triamphant"]
nouns = ["Brew", "Tea", "Cuppa", "Cup", "Blend", "Melange", "Medley", "Beverage", "Liquid"]

base_tea = {
    "name": "",
    "brew_time": 0,
    "milk": 0,
    "sweeteners": 0,
    "fitness": 0,
}

def random_name():
    return random.choice(adjectives) + " " + random.choice(nouns)

def random_num(a, b, dp):
    return round( random.uniform(a, b), dp )

def random_bias(a, dp):
    return round( random.uniform(-a, a), dp )

def random_initial_tea():
    curr = base_tea.copy()

    curr["name"] = random_name()

    curr["brew_time"] = random_num(1, 5, 1)
    curr["milk"] = random_num(0.2, 1, 1)
    curr["sweeteners"] = random_num(1, 3, 0)

    curr["fitness"] = 0

    return curr

def mutate(tea):
    curr = tea.copy()

    curr["brew_time"] += random_bias(.5, 1)
    curr["milk"] += random_bias(0.2, 1)
    curr["sweeteners"] += random_bias(1, 0)

    return curr

def initial_teas():
    curr = {}
    for i in range(10):
        curr[i] = random_initial_tea()

    return curr

def rank_teas(var, rank_arr):
    curr = var
    keys = list( var.keys() )

    for i in range( len(var) ):
        curr[ keys[i] ]["fitness"] = rank_arr[i]

    return curr

def natrual_selection(var):
    population_size = len(var)

    next_population_size = int( math.floor( population_size/2 ) )
    keys = list( var.keys() )

    new_population = var
    fittest_keys = sorted( keys, key = lambda x: var[x]["fitness"], reverse = True )[0:next_population_size]

    for i in range( len(new_population) ):
        if keys[i] not in fittest_keys:
            del new_population[ keys[i] ]

    return new_population

def do_generation(var):
    curr = var
    keys = list( curr.keys() )
    for i in range( len(curr) ):
        curr[ keys[i] ] = mutate( curr[ keys[i] ] )

    return curr

def evolutions_left(var):
    i = len(var)
    count = 0
    while True:
        if i == 1:
            return count
        else:
            count += 1
            i = math.floor(i/2)

def evolve_remaining(var):
    curr = var
    for i in range( evolutions_left(curr) ):
        yellow("Please enter the rank of each of tea in an array format. [4,5,6,2...]")
        teas = rank_teas(curr, eval(input()))
        teas = natrual_selection(teas)
        if len(curr) != 1:
            do_generation(teas)
            yellow("Current remaining teas:")
            show_teas(teas)
        else:
            key = list( curr.keys() )
            green("So, the best cup of tea is the...")
            time.sleep(1)
            show_teas(teas)
            line()
            green("What? And you only had to drink 18 cups of tea to find out!")



def show_teas(var):
    keys = list(var.keys())
    time.sleep(0.7)
    for i in range(0, len(var)):
        print("")
        print(colors.yellow + "– " + var[ keys[i] ]["name"] + ":" + colors.reset)
        print(colors.red + "\t– Brew Time: " + str(var[keys[i]]["brew_time"]) + colors.reset)
        print(colors.red + "\t– milkiness: " + str(var[keys[i]]["milk"]) + colors.reset)
        print(colors.red + "\t– Sweeteners: " + str(var[keys[i]]["sweeteners"]) + colors.reset)
        print(colors.red + "\t– Fitness: " + str(var[keys[i]]["fitness"]) + colors.reset)
        print("")
        time.sleep(0.2)

    with open("saves.txt", "a") as myfile:
        myfile.write(str(var) + "\n")

    if len(var) != 1:
        print( colors.green + "Current python dictionary (copy it to save or find it in the saves.txt file):" + colors.reset)
        print( colors.blue + str(var) + colors.reset )
        line()


def yellow(str):
    print( colors.yellow + str + colors.reset )

def red(str):
    print( colors.red + str + colors.reset )

def blue(str):
    print( colors.blue + str + colors.reset )

def green(str):
    print( colors.green + str + colors.reset )

def logo():
    green(" ██████╗ ███████╗███╗   ██╗███████╗████████╗██╗ ██████╗    ████████╗███████╗ █████╗\n██╔════╝ ██╔════╝████╗  ██║██╔════╝╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔════╝██╔══██╗\n██║  ███╗█████╗  ██╔██╗ ██║█████╗     ██║   ██║██║            ██║   █████╗  ███████║\n██║   ██║██╔══╝  ██║╚██╗██║██╔══╝     ██║   ██║██║            ██║   ██╔══╝  ██╔══██║\n╚██████╔╝███████╗██║ ╚████║███████╗   ██║   ██║╚██████╗       ██║   ███████╗██║  ██║\n ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚══════╝╚═╝  ╚═╝")

def line():
    print("")

def run():
    logo()
    blue("Welcome to GeneticTea, an evolutionary algorithm to brew the perfect cup of tea.")
    line()
    yellow("Have you got a save? (y/n or h for help)")
    save_bool = input()

    if save_bool == "y":
        yellow("Please paste your save:")
        teas = eval( input() )
        if len(teas) not in [10, 5, 2, 1]:
            red("That tea save is invalid, as it is " + str( len(teas) ) + " in length, meaning it is not the result of evolution from this program. They are usally either 10,5,2 or 1 in size.")

        else:
            yellow("Here are your teas!")
            show_teas(teas)
            teas = evolve_remaining(teas)

    elif save_bool == "n":
        yellow("Ok, generating the teas...")
        time.sleep(0.6)
        teas = initial_teas()
        yellow("Right: Here are your first ten teas:")
        time.sleep(0.3)
        show_teas(teas)
        teas = evolve_remaining(teas)

    elif save_bool == "h":
        line()
        blue("=" * 101)
        green("GeneticTea is a python script that uses the theory of evolution to generate the perfect cup of tea.")
        line()

        green("When it starts, it will generate 10 random cups of tea. It will show you these, giving each a unique")
        green("name, brew time, milkiness and sweetener amount.")
        line()

        blue("Brew Time: How long the tea is brewed for in minutes.")
        blue("milkiness: How milky your tea is, 0 = no milk and 1 = really milky.")
        blue("Sweeteners: How many sweeteners or sugars to put in the tea.")
        line()

        green("When the program starts, you can either choose to use a previous \"save\", or generate a new set of")
        green("teas. Using a save just means copying and pasting a previous dictionary from the saves.txt file.")
        green("Once it's generated the teas, you need to score the teas and keep a track of these scorings.")
        green("You should do something like this:")
        line()

        blue("Tea 1: 8/10, Tea 2: 5/10, Tea 3: 9/10...")
        line()

        green("Now you need to type these into the computer, in the following format:")
        line()

        blue("[8,5,9...]")
        blue("You can also do things like [0.8, 0.5, 0.9] and [8.2, 5.8, 9.3]")
        line()

        red("Note: This needs to be done for every tea, or it will give an error.")
        green("The program will then kill off the 5 least-scoring teas, and then \"mutate\" the remaining ones, ")
        green("which is basically changing the above variables ever so slightly. You then need to drink the teas that")
        green("are displayed afterwards. Repeat this process, until it gives you a final cup of tea – which should be the best!")
        blue("=" * 101)

    else:
        red("That is not a valid command. Please re-run the program.")

run()
