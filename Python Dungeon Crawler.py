#To begin we create a class named Creature with Name, HP and Max HP characteristic attribute variables and a 
#dictionary for storing the ability variables of each creature object.These attribute variables define each 
#creature object and allow it to partake in battle. Each creature has methods for checking hp, performing an 
#attack and taking a turn, named 'check_life', 'attack' and 'turn' respectively. 
#We then create Fighter and Archer classes, which inherit from the Creature class and are constructed 
#much similarly, but each have higher attribute variables making objects of their types more 
#powerful than objects of the Creature class and have checks implemented which checks whether their attribute 
#variables have been boosted or not. As well as attack, these two additional classes have their own individual 
#methods for performing different actions. The Fighter class can implement 'shield_up' and 'shield_down', which 
#alter its stats, and the Archer class can use 'sneak_attack' which is more powerful than a normal 
#'attack'. Both classes also contain a method which loops their actions over a number of turns, in this 
#case 4, using a combination of possible actions, which is named 'turn'.

import random

class StopExecution(Exception):#additional class for smooth exit of the system. taken from https://stackoverflow.com/questions/24005221/ipython-notebook-early-exit-from-cell
    def _render_traceback_(self):
        pass

class Creature():# Creature class

    def __init__(self, name, hp=10):# Creature constructor
        self.name = name
        self.hpmax = hp
        self.hp = hp
        self.abil = {'Attack': 1, 'Defense': 5, 'Speed': 5}

    def check_life(self):# Object check life method
        if self.hp <= 0:
            self.hp = 0
        if self.hp > self.hpmax:
            self.hp = self.hpmax//1#make sure returned hp is not in decimal form
        return self.hp
        

    def attack(self, target):
        attackroll = random.randint(0, 20)
        if attackroll < (target.abil['Defense'] + target.abil['Speed']):
            print("Attack of", self.name, "was not sucessful")
        if attackroll >= (target.abil['Defense'] + target.abil['Speed']):
            damage = (random.randint(0, 4) + self.abil['Attack'])
            target.hp = target.hp - damage
            print("Sucess!", self.name, "Attack hit for", damage, "damage")
            print(target.name, "has", target.hp, "HP left.")

    def turn(self, round_num, target):
        return self.attack(target)
    
class Fighter(Creature):# Fighter Class

    def __init__(self, name, hp=50):# Fighter constructor
        self.name = name
        self.hpmax = hp
        self.hp = hp
        self.abil = {'Attack': 5, 'Defense': 10, 'Speed': 3}
        self.shieldup = False #boolean value to check if the shield is up currently
    
    def shield_up(self): #method which raises the 'Defense' ability and lowers the 'Attack' ability. 
        if self.shieldup == False:
            self.abil['Attack'] = (self.abil['Attack'] -5)
            self.abil['Defense'] = (self.abil['Defense'] +5)
            self.shieldup = True
            print(self.name, "has optimized shields")
    
    def shield_down(self): #method which raises the 'Attack' ability and lowers the 'Defense' ability.
        if self.shieldup == False:
            pass
        if self.shieldup == True:
            self.abil['Attack'] = (self.abil['Attack'] +5)
            self.abil['Defense'] = (self.abil['Defense'] -5)
            self.shieldup = False
            print(self.name, "has optimized main cannon")


    def turn(self, round_num, target):#method which checks the current rount number and performs a loop of actions accordingly
        if round_num % 4 == 1:
            self.attack(target)
            self.shield_up()
        if round_num % 4 == 2:
            self.attack(target)
        if round_num % 4 == 3:
            self.attack(target)
        if round_num % 4 == 0:
            self.attack(target)
            self.shield_down()


