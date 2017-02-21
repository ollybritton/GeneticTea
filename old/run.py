# coding=utf-8

""" A genetic algorithm to brew the perfect cup of tea. """

import numpy as np
import random, heapq, math, time

# Milk (1 = Lots), Sweeteners, Brew Time (In mins).
# 10 -> 5 -> 3 -> 2 -> 1

starting_teas = 10
adjectives = ["Wonderous", "Heroic", "Bold", "Daring", "Epic", "Fearless", "Courageous", "Grand", "Gallent", "Gusty", "Nobel", "Dauntless", "Fire-Eating", "Dragon-Slaying", "Unafraid", "Lion-Hearted"]
nouns = ["Brew", "Tea", "Cuppa", "Cup", "Blend", "Melange", "Medley"]
teas = {}

class colors:
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    reset = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
    blue = '\033[94m'

def random_name():
    return random.choice(adjectives) + " " + random.choice(nouns)

def random_milk(gen = 1, prev = 0):
    # Start at 0.5**2 = 0.25
    if(gen == 1):
        return round(random.uniform(0.3, 0.9), 1)
    else:
        return prev + round(random.uniform(-(0.5**gen), 0.5**gen), gen)

def random_sweetners(gen = 1, prev = 0):
    # Roughly 1 to 3.
    if(gen == 1):
        return round(random.uniform(1, 3), 0)
    else:
        return prev + round(random.uniform(-(0.5**gen), 0.5**gen), gen)

def random_brew_time(gen = 1, prev = 0):
    # Roughly 2mins to 4mins
    if(gen == 1):
        return round(random.uniform(2, 4), 0)
    else:
        return prev + round(random.uniform(-(0.5**(gen-1)), 0.5**(gen-1)), (gen-1))

soft_random = {

    "name": random_name,
    "milk": random_milk,
    "sweeteners": random_sweetners,
    "brew_time": random_brew_time

}


base_tea = {

    "brew_time": 0,
    "milk": 0,
    "sweeteners": 0,
    "name": "",
    "fitness": 0,

}

def create_base_teas():
    ret = {}

    for i in range(0, starting_teas):
        curr = base_tea.copy()

        curr["brew_time"] = soft_random["brew_time"]()
        curr["milk"] = soft_random["milk"]()
        curr["sweeteners"] = soft_random["sweeteners"]()
        curr["name"] = soft_random["name"]()

        ret[i] = curr

    return ret

def evolve_single_tea(var, index, gen):
    curr = var[index]

    curr["brew_time"] = soft_random["brew_time"](gen, curr["brew_time"])
    curr["milk"] = soft_random["milk"](gen, curr["milk"])
    curr["sweeteners"] = soft_random["sweeteners"](gen, curr["sweeteners"])

    return var

def rank_tea(arr, var):
    keys = list(var.keys())
    updated_fitness = var
    for i in range(0, len(var)):
        updated_fitness[ keys[i] ]["fitness"] = arr[i]

    return updated_fitness

def selection(var):
    #keys_best = sorted(keys, key=lambda x:var[x]['fitness'], reverse=True)[0:int(pop_size)]
    population_size = len(var)
    next_population_size = int( math.floor( population_size/2 ) )
    keys = list( var.keys() )

    new_population = var
    fittest_keys = sorted( keys, key = lambda x: var[x]["fitness"], reverse = True )[0:next_population_size]

    for i in range( len(new_population) ):
        if keys[i] not in fittest_keys:
            del new_population[ keys[i] ]

    return new_population

def evolve_teas(var, gen = 2):
    keys = list(var.keys())
    for i in range(0, len(var)):
        evolve_single_tea(var, var[i], gen)

def evolutions_left(var):
    i = len(var)
    count = 0
    while True:
        if i == 1:
            return count
        else:
            count += 1
            i = math.floor(i/2)

def show_teas(var):
    keys = list(var.keys())
    for i in range(0, len(var)):
        print("")
        print(colors.yellow + "– " + var[ keys[i] ]["name"] + ":" + colors.reset)
        print(colors.red + "\t– Brew Time: " + str( abs( var[keys[i]]["brew_time"])) + colors.reset)
        print(colors.red + "\t– Milkyness: " + str( abs( var[keys[i]]["brew_time"])) + colors.reset)
        print(colors.red + "\t– Sweeteners: " + str( abs( var[keys[i]]["sweeteners"])) + colors.reset)
        print(colors.red + "\t– Fitness: " + str(var[keys[i]]["fitness"]) + colors.reset)
        print("")
        time.sleep(0.1)

    print( colors.red + "Current python dictionary (copy it to save):" + colors.reset)
    print( colors.yellow + str(var) + colors.reset )

def evolve_remaining(var):
    change_var = var
    for i in range(1, evolutions_left(var)+1):
        print(colors.yellow + "Please rank the teas in an array format." + colors.reset)
        rank_tea(eval(input()), change_var)
        change_var = selection(change_var)

        print(colors.yellow + "Current Population:" + colors.reset)
        show_teas(change_var)

    return change_var

def run():
    print(colors.green  + " ██████╗ ███████╗███╗   ██╗███████╗████████╗██╗ ██████╗    ████████╗███████╗ █████╗\n██╔════╝ ██╔════╝████╗  ██║██╔════╝╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔════╝██╔══██╗\n██║  ███╗█████╗  ██╔██╗ ██║█████╗     ██║   ██║██║            ██║   █████╗  ███████║\n██║   ██║██╔══╝  ██║╚██╗██║██╔══╝     ██║   ██║██║            ██║   ██╔══╝  ██╔══██║\n╚██████╔╝███████╗██║ ╚████║███████╗   ██║   ██║╚██████╗       ██║   ███████╗██║  ██║\n ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚══════╝╚═╝  ╚═╝\n" + colors.reset)
    print(colors.blue + "Welcome to GeneticTea, a evolutionary algorithm for brewing the perfec cup of tea." + colors.reset)
    print(colors.yellow + "Have you got a save? (y/n)" + colors.reset)
    save = input()
    if save == "n":
        print(colors.yellow + "Press enter to start." + colors.reset)
        input()

        teas = create_base_teas()

        show_teas(teas)

        teas = evolve_remaining(teas)

    elif save == "y":
        print(colors.yellow + "Please enter the python dictionary." + colors.reset)
        teas = eval(input())

        if len(teas) not in [10, 5, 2, 1]:
            print( colors.red + "That tea save is invalid, as it is " + str( len(teas) ) + " in length, meaning it is not the result of evolution from this program."  )

        else:
            print( colors.yellow + "Cool! These are the current teas:" )
            show_teas(teas)

            teas = evolve_remaining(teas)

    else:
        print(colors.red + "That's not a choice. Please re-run the program.")

run()
