import random 
import Character
import Enemy

possible_archetype = ["Warrior", "Mage", "Thief", "Bard", "Archer", "Pawn"]

def encounter():
    decision = raw_input("How would you like to proceed (Attack/Magic/Ranged/Steal/Sing/Run)? ")
    if decision == 'Attack':
        
    elif decision == 'Magic':
    elif decision == 'Ranged':
    elif decision == 'Steal':
    elif decision == 'Sing':
    elif decision == 'Run':
    else: 
	

def encounter_warrior():
    Enemy.create_warrior()
	encounter()

def encounter_random():

def encounter_attack():
	decision = raw_input("How would you like to proceed (Attack/Magic/Ranged/Steal/Sing/Run)? ")
    if decision == 'Attack':
        
    elif decision == 'Magic':
    elif decision == 'Ranged':
    elif decision == 'Steal':
    elif decision == 'Sing':
    elif decision == 'Run':
    else: 

def encounter_magic():


def encounter_steal():



def encounter_sing():



def encounter_run():
    roll = random.randrange(1,10,1)
    if roll >= 6:
        print"Run Away"
        return
    else: 
        print"Can't run away!"
        encounter()
    
	
