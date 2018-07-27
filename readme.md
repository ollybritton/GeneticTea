# GeneticTea

## What?

GeneticTea is a python script that reproduces the evolutionary model to generate
the optimal cup of tea. It's completely based on a python script with the same name
developed by ollybritton. This is a link to the original [GeneticTea](https://github.com/ollybritton/GeneticTea) script.

I express my gratitud towards **ollybritton** for developing such a wonderful script and also making it public here on GitHub for all of us to see, learn from and modifiy.

## What's new about it?

The original GeneticTea implemented the evolutionary model by perfectily reproducing all
its conditions. I found, nevertheless, that one of them was missing: the exchange of genes 
between an individual (a cup of tea) and another to produce offspring of the next generation. 
Instead, the original program only mutated by a small factor the better cup of teas and removed the less
adapted ones. In other words, chromosomatic exchange and actual reproduction were not reproduced.
Both this things are now implemented.

Also some properties of the teas were added while others were removed. Teas no longer
have milkiness, are now composed by three ingredients (apart of the obvious sack of tea),
and each ingredient is defined with its own ammount. This will produce more complex and
tasty teas!

## How to

To run the program, download the repo and `cd` into it. Then run the command:

    python3 natural_selection.py

## How it works

Each tea contains a chromosome, which is a set of gens. This set of genes
define the sweetness, brewing time and ingredients of the tea. This chromosomes
are stored in the following format:

    {
      0: first ingredient of the tea,
      1: second ingredient of the tea,
      2: third ingredient of the tea,
      3: amount of the first ingredient,
      4: amount of the second ingredient,
      5: amouunt of the third ingredient,
      6: sweetness of the tea,
      7: brew time of the tea
     }



where each value is a gen that defines what follows it. All of this
values, except the ingredients, are numbers from 0.1 to 1, where 1 is "very" or
"a lot of" and 0.1 is "a little bit of" or "just a little of". 0.5 is
"a regular ammount". For instance,

    4: 0.2
    5: 0.9
    6: 0.5

defines a tea with a bit of the second ingredient, a lot of the third ingredient
and just the regular ammount of sweetness.

Firstly, an initial set of teas (the initial population) is generated, each tea
with randomly generated chromosomes and thus different ingredients and qualities.
After trying the teas, you are to rank them from 0 to 9, where 0 is disgusting
and 9 is perfect. You are to input value separated by a comma,

    n,m,x,y...

where the first value corresponds to the first tea, the second value to the second
tea, and so on.

After the initial population was ranked by you, the 5 superior teas will
reproduce between themselves, crossing their genes randomly with one another,
thus producing an offspring. This offspring passes also through a very minor
mutation process which is likely to change some of its values. When this is over,
you'll be showned the offspring as a new set of teas. This second generation
will pass through the same process: ranking, crossover and mutation, to produce
a new generation, until this repeating process boils down to one optimal cup
of tea.

The process is slow because it requires a human to taste the teas in order to
rank them, i.e. it is not capable of recognizing the fitness of an individual
of the population by itself. Nevertheless, depending on how many teas per day
you drink, you can easily reach the optimal tea in a week or two.
