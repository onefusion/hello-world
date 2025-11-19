import random
def roll_dice(num_dice, sides):
    """
    Roll 'num_dice' dice, each with 'sides' number of sides.
    Returns a list containing each individual die result.
    """
    rolls = []
    for _ in range(num_dice):
        roll = random.randint(1, sides)
        rolls.append(roll)
    return rolls

# Sim 1000 rolls of single die
results = []

for _ in range(1000):
    roll_result = roll_dice(1, 20)
    results.append(roll_result[0])

# Print a frequency summary of results
print("Results after 1000 rolls of 1d20:")
for side in range(1, 21):
    count = results.count(side)
    print(f"{side}: {count}")