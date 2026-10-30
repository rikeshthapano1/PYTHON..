animals = ["cat", "dog", "rabbit", "hamster", "turtle"]
actions = ["jumped over", "ran around", "climbed on", "danced with", "played with"]
places = ["the park", "the house", "the tree", "the river", "the mountain"]

import random

choices = [random.choice(animals), random.choice(actions), random.choice(places)]

print(f"Once upon a time, a {choices[0]} {choices[1]} {choices[2]}.")