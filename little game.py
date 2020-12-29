#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 09:53:41 2020

@author: ziranxu
"""
import random

class person:
    def __init__(self,name,blood):
        self.name = name
        self.blood = blood

class scene:
   def __init__(self,color):
       print("This is a {} color room".format(color))
       if color =="red":
           self.number = 3
           print("There are {} normal anemies".format(self.number))
       elif color == "green":
           self.number = 1
           print("There are {} normal anemy".format(self.number))
       else:
        self.number = 2
        print("There are {} normal anemies".format(self.number))
       self.cost = 10*self.number

class bridge(scene):
    def __init__(self,color):
        super().__init__(color)
    def mission(self):
        print("You put the boom and broke the bridge. Go to find the  Escape Pod")
class Escape_Pod(scene):
    def __init__(self):
        pass
    def escape(self):
        print("You arrived Escape Pod and escaped. You win the game!")
class Laser_Weapon_Armory(scene):
    def __init__(self):
        print("Here is Laser Weapon Armory.")
        print("You need to gess the final number from 0~100 to stop the boom.")
        print("You have five chances.")
    def game(self):
        st = stats()
        x = st.game()
        return x

class stats:
    def __init__(self):
        pass
    def randcol(self):
        return random.choice(["red","yellow","green"])
    def fight(self,scene):
        hero.blood -= scene.cost
    def game(self):
        n = random.randint(0,100)
        i = 5
        while i >0:
            x = int(input("input your number:"))
            if x > n:
                print("Larger than the number")
            elif x<n:
                print("Smaller than the number")
            elif x ==n:
                break
            i-=1
        return i

hero = person("Joker",100)
st = stats()
print("Game Begin! You are a hero has 100 blood now")
Central_Corridor = scene(st.randcol())
st.fight(Central_Corridor)
print("At the beginning, you arrived the contral corridor and your blood now is {} after the fight".format(hero.blood))
weapon_exist = True
bridge_exist = True
while True and hero.blood > 0 :
    
    if hero.blood == 0:
        print("Hero dead.Game Over")
        break
    else:
        print("You have three choices: ")
        print("\t1. Go ahead\n\t2. Go right\n\t3. Go left")
        step = input("> ")
        if step == "3" and weapon_exist:
            lwa = Laser_Weapon_Armory()
            x = lwa.game()
            if x ==0:
                print("You dead.Game Over")
                break
            else:
                print("You finished your mission. Congrets! Try to find the bridge")
                weapon_exist = False
        elif step == "1" and not weapon_exist:
            ep = Escape_Pod()
            ep.escape()
            break
        elif step == "2" and bridge_exist:
            print("You are on the bridge")
            Gothon = person("Gothon",60)
            hero.blood -= Gothon.blood
            if hero.blood <=0:
                print("You dead. Game Over")
                break
            else:
                b = bridge(st.randcol)
                b.mission()
                bridge_exist = False
        else:
            room = scene(st.randcol())
            st.fight(room)
        print("you have {} blood now".format(hero.blood))
