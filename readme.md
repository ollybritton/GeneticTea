# GeneticTea

## Wha???

GeneticTea is a python script that uses the theory of evolution to generate the perfect cup of tea.

## Prerequisites

Make sure that you have `python3` and `numpy` installed on your system. You can install `numpy` [here](http://www.numpy.org/).

To run the program, simply download the repo and `cd` into it, then run the command:

    python3 brew.py

When it starts, it will generate 10 random cups of tea. It will show you these, giving each a unique
name, brew time, milkiness and sweetener amount.

Brew Time: How long the tea is brewed for in minutes.
Milkiness: How milky your tea is, 0 = no milk and 1 = really milky.
Sweeteners: How many sweeteners or sugars to put in the tea.

When the program starts, you can either choose to use a previous "save", or generate a new set of
teas. Using a save just means copying and pasting a previous dictionary from the `saves.txt` file.
Once it's generated the teas, you need to score the teas and keep a track of these scorings.
You should do something like this:

Tea 1: 8/10, Tea 2: 5/10, Tea 3: 9/10...

Now you need to type these into the computer, in the following format:

[8,5,9...]
You can also do things like [0.8, 0.5, 0.9] and [8.2, 5.8, 9.3]

*Note: This needs to be done for every tea, or it will give an error.*

The program will then kill off the 5 least-scoring teas, and then "mutate" the remaining ones,
which is basically changing the above variables ever so slightly. You then need to drink the teas that
are displayed afterwards. Repeat this process, until it gives you a final cup of tea – which should be the best!

## How it works.

*Note: This is my first attempt at a genetic algorithm, so it's probably not very good.*

### Data Structure

Teas are stored in the following format:

    {
      name: A randomly generated name,
      fitness: 0 by default, but a measure of how good it is,
      brew_time: Time to brew for, in minutes,
      sweeteners: Amount of sweeteners,
      milkiness: How milky the tea is (0 = no milk, 1 = lots of milk)
    }

10 of these are "randomly" generated at the beginning, using the `initial_teas()` function, which itself is made using the `random_num(a, b, dp)`. `random_num()` is the same as doing `round( random.uniform(a,b), dp )`, but it looks cleaner.

*I say "randomly", because I have put some bounds on a few of the variables. For example, a tea that is brewed for 10 seconds isn't going to taste very good.*

If you're interested, these are the bounds:

- 1 <= `brew_time` <= 5
- 0.2 <= `milk` <= 1
- 1 <= `sweeteners` <= 3

The values shown are always the absolute value as well, as you can't brew a cup of tea for -3 minutes.

### The Evolution

Evolution is done by killing off the least scoring `floor(x/2)` members of the population, and then mutating the remaining ones by a small factor.

*Note: The final killing doesn't involve a mutation, as it may ruin the tea you just chose.*

Once again, here are the bounds for the variance:

- -0.5 <= `brew_variance` <= 0.5
- -0.2 <= `milk_variance` <= 0.2
- -1 <= `sweeteners` <= 1

Also, the values for `brew` and `milk` are limited to `1dp`, but `sweeteners` is always an integer (but it's type is still a float).

The change can be applied to a single tea using the `mutate(tea)` function, and you can mutate the entire dictionary of teas with `do_generation()`.
