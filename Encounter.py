import sys
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
    #Define Player Roll
    print Character.attributes
    player_attack = Character.attributes[key][0] + Character.attributes[key][1]
    player_roll = player_attack * random.randrange(1,6,1)
    
    #Define Enemy Roll
    print Enemy.attributes
    enemy_attack = Enemy.attributes[key][0] + Enemy.attributes[key][1]
    enemy_roll = enemy_attack * random.randrange(1,6,1)
    
    #Define Winner
    if player_roll > enemy_roll:
    	print "Enemy defeated"
    	return
    elif player_roll < enemy_roll:
    	print "Enemy has defeated you. Game Over."
    	sys.kill()
    elif player_roll = enemy_roll:
    	print "You were blocked. Try Again."
    	encounter()
    else:
    	print "Error with commands or inputs"
    	sys.kill()

def encounter_magic():
    #Define Player Roll
    print Character.attributes
    player_attack = Character.attributes[key][0] + Character.attributes[key][1]
    player_roll = player_attack * random.randrange(1,6,1)
    
    #Define Enemy Roll
    print Enemy.attributes
    enemy_attack = Enemy.attributes[key][0] + Enemy.attributes[key][1]
    enemy_roll = enemy_attack * random.randrange(1,6,1)
    
    #Define Winner
    if player_roll > enemy_roll:
    	print "Enemy defeated by spell."
    	return
    elif player_roll < enemy_roll:
    	print "Spell failed. Enemy defeats you. Game Over."
    	sys.kill()
    elif player_roll = enemy_roll:
    	print "Your spell was absorbed. Try Again."
    	encounter()
    else:
    	print "Error with commands or inputs"
    	sys.kill()
	
def encounter_ranged():
    #Define Player Roll
    print Character.attributes
    player_attack = Character.attributes[key][0] + Character.attributes[key][1]
    player_roll = player_attack * random.randrange(1,6,1)
    
    #Define Enemy Roll
    print Enemy.attributes
    enemy_attack = Enemy.attributes[key][0] + Enemy.attributes[key][1]
    enemy_roll = enemy_attack * random.randrange(1,6,1)
    
    #Define Winner
    if player_roll > enemy_roll:
    	print "Enemy defeated"
    	return
    elif player_roll < enemy_roll:
    	print "You were shot. Enemy wins. Game Over."
    	sys.kill()
    elif player_roll = enemy_roll:
    	print "Missed. Try Again."
    	encounter()
    else:
    	print "Error with commands or inputs"
    	sys.kill()

def encounter_steal():
    #Define Player Roll
    print Character.attributes
    player_attack = Character.attributes[key][0] + Character.attributes[key][1]
    player_roll = player_attack * random.randrange(1,6,1)
    
    #Define Enemy Roll
    print Enemy.attributes
    enemy_attack = Enemy.attributes[key][0] + Enemy.attributes[key][1]
    enemy_roll = enemy_attack * random.randrange(1,6,1)
    
    #Define Winner
    if player_roll > enemy_roll:
    	print "Succussfully stole enemy gold"
    	return
    elif player_roll < enemy_roll:
    	print "You were caught and are going to jail. Game Over."
    	sys.kill()
    elif player_roll = enemy_roll:
    	print "Unsuccessful. Try Again."
    	encounter()
    else:
    	print "Error with commands or inputs"
    	sys.kill()


def encounter_sing():
    #Define Player Roll
    print Character.attributes
    player_attack = Character.attributes[key][0] + Character.attributes[key][1]
    player_roll = player_attack * random.randrange(1,6,1)
    
    #Define Enemy Roll
    print Enemy.attributes
    enemy_attack = Enemy.attributes[key][0] + Enemy.attributes[key][1]
    enemy_roll = enemy_attack * random.randrange(1,6,1)
    
    #Define Winner
    if player_roll > enemy_roll:
    	print "Enemy fell asleep. You can escape or take advantage of him."
    	print "We won't judge."
    	choice = raw_input("What are you going to do (run away or take advantage)? ")
    	if choice.lower == 'take advantage':
    	    print "You sicko"
    	else:
    	    print "You're probably a woman anyway."
    	return
    elif player_roll < enemy_roll:
    	print "Enemy wins. Game Over."
    	sys.kill()
    elif player_roll = enemy_roll:
    	print "It's a tie. Try Again."
    	encounter()
    else:
    	print "Error with commands or inputs"
    	sys.kill()


def encounter_run():
    roll = random.randrange(1,10,1)
    if roll >= 6:
        print"Run Away"
        return
    else: 
        print"Can't run away!"
        encounter()
    
	
