class Character:

    #DATA
    name = "None"
    gender = "None"
    archetype = "None"
    race = "None"
    possible_attributes = ["Strength", "Perception", "Endurance", "Charisma", "Intelligence", "Agility", "Luck"]
    attributes = dict.fromkeys(possible_attributes)
    for key in attributes.keys():
        attributes[key] = 0
    #skills

    possible_races = ["Human", "Elf", "Dwarf", "Orc", "Asian"]
    possible_archetypes = ["Warrior", "Mage", "Thief", "Bard", "Jew"]
    

    #Helper
    legal_character = False

    #Methods
    def __init__(self):
        self.name = raw_input ("Name: ")
        while self.gender != "M" and self.gender != "F" and self.gender != "T":
            self.gender = raw_input ("Gender(M/F/T): ")


        while self.archetype not in self.possible_archetypes:
            print "The archetypes to choose from are:"
            for archetype in self.possible_archetypes:
                print archetype
            self.archetype = raw_input ("Archetype: ")


        while self.race not in self.possible_races:
            print "The races to choose from are:"
            for race in self.possible_races:
                print race
            self.race = raw_input ("Race: ")

        while self.legal_character == 'False':
            self.attributes = self.get_attributes()
            
            

            
        #self.skills = raw_input ("skills: ")
        

    def print_char_sheet(self):
        print("##### D&D Character Sheet #####")
        print "Name: "+self.name
        print "Gender: "+self.gender
        print "Archetype: "+self.archetype
        #print "Hair_Color: "+self.hair_color
        #print "Eye_color: "+self.eye_color
        print "Race: "+self.race
        #print "Skin_Color: "+self.skin_color
        self.print_attributes()
        #print "Skills: "+self.skills

    def get_attributes(self):
        print "Selct the value of your attributes"
        print self.attributes
        points = 30
        while points > 0 and points < 31:
            for key in self.attributes.keys():
                print "Select the value for "+key 
                key = raw_input(key + ": ")
                points = points - int(float(key))
                print "Points Remaining: "+str(points)

        if points != 0:
            print "Your attributes are invalid"
            self.get_attributes()
        else:
            self.legal_character = True

    def print_attributes(self):
        print "Attributes:\n"
        
        
        