class Archer(Creature):# Archer class

    def __init__(self, name, hp=30):# Archer constructor
            self.name = name
            self.hpmax = hp
            self.hp = hp
            self.abil = {'Attack': 7, 'Defense': 8, 'Speed': 8}
            self.abil2 = {'Attack': 7, 'Defense': 8, 'Speed': 8} #second set of ability variables for actual abilit variable to be checked against
            self.modified = False #check to see if the current have been modified
    
    def sneak_attack(self, target):# Archer Sneak Attack turn method
        sneakroll = max((random.randint(1, 20)), (random.randint(1, 20)))
        if self.abil["Speed"] > target.abil["Speed"]:
            sneakroll += (self.abil["Speed"] - target.abil["Speed"])
        if self.abil == self.abil2:
            self.abil['Attack'] = (self.abil['Attack'] +3)
            self.abil['Defense'] = (self.abil['Defense'] -3)
        if sneakroll < (target.abil['Defense'] + target.abil['Speed']):
            print("Attack of", self.name, "was not sucessful")
        if sneakroll >= (target.abil['Defense'] + target.abil['Speed']):
            damage = (random.randint(0, 8) + self.abil['Attack'])
            target.hp = target.hp - damage
            print("Sucess!", self.name, "Sneak attack hit for", damage, "damage")
            print(target.name, "has", target.hp, "HP left.")
        self.abil['Attack'] = (self.abil['Attack'] -3)
        self.abil['Defense'] = (self.abil['Defense'] +3)

    def turn(self, round_num, target):# Archer turn method
        if round_num % 4 == 1:
            self.attack(target)
        if round_num % 4 == 2:
            self.sneak_attack(target)
        if round_num % 4 == 3:
            self.sneak_attack(target)
        if round_num % 4 == 0:
            self.sneak_attack(target)

#We must then create classes named Goblin and Orc with Name, HP and Max HP characteristic attribute variables 
#and a dictionary for storing the ability variables of each object of the class. The Goblin and Orc classes 
#inherit their methods from the Creature class, and the class Orc also has access to the 'heavy_attack' 
#method, which is a more powerful version of attack that modifies the users 'attack' and 'defense' 
#attribute values. The orc class uses a 'turn' method similar to those used by the Fighter and Archer 
#classes. We then create the OrcGeneral class. This class inherits from the Orc and Fighter classes and 
#is constructed in the same fashion. The Orc General class uses its own version of the 'turn' method 
#similar to those used by the 'Orc'. The third task has asked us to create to create the GoblinKing class. 
#This class inherits from the Goblin and Archer classes and is constructed in the same fashion. 
#The Orc General class uses its own version of the 'turn' method similar to those used by the 'Archer'.

class Goblin(Creature):# Goblin class

    def __init__(self, name, hp=15):# Goblin constructor
            self.name = name
            self.hpmax = hp
            self.hp = hp
            self.abil = {'Attack': 4, 'Defense': 6, 'Speed': 6}

class Orc(Creature):# Orc Class

    def __init__(self, name, hp=50):# Orc constructor
            self.name = name
            self.hpmax = hp
            self.hp = hp
            self.abil = {'Attack': 10, 'Defense': 6, 'Speed': 2}
            self.abil2 = {'Attack': 10, 'Defense': 6, 'Speed': 2}
            self.modified = False

    def heavy_attack(self, target):
        if self.abil == self.abil2:#check to see the current stats against the base stats
            self.abil['Attack'] = (self.abil['Attack'] +5)
            self.abil['Defense'] = (self.abil['Defense'] -3)
        attackroll = random.randint(1, 20)
        if attackroll < (target.abil['Defense'] + target.abil['Speed']):
            print("Heavy attack of", self.name, "was not sucessful")
        if attackroll >= (target.abil['Defense'] + target.abil['Speed']):
            damage = (random.randint(0, 8) + self.abil['Attack'])
            target.hp = target.hp - damage
            print("Sucess!", self.name, "Heavy attack hit for", damage, "damage")
            print(target.name, "has", target.hp, "HP left.")
        self.abil['Attack'] = (self.abil['Attack'] -5)
        self.abil['Defense'] = (self.abil['Defense'] +3)

    def turn(self, round_num, target):# Orc turn method
        if round_num % 4 == 1:
            self.attack(target)
        if round_num % 4 == 2:
            self.attack(target)
        if round_num % 4 == 3:
            self.attack(target)
        if round_num % 4 == 0:
            self.heavy_attack(target)


class OrcGeneral(Orc, Fighter):# OrcGeneral class

    def __init__(self, name, hp=100):# OrcGeneral constructor
            self.name = name
            self.hpmax = hp
            self.hp = hp
            self.abil = {'Attack': 10, 'Defense': 6, 'Speed': 2}
            self.abil2 = {'Attack': 10, 'Defense': 6, 'Speed': 2}
            self.shieldup = False

    def turn(self, round_num, target):# OrcGeneral turn method
        if round_num % 4 == 1:
            self.attack(target)
            self.shield_up()
        if round_num % 4 == 2:
            self.attack(target)
        if round_num % 4 == 3:
            self.shield_down()
            self.attack(target)
        if round_num % 4 == 0:
            self.heavy_attack(target)

