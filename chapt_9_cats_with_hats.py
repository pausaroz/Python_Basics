# 9.9 - Challenge: Cats With Hats
# Solution to challenge


def get_cats_with_hats(array_of_cats):
    cats_with_hats_on = []
    # We want to walk around the circle 100 times
    for num in range(1, 100 + 1):
        # Each time we walk around, we visit 100 cats
        for cat in range(1, 100 + 1):
            # Determine whether to visit the cat
            # Use modulo operator to visit every 2nd, 3rd, 4th,... etc.
            if cat % num == 0:
                # Remove or add hat depending on
                # whether the cat already has one
                if array_of_cats[cat] is True:
                    array_of_cats[cat] = False
                else:
                    array_of_cats[cat] = True

    # Add all number of each cat with a hat to list
    for cat in range(1, 100 + 1):
        if array_of_cats[cat] is True:
            cats_with_hats_on.append(cat)

    # Return the resulting list
    return cats_with_hats_on


# Cats contains whether each cat already has a hat on,
# by default all are set to false since none have been visited
cats = [False] * (100 + 1)
print(get_cats_with_hats(cats))


# 9.9 - Challenge: Cats With Hats
# Alternative solution to challenge


number_of_cats = 100
cats_with_hats = []
number_of_laps = 100

# We want the laps to be from 1 to 100 instead of 0 to 99
for lap in range(1, number_of_laps + 1):
    for cat in range(1, number_of_cats + 1):

        # Only look at cats that are divisible by the lap
        if cat % lap == 0:
            if cat in cats_with_hats:
                cats_with_hats.remove(cat)
            else:
                cats_with_hats.append(cat)

print(cats_with_hats)

### 9.9 - Challenge: Cats With Hats
### Alternative solution to challenge using dictionaries
##
##
##theCats = {}
##
### By default, no cats have been visited
### so we set every cat's number to False
##for i in range(1, 101):
##    theCats[i] = False
##
### Walk around the circle 100 times
##for i in range(1, 101):
##    # Visit all cats each time we do a lap
##    for cats, hats in theCats.items():
##        # Determine whether or not we visit a cat
##        if cats % i == 0:
##            # Add or remove the hat
##            if theCats[cats]:
##                theCats[cats] = False
##            else:
##                theCats[cats] = True
##
### Print whether each cat has a hat
##for cats, hats in theCats.items():
##    if theCats[cats]:
##        print(f"Cat {cats} has a hat.")
##    else:
##        print(f"Cat {cats} is hatless!")
