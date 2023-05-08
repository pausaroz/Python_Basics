##### 8.8 - Challenge: Simulate a Coin Toss Experiment
##### Solution to challenge
####
####
##### Simulate the results of a series of coin tosses and track the results
####
##### This one is tricky to structure correctly. Try writing out the logic before
##### you start coding. Some additional pointers if you're stuck:
##### 1. You will need to use a `for` loop over a range of trials.
##### 2. For each trial, first you should check the outcome of the first flip.
##### 3. Make sure you add the first flip to the total number of flips.
##### 4. After the first toss, you'll need another loop to keep flipping while you
#####    get the same result as the first flip.
####
####import random
####
####
####def coin_flip():
####    """Randomly return 'heads' or 'tails'."""
####    if random.randint(0, 1) == 0:
####        return "heads"
####    else:
####        return "tails"
####
####
####flips = 0
####num_trials = 10_000
####
####for trial in range(num_trials):
####    if coin_flip() == "heads":
####        # Increment the number of flips by 1
####        flips = flips + 1
####        while coin_flip() == "heads":
####            # Keep incrementing the total number of flips
####            # until "tails" is returned by coin_flip()
####            flips = flips + 1
####        # Once coin_flip() return "tails", the loop will exit,
####        # but we need to add one more to flips to track the
####        # last flip that generated "tails"
####        flips = flips + 1
####    else:
####        # coin_flip() returned "tails" on the first flip.
####        # Increment the number of flips by 1
####        flips = flips + 1
####        while coin_flip() == "tails":
####            # Keep incrementing the total number of flips
####            # until "heads" is returned by coin_flip()
####            flips = flips + 1
####        # Once coin_flip() returns "heads", the loop will exit,
####        # but we need to add one more to flips to track the
####        # last flip that generated "heads"
####        flips = flips + 1
####
####avg_flips_per_trial = flips / num_trials
####print(f"The average number of flips per trial is {avg_flips_per_trial}.")
####
###------------------------------------------------------------------------
##
### 8.8 - Challenge: Simulate a Coin Toss Experiement
### Alternative solution to challenge
##
##
### Simulate the results of a series of coin tosses and track the results
##
### This one is tricky to structure correctly. Try writing out the logic before
### you start coding. Some additional pointers if you're stuck:
### 1. You will need to use a `for` loop over a range of trials.
### 2. For each trial, first you should check the outcome of the first flip.
### 3. Make sure you add the first flip to the total number of flips.
### 4. After the first toss, you'll need another loop to keep flipping while you
###    get the same result as the first flip.
##
##import random
##
##
##def coin_flip():
##    """Randomly return 'heads' or 'tails'."""
##    if random.randint(0, 1) == 0:
##        return "heads"
##    else:
##        return "tails"
##
##
##flips = 0
##num_trials = 10_000
##
##for trial in range(num_trials):
##    # Flip the coin once and increment the flips tally by 1
##    first_flip = coin_flip()
##    flips = flips + 1
##    # Continue flipping the coin and updating the tally until
##    # a different result is returned by coin_flips()
##    while coin_flip() == first_flip:
##        flips = flips + 1
##    # Increment the flip tally once more to account for the
##    # final flip with a different result
##    flips = flips + 1
##
##avg_flips_per_trial = flips / num_trials
##print(f"The average number of flips per trial is {avg_flips_per_trial}.")
##
###------------------------------------------------------------------------
# 8.8 - Challenge: Simulate a Coin Toss Experiement
# Alternative solution to challenge using functions


# Simulate the results of a series of coin tosses and track the results

# This one is tricky to structure correctly. Try writing out the logic before
# you start coding. Some additional pointers if you're stuck:
# 1. You will need to use a `for` loop over a range of trials.
# 2. For each trial, first you should check the outcome of the first flip.
# 3. Make sure you add the first flip to the total number of flips.
# 4. After the first toss, you'll need another loop to keep flipping while you
#    get the same result as the first flip.

import random


def single_trial():
    """Simulate repeatedly a coing  until both heads and tails are seen."""
    # This function uses random.randint() to simulate a single coin toss.
    # randing(0, 1) randomly returns 0 or 1 with equal probability. We can
    # use 0 to represent heads and 1 to represent tails.

    # Flip the coin the first time
    flip_result = random.randint(0, 1)
    # Keep a tally of how many times the coin has been flipped. We've only
    # flipped once so the initial count is 1.
    flip_count = 1

    # Continue to flip the coin until randint(0, 1) returns something
    # different than the original flip_result
    while flip_result == random.randint(0, 1):
        flip_count = flip_count + 1

    # The last step in the loop flipped the coin but didn't update the tally,
    # so we need to increase the flip_count by 1
    flip_count = flip_count + 1
    return flip_count


def flip_trial_avg(num_trials):
    """Calculate the average number of flips per trial over num_trials total trials."""
    total = 0
    for trial in range(num_trials):
        total = total + single_trial()
    return total / num_trials


print(f"The average number of coin flips was {flip_trial_avg(10_000)}")
#------------------------------------------------------------------------

