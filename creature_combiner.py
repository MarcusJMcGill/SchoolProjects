import random
import pandas as pd


class Creature:
    def __init__(self, name, weight, num_legs, can_fly, has_tail, aquatic, breathes_fire):
        self.name = name
        self.weight = weight
        self.num_legs = num_legs
        self.can_fly = can_fly
        self.has_tail = has_tail
        self.aquatic = aquatic
        self.breathes_fire = breathes_fire
        self.stats = [{"Name": name, "Weight in lbs": weight, "Number of Legs": num_legs, "Can Fly": can_fly,
                       "Has Tail": has_tail, "Aquatic": aquatic, "Breathes Fire": breathes_fire}]
        self.df = pd.DataFrame(self.stats)

    def __repr__(self):
        return str(self.df)


def combine_creature(creature1, creature2):
    # Combines 2 creature objects and returns a new Creature object with hybrid
    new_name = combine_names(creature1.name, creature2.name)
    new_weight = (creature1.weight + creature2.weight) / 2
    if creature1.num_legs > creature2.num_legs:
        new_num_legs = random.randint(creature2.num_legs, creature1.num_legs)
    else:
        new_num_legs = random.randint(creature1.num_legs, creature2.num_legs)
    new_can_fly = random.choice([creature1.can_fly, creature2.can_fly])
    new_has_tail = random.choice([creature1.has_tail, creature2.has_tail])
    new_aquatic = random.choice([creature1.aquatic, creature2.aquatic])
    new_breathes_fire = random.choice([creature1.breathes_fire, creature2.breathes_fire])

    # Returns new creature with the new stats
    return Creature(new_name, new_weight, new_num_legs, new_can_fly, new_has_tail, new_aquatic,
                    new_breathes_fire)


def combine_names(name1, name2):
    # Combines 2 names and returns a new hybrid name.
    part1, part2 = "", ""
    num_vow, num_con = 0, 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Selects part1 of the new_name
    i = 0
    while i < len(name1) - 1:
        part1 += name1[i]
        is_v = False
        for v in vowels:
            if v == name1[i]:
                is_v = True
        if is_v:
            num_vow += 1
        else:
            num_con += 1
        if (num_con > 0 and num_vow > 0) and (num_con > 1 or num_vow > 1):
            break
        i += 1

    # Selects part2 of new_name
        j = 0
        while j < len(name2) - 1:
            is_v = False
            for v in vowels:
                if v == name2[j]:
                    is_v = True
            if is_v:
                num_vow += 1
            else:
                num_con += 1
            if (num_con > 0 and num_vow > 0) and (num_con > 1 or num_vow > 1):
                break
            j += 1
        part2 = name2[j:len(name2)]

    new_name = part1 + part2
    return new_name


# Formatting to allow printing of an entire dataframe in Pycharm
pd.options.display.width = None
pd.options.display.max_columns = None
pd.set_option('display.max_rows', 42)
pd.set_option('display.max_columns', 42)

# Creatures the player will select from
lion = Creature("Lion", 240, 4, False, True, False, False)
python = Creature("Python", 30, 0, False, True, True, False)
dog = Creature("Dog", 90, 4, False, True, False, False)
human = Creature("Human", 160, 2, False, False, False, False)
trout = Creature("Trout", 3, 0, False, True, True, False)
eagle = Creature("Eagle", 10, 2, True, True, False, False)
dragon = Creature("Dragon", 2700, 4, True, True, True, True)
ant = Creature("Ant", 0.0000022046, 6, False, False, False, False)
octopus = Creature("Octopus", 80, 8, False, False, True, False)

creatures = [lion, python, dog, human, trout, eagle, dragon, ant, octopus]

GAME = True
while GAME:
    for i in range(len(creatures)):
        print(i + 1, creatures[i].name)

    choice1 = int(input("Select your first creature, 1 - " + str(len(creatures)) + ": ")) - 1
    choice2 = int(input(
        "Select your second creature, 1 - " + str(len(creatures)) + " to be combined with your first creature: ")) - 1

    hybrid = combine_creature(creatures[choice1], creatures[choice2])
    creatures.append(hybrid)
    print("**************** Creature Stats ****************")
    print("Creature Choice 1")
    print(creatures[choice1], "\n")
    print("Creature Choice 2")
    print(creatures[choice2], "\n")
    print("Hybrid of a", creatures[choice1].name, "and a", creatures[choice2].name)
    print(hybrid, "\n")
    y_n = str(input("Press y to continue or another key to exit: "))
    if y_n != "y":
        GAME = False