class GoblinKing(Goblin, Archer):# GoblinKing class

    def __init__(self, name, hp=50):# GoblinKing constructor
            self.name = name
            self.hpmax = hp
            self.hp = hp
            self.abil = {'Attack': 7, 'Defense': 8, 'Speed': 8}
            self.abil2 = {'Attack': 7, 'Defense': 8, 'Speed': 8}
            self.modified = False

    def turn(self, round_num, target):# GoblinKing turn method
        if round_num % 4 == 1:
            self.attack(target)
        if round_num % 4 == 2:
            self.sneak_attack(target)
        if round_num % 4 == 3:
            self.sneak_attack(target)
        if round_num % 4 == 0:
            self.sneak_attack(target)

#The next step is to create the Wizard class with Name, HP and Max HP characteristic attribute variables 
#and a dictionary for storing the ability variables of each Wizard object. The wizard class also implements 
#a mana variable in the constructor, which determines how many mana dependant actions the wizard can perform. 
#The second task has asked us to create a number of methods for the wizard to use which can either damage or 
#heal other objects in the game. These methods are titled 'attack', 'recharge', 'fire_bolt', 'heal', 
#'mass_heal' and 'fire_storm', and most of them require the use of mana to perform, and performing one 
#that requires mana will deplete a Wizard objects mana accordingly.

