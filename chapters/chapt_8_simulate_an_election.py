#####-----------------------------------------------------------------------
######My solution
####
####import random
####def who_win(probability):
####    if random.random() <= probability:
####        return "A"
####    else:
####        return "B"
####all_wins_a = 0
####elections = 10_000
####for choice in range(elections):
####    a_win_in_rejons = 0
####    for i in range(1, 4):
####        if i == 1:
####            if who_win(.87) == "A":
######                print(f"{i} A")
####                a_win_in_rejons = a_win_in_rejons + 1
######            else:
######                print(f"{i} B")
####        elif i == 2:
####            if who_win(.65) == "A":
######                print(f"{i} A")
####                a_win_in_rejons = a_win_in_rejons + 1
######            else:
######                print(f"{i} B")
####        elif i == 3:
####            if who_win(.17) == "A":
######                print(f"{i} A")
####                a_win_in_rejons = a_win_in_rejons + 1
######            else:
######                print(f"{i} B")
####    if a_win_in_rejons >= 2:
####        all_wins_a = all_wins_a + 1
######    print(f"a_win_in_rejons {a_win_in_rejons}")
######    print("-----")
####
####print(f"Probability A wins: {all_wins_a / elections}")
####
#####-----------------------------------------------------------------------
#####-----------------------------------------------------------------------
### Not my solutions:
##
### 8.9 - Challenge: Simulate an Election
### Solution to challenge
##
##
### Simulate the results of an election using a Monte Carlo simulation
##
##from random import random
##
##num_times_A_wins = 0
##num_times_B_wins = 0
##
##num_trials = 10_000
##for trias in range(0, num_trials):
##    votes_for_A = 0
##    votes_for_B = 0
##
##    # Determine who wins the 1st region
##    if random() < 0.87:
##        votes_for_A = votes_for_A + 1
##    else:
##        votes_for_B = votes_for_B + 1
##
##    # Determine who wins the 2st region
##    if random() < 0.65:
##        votes_for_A = votes_for_A + 1
##    else:
##        votes_for_B = votes_for_B + 1
##
##    # Determine who wins the erd region
##    if random() < 0.17:
##        votes_for_A = votes_for_A + 1
##    else:
##        votes_for_B = votes_for_B + 1
##
##    # Determine overall election outcome
##    if votes_for_A > votes_for_B:
##        num_times_A_wins = num_times_A_wins + 1
##    else:
##        num_times_B_wins = num_times_B_wins + 1
##
##print(f"Probability A wins: {num_times_A_wins / num_trials}")
##print(f"Probability B wins: {num_times_B_wins / num_trials}")
##
###-----------------------------------------------------------------------
# 8.9 - Challenge: Simulate an Election
# Alternate solution to challenge

# Simulate the results of an election using a Monte Carlo simulation

from random import random

def run_ragional_elections(chance_A_wins):
    """Return the result of a regional election, either "A" or "B".

    The chances of "A" winning are determined by chance_A_wins.
    """
    if random() < chance_A_wins:
        return "A"
    else:
        return "B"

def run_election(regional_chances):
    """Return the result of an election, either "A" or "B".

    regional chances is a list or tuple of floats represrntion the
    chances that candidate "A" will win in each region.

    For example, run_election([.2, .5, .7]) will run an election with
    three regions where candidate "A" has a 20% chance to win in the
    first region, 50% in the second, and 70% in the third.
    """
    num_regions_won_by_A = 0
    for chance_A_wins in regional_chances:
        if run_ragional_elections(chance_A_wins) == "A":
            num_regions_won_by_A = num_regions_won_by_A + 1

    # Return the resuls. Note that the number of regions won by candidate
    # "B" is the total number of regions minus the number of regions won by
    # candidate "A". The total number of regions is the same as the length
    # of the regional_chances list.
    num_regions_won_by_B = len(regional_chances) - num_regions_won_by_A
    if num_regions_won_by_A > num_regions_won_by_B:
        return "A"
    else:
        return "B"

CHANCES_A_WINS_BY_REGION = [0.87, 0.65, 0.17]
NUM_TRIALS = 10_000

# Run the Monte-Carlo simulation
num_times_A_wins = 0
for trial in range(NUM_TRIALS):
    if run_election(CHANCES_A_WINS_BY_REGION) == "A":
        num_times_A_wins = num_times_A_wins + 1

# Display the probabilities that candidate A or candidate B wins the
# election. Note the probability that B wins can be calculated by
# subtracting the probability that A wins from 1.
print(f"Probability A wins: {num_times_A_wins / NUM_TRIALS}")
print(f"Probability B wins: {1 - (num_times_A_wins / NUM_TRIALS)}")

    
###-----------------------------------------------------------------------
###-----------------------------------------------------------------------
