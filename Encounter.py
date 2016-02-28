import random 
import Character
import Enemy

possible_archetype = ["Warrior", "Mage", "Thief", "Bard", "Archer", "Pawn"]
actions = ["Attack","Magic","Ranged","Steal","Sing","Run"]

def encounter():
    decision = raw_input("How would you like to proceed ("+actions+")? ")
    if decision == 'Attack':
        #Character Strength and Endurance Rolls vs Enemy Strength and Endurance Rolls
        encounter_attack()
    elif decision == 'Magic':
        #Character Intelligence and Perception Rolls vs Enemy
        encounter_magic()
    elif decision == 'Ranged':
        #Character Perception and Endurance vs Enemy
        encounter_ranged()
    elif decision == 'Steal':
        #Character Agility and Perception vs Enemy
        encounter_steal()
    elif decision == 'Sing':
        #Character Charisma and Strength vs Enemy
        encounter_sing()
    elif decision == 'Run':
        #Luck Roll
        encounter_run()
    else: 
        #Incorrect Decision 
        print "You made an invalid choice. Try again."
        encounter()
	

def encounter_warrior():
    Enemy.create_warrior()
    encounter()
	
def encounter_mage():
    Enemy.create_mage()
    encounter()
	
def encounter_archer():
    Enemy.create_archer()
    encounter()
	
def encounter_thief():
    Enemy.create_thief()
    encounter()
	
def encounter_bard():
    Enemy.create_bard()
    encounter()
	
def encounter_pawn():
    Enemy.create_pawn()
    encounter()

def encounter_random():

def encounter_attack():
    

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
    
	