class Wizard(Creature):# Wizard class

    def __init__(self, name, hp=20):# Wizard constructor
        self.name = name
        self.hpmax = hp
        self.hp = hp
        self.abil = {'Attack': 3, 'Defense': 5, 'Speed': 5, 'Arcana': 10}
        self.mana = 100


    def mana_check(self):# Wizards mana check method
        if self.mana > 100:
            self.mana = 100
        if self.mana < 0:
            self.mana = 0

    def attack(self, target):# Wizards attack method
        self.mana += 20
        self.mana_check()
        attackroll = random.randint(0, 20)
        if attackroll < (target.abil['Defense'] + target.abil['Speed']):
            print("Attack of", self.name, "was not sucessful")
        if attackroll >= (target.abil['Defense'] + target.abil['Speed']):
            damage = (random.randint(0, 4) + self.abil['Attack'])
            target.hp = target.hp - damage
            print("Sucess!", self.name, "Attack hit for", damage, "damage")
            print(target.name, "has", target.hp, "HP left.")
        print("20% Charge Restored")

    def recharge(self):# recharge spell method
        self.mana += 30
        print("30% Charge Restored")
        self.mana_check

    def fire_bolt(self, target):# fire bolt attack method
        self.mana_check
        attackroll = (random.randint(0, 20) + (self.abil['Arcana']//2)) 
        if attackroll < (target.abil['Defense'] + target.abil['Speed']):
            print("Attack of", self.name, "was not sucessful")
        if attackroll >= (target.abil['Defense'] + target.abil['Speed']):
            damage = (random.randint(0, self.abil['Arcana']))
            target.hp = target.hp - damage
            self.mana += 10
            self.mana_check()
            print("Sucess!", self.name, "Firebolt hit for", damage, "damage.", self.name, "is gettng all fired up!")
            print("10% Charge Restored")
            print(target.name, "has", target.hp, "HP left.")

    def heal(self, target):# heal spell method
        self.mana_check()
        if self.mana < 20:
            print('You do not have enough charge for Heal.')
        if self.mana >= 30:
            self.mana -= 30
            healing = (random.randint(0, 8) + (self.abil['Arcana'] // 2))
            target.hp += healing
            self.check_life()
            print("Healing sucess!", self.name, "has healed", target.name, "for", healing, "points.")
            if self.hp > self.hpmax:
                self.hp = self.hpmax
    
    def mass_heal(self, allies):# mass heal spell method
        self.mana_check()
        if self.mana < 30:
            print('You do not have enough charge for Mass Heal.')
            return None
        if self.mana >= 30:
            self.mana -= 30
            healing = (random.randint(0, 10) + (self.abil['Arcana'] // 2))
            self.hp += healing
            for i in allies:
                i.hp += healing
                i.check_life()
                print("Healing sucess!", i.name, "has been healed for", healing, "points.")

    def fire_storm(self, enemies):# fire storm spell method
        self.mana_check()
        self.enemies = enemies
        if self.mana < 50:
            print('You do not have enough charge for Fire Storm.')
            return None
        if self.mana >= 50:
            self.mana -= 50
            attackroll = (random.randint(1, 20) + self.abil['Speed'])
            firedamage = (random.randint(5, 20) + self.abil['Arcana'])
            if attackroll <= (self.abil['Arcana']):
                for i in self.enemies:
                    i.hp -= (firedamage //2)
                    print("Sucess! A weak Fire Storm has hit", i.name, "for", (firedamage//2), "damage.")
            else:
                for i in self.enemies:
                    i.hp -= firedamage
                    print("Sucess! A powerfull Fire Storm has hit", i.name, "for", firedamage, "damage.")


#The final step is to create a Battle class and its constructor. Inside the constructor, we have variables 
#for creating a list of enemies and allies, as well as a variable which is creates an object of the Wizard 
#class, to act as the player character. We must also create the methods 'auto_select' and 'select_target', 
#which will be used by objects to select targets for their attacks. The methods check which team an object is in and 
#assign its target_list accordingly. The 'select_target' method is used by the player and prints out information 
#regarding the other objects participating in the instance of Battle. We then must implement a 'start' method. 
#This method defines which object is to take it's turn first by creating a list of all objects 
#participating in the battle instance and organizing it according to their ability speed variable. The method also 
#executes each round of the battle, printing messages stating which round it is. The method also makes each object 
#take it's turn and perform its correct action determined by the round number. The players Wizard object also takes 
#its turn in the same fashion. This method also checks for objects whos hp has dropped below 0 and removes any it finds, 
#printing a message when it does so. The method also concludes the game if ether team loses all their members. 
#Finally, we must create the 'player_turn' method. This method is used to create the players turn and displays information 
#on the possible targets, including their name and hp/maxhp values. Once a target is selected, it then prints out the 
#possible actions that the player can perform. The method also includes an option to quit the game, which terminates the program.

class Battle():# the Battle class

    def __init__(self, enemies, allies):# the battle class constructor
        self.lenemies = []
        self.lallies = []
        self.goodbye = str("///////////////////////////////////////////\n///////////////////////////////////////////\n/////////////////GAME OVER/////////////////\n///////////////////////////////////////////\n///////////////////////////////////////////")
        for i in enemies:
            self.lenemies.append(i)
        for i in allies:
            self.lallies.append(i)
        print("///////////////////////////////////////////")
        player = input("DIGIDESTINED, WHAT IS YOUR NAME?? ")
        self.wiz = Wizard(player)
        self.lallies.append(self.wiz)
        print("/////////// LET THE BATTLE BEGIN ///////////")
        
    def auto_select(self, target_list):# method for giving non player objects a target list
        target = random.choice(target_list)
        if target.check_life() > 0:
            return target
        if target.check_life() <= 0:
            return None 

    def select_target(self, target_list):# a method for player target selection
        index = 1
        targets = []
        print("It's your turn, chose who you want to attack \n")
        for mob in target_list:# prints possible targets and information related to them
            print("|||\t", index, mob.name, '\tHP:', mob.hp, "/", mob.hpmax, end='\t\t|||\n')
            targets.append(mob)
            index += 1
        while True:# error checking for user input
            try:
                choice = int(input("Your choice: "))
                break
            except ValueError:
                print("Pick a target number please please.")
        target = targets[(choice)-1]
        return target

    def start(self):# the main loop for which performs the 'Battle'
        round_num = 1
        self.turn = []
        for x in self.lenemies:
             self.turn.append(x)
        for y in self.lallies:
             self.turn.append(y)
        self.turn.sort(key=lambda x: x.abil['Speed'], reverse=True)# lambda function to sort list objects by their .abil['Speed'] value
        while True:
            print("\n///////////////////////////////////////////")
            print ("/////////////// Round ", round_num, ": ///////////////")
            print("/////////////////////////////////////////\n")
            for t in self.turn:#checks to see which object gets to take a turn first
                self.deadlist = []
                for c in self.turn:#removes objects with hp <=0
                    if c.check_life() <= 0:
                        print (c.name, "Has fainted")
                        self.deadlist.append(c)
                        self.turn.remove(c)
                    for e in self.lenemies:
                        if e.hp <= 0:
                            self.deadlist.append(e)
                            self.lenemies.remove(e)
                        if len(self.lenemies) == 0:
                            print ("All the enemies have been defeated!")
                            print (self.goodbye)
                            raise StopExecution
                    for a in self.lallies:
                        if a.hp <= 0:
                            self.deadlist.append(a)
                            self.lallies.remove(a)
                        if len(self.lallies) == 0:
                            print ("All the allies have been defeated! :( ")
                            print (self.goodbye)
                            raise StopExecution
                if self.wiz in self.deadlist: # check which stops player from being able to a make move after dying.
                    break
                if t == self.wiz:# creating a target list for an object
                    target = self.select_target(self.lenemies + self.lallies)
                    self.player_turn(target)
                if t in self.lenemies:
                    target_list = self.lallies
                if t in self.lallies:
                    target_list = self.lenemies
                if t in self.deadlist:# if object with hp <= 0 is picked up by accident, it's turn is missed.
                    break
                target = self.auto_select(target_list)
                if t != self.wiz:# non player objects to take their turn
                    t.turn(round_num, target)
            for c in self.turn: # second check to avoid getting fainted messages after round start text
                self.deadlist = []
                if c.check_life() <= 0:
                    print (c.name, "Has fainted")
                    self.deadlist.append(c)
                    self.turn.remove(c)
                for e in self.lenemies:
                    if e.hp <= 0:
                        self.deadlist.append(e)
                        self.lenemies.remove(e)
                    if len(self.lenemies) == 0:
                        print ("All the enemies have been defeated!")
                        print (self.goodbye)
                        raise StopExecution
                for a in self.lallies:
                    if a.hp <= 0:
                        self.deadlist.append(a)
                        self.lallies.remove(a)
                    if len(self.lallies) == 0:
                        print ("All the allies have been defeated! :( ")
                        print (self.goodbye)
                        raise StopExecution
            round_num += 1


    def player_turn(self, target):#Method for players turn
        attempts = 0
        self.target = target
        print ("Chose an attack:")
        attacks = {'1.Attack | 2.Recharge | 3.Firebolt | 4.Heal | 5.Mass Heal | 6.Fire Storm | 7.Endgame'}
        print("CHARGE: ", self.wiz.mana, "% ////////////////////////////////")
        print ('|1.Attack | 2.Recharge | 3.Firebolt | 4.Heal | \n | 5.Mass Heal |  6.Fire Storm  | 7.Endgame |')
        print("///////////////////////////////////////////////")
        while True:# error checking for user input
            try:
                choice = int(input("Your choice: "))
                break
            except ValueError:
                print("Pick a number please please.")
        while choice < 8:
            while attempts < 1:
                for i in attacks:
                    if choice == 1:
                        self.wiz.attack(target)
                        attempts += 1
                        return
                    if choice == 2:
                        self.wiz.recharge()
                        attempts += 1
                        return
                    if choice == 3:
                        self.wiz.fire_bolt(target)
                        attempts += 1
                        return
                    if choice == 4:
                        self.wiz.heal(target)
                        attempts += 1
                        return
                    if choice == 5:
                        self.wiz.mass_heal(self.lallies)
                        return
                    if choice == 6:
                        self.wiz.fire_storm(self.lenemies)
                        return
                    if choice == 7:
                        print(self.goodbye)
                        raise StopExecution

Agumon = Creature('Agumon')#creating the mobs to be used in Battle
Gabumon = Creature('Gabumon')
Greymon = Fighter('Greymon')
Angelmon = Archer('Agelmon')
Gatumon = Goblin('Gatumon')
Myotismon = Orc('Myotismon')
Devimon = OrcGeneral("Devimon")
Impmon = GoblinKing("Impmon")

enemies = (Gatumon, Myotismon, Devimon, Impmon)#making battle parties
allies = (Greymon, Angelmon)

Battle2 = Battle(enemies, allies)#creating Battle class objects with party list inputs

Battle2.start()#initiating the main loop of the Battle class 'start' method