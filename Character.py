class Character:

    #DATA
    name = "None"
    gender = "None"
    archetype = "None"
    race = "None"
    possible_gender = ["M","F","T"]
    possible_attributes = ["Strength", "Perception", "Endurance", "Charisma", "Intelligence", "Agility", "Luck"]
    attributes = dict.fromkeys(possible_attributes)
    for key in attributes.keys():
        attributes[key] = 0
    #skills

    possible_races = ["Human", "Elf", "Dwarf", "Orc", "Cyborg"]
    possible_archetypes = ["Warrior", "Mage", "Thief", "Bard", "Archer"]
    

    #Helper
    legal_character = False

    #Methods
    def __init__(self):
        self.name = raw_input ("Name: ")
        areyousure = raw_input ("Are you sure? (Y/N) ")
        if areyousure == 'Y':
            print "Ok, I'll call you "+ self.name
        else:
		    #Decide on a Name for Your Character 
            self.name = raw_input("Name: ")
            areyousure = raw_input("Are you sure? (Y/N) ")
            if areyousure == 'Y':
                print "Ok, I'll call you "+ self.name
            else:
                print "You failed to make a decision. I'll call you Hero"
                self.name = 'Hero'
		
		#Decide on the Gender of Your Character
        while self.gender != "M" and self.gender != "F" and self.gender != "T":
            self.gender = raw_input ("Gender(M/F/T): ")

		#Decide on What Type of Character You Want to Be
        while self.archetype not in self.possible_archetypes:
            print "The archetypes to choose from are:"
            for archetype in self.possible_archetypes:
                print archetype
            self.archetype = raw_input ("Archetype: ")

		#Decide on Which Race You Want Your Character to Be 
        while self.race not in self.possible_races:
            print "The races to choose from are:"
            for race in self.possible_races:
                print race
            self.race = raw_input ("Race: ")

		#Initiate the Attribute Selection 
        if self.legal_character == False:
            self.attributes = self.get_attributes()
        else: 
            print self.legal_character
            print "something is wrong"


    def print_char_sheet(self):
        print '\n'
        print '\n'
        print("########## D&D Character Sheet ##########")
        print "Name: "+self.name
        print "Gender: "+self.gender
        print "Archetype: "+self.archetype
        print "Race: "+self.race
        self.print_attributes()

    def get_attributes(self):
        print "Selct the value of your attributes"
        print self.attributes
        points = 30
        print "Points Remaining: "+str(points)
        while points > 0 and points < 31:
            for key in self.attributes.keys():
                print "Select the value for "+key 
                value = raw_input(key + ": ")
                if value == '':
                    value = '0'
                points = points - int(float(value))
                self.attributes[key] = value
                print "Points Remaining: "+str(points)

		#Re-do Point Selection for Invalid Character 
        if points != 0:
            print "\n"
            print "Your attributes are invalid"
            for key in self.attributes:
                key = 0
            self.get_attributes()
			
		#Character is valid
        else:
            self.legal_character = True
            return self.attributes         

	#Prints the Attributes in a List Form (Similar to a Stats Screen for Video Games)
    def print_attributes(self):
        print "Attributes:"
        for key in self.attributes:
            print str(key) + ": " + str(self.attributes[key])
        
    
	#Create a Random NPC
    def random_npc(self):
        import random 
        self.name = 'Random NPC'
        self.gender = self.possible_gender[random.randrange(0,3,1)]
        self.race = self.possible_races[random.randrange(0,5,1)]
        self.archetype = self.possible_archetypes[random.randrange(0,5,1)]
        self.random_attributes()
        self.print_char_sheet()
		
    #Generate Random Attributes for Random NPC 
    def random_attributes(self):
        import random 
        points = 30
        for key in self.attributes:
            value = random.randrange(3,6,1)
            self.attributes[key] = value 
            points = points - int(float(value))
			
        if points < 0:
            self.random_attributes()
			
        else: 
            pass 
		
    def level_up(self):
        import random
        favored_skill = []
        if self.archetype == 'Warrior':
            self.favored_skill = ['Strength','Endurance']
        elif self.archetype == 'Mage':
            self.favored_skill = ['Perception','Intelligence']
        elif self.archetype == 'Archer':
            self.favored_skill = ['Perception','Agility']
        elif self.archetype == 'Thief':
            self.favored_skill = ['Agility','Endurance']
        elif self.archetype == 'Bard':
            self.favored_skill = ['Charisma','Strength']
        for key in self.attributes:
            if key in self.favored_skill:
                value = random.randrange(2,5,1)
                self.attributes[key] = int(float(self.attributes[key])) + int(value)
            elif key not in self.favored_skill:
                value = random.randrange(0,3,1)
                self.attributes[key] = int(float(self.attributes[key])) +int(value)
	    else:
                print "I'm not sure if you're doing this right"
        self.print_char_sheet()
        
        
