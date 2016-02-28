import random

possible_attributes = ["Strength", "Perception", "Endurance", "Charisma", "Intelligence", "Agility", "Luck"]
attributes = dict.fromkeys(possible_attributes)
for key in attributes.keys():
    attributes[key] = 0
archetype = 'none'
possible_archetype = ["Warrior", "Mage", "Thief", "Bard", "Archer", "Pawn"]	

def random_stats():
    points_remaining = 30
    for key in attributes.keys():
        attributes[key] = random.randrange(1,10,1)
        points_remaining = points_remaining - int(attributes[key])
    if points_remaining == '0':
        return
    else:
        attributes[key] = attributes[key] + points_remaining
	
def create_warrior():
    for key in attributes.keys():
        if key == "Strength":
            attributes[key] = random.randrange(5,7,1)
        elif key == "Endurance":
            attributes[key] = random.randrange(5,7,1)
        else:
            attributes[key] = random.randrange(2,4,1)
    print "Encountered a Warrior"

def create_mage():
    for key in attributes.keys():
        if key == "Intelligence":
            attributes[key] = random.randrange(5,7,1)
        elif key == "Perception":
            attributes[key] = random.randrange(5,7,1)
        else:
            attributes[key] = random.randrange(2,4,1)
    print "Encountered a Mage"

def create_archer():
    for key in attributes.keys():
        if key == "Perception":
            attributes[key] = random.randrange(5,7,1)
        elif key == "Endurance":
            attributes[key] = random.randrange(5,7,1)
        else:
            attributes[key] = random.randrange(2,4,1)
    print "Encountered an Archer"

def create_thief():
    for key in attributes.keys():
        if key == "Agility":
            attributes[key] = random.randrange(5,7,1)
        elif key == "Perception":
            attributes[key] = random.randrange(5,7,1)
        else:
            attributes[key] = random.randrange(2,4,1)
    print "Encountered a Thief"

def create_bard():
    for key in attributes.keys():
        if key == "Charisma":
            attributes[key] = random.randrange(5,7,1)
        elif key == "Intelligence":
            attributes[key] = random.randrange(5,7,1)
        else:
            attributes[key] = random.randrange(2,4,1)
    print "Encountered a Bard"

def create_pawn():
    points_remaining = 20
    for key in attributes.keys():
        attributes[key] = random.randrange(3,4,1)
        points_remaining = points_remaining - int(attributes[key])
    if points_remaining == '0':
        return
    else:
        attributes[key] = attributes[key] + points_remaining
    print "Encountered a Pawn"

