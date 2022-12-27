import random
import time

from pandas import test

testing=True
testclass=1
testround=4


playerclasses=[
    {"name":"Warrior","hp":30,"atk":6,"df":2,"moves":["Attack","Recharge","Heavy Swing","Bulk Up"]},
    {"name":"Mage","hp":20,"atk":8,"df":1,"moves":["Attack","Recharge","Energy Drain","Channel Power"]},
    {"name":"Rogue","hp":25,"atk":7,"df":1,"moves":["Attack","Recharge","Targeted Stab","Piercing Wounds"]},
]
specialmoves=[
    "Burning Blade","Explosion","1000 Knives"
]
idx=0
player=None

#Project will only involve the first three enemies
#On my own I will set up the next three
enemies=[
    {"name":"Skull Conscript","hp":25,"atk":5,"df":2,"moves":["Wild Stab","Battle Cry"]},
    {"name":"Skeleton Mage","hp":15,"atk":4,"df":1,"moves":["Fireball","Recover"]},
    {"name":"The Fallen Knight","hp":30,"atk":7,"df":2,"moves":["Heavy Swing","Draining Punch","Energy Drain","Chaos Blade"]},
    {"name":"Praetorian Undead","hp":35,"atk":8,"df":5,"moves":["Heavy Swing","Targeted Stab","Stab and Slash"]},
    {"name":"The Necromancer?","hp":55,"atk":8,"df":3,"moves":["Energy Drain","Mana Drain","Chaos Blade"]},
    {"name":"Dracolich","hp":70,"atk":10,"df":0,"moves":["Intimidating Roar","Crunch","Shadowflame"]},
    {"name":"The Necromancer","hp":70,"atk":10,"df":3,"moves":["Energy Drain+","Mana Drain+","Chaos Blade+","Final Destination"]},
]
#Probabilities that enemy uses certain attacks
enemyweights=[
    [10,60,30],
    [10,70,20],
    [10,20,20,20,30],
    [10,30,30,40],
    [10,20,40,30],
    [10,30,30,20,10]
]

for i in range(len(enemyweights)):
    enemies[i]["weights"]=enemyweights[i]
for i in range(len(enemies)):
    enemies[i]["moves"]=["Attack"]+enemies[i]["moves"]

enemyon=0

class Entity:
    def __init__(self,name,hp,atk,df,moves) -> None:
        self.name=name
        self.hp=hp
        self.maxhp=hp
        self.atk=atk
        self.maxatk=atk
        self.df=df
        self.maxdf=df
        self.moves=moves
    def __str__(self) -> str:
        res=self.name+"\n"
        res+="HP:"+str(self.hp)+"/"+str(self.maxhp)+"\n"
        res+="ATK:"+str(self.atk)+"\n"
        res+="DEF:"+str(self.df)+"\n"
        return res

class Enemy(Entity):
    def __init__(self,name,hp,atk,df,moves,weights) -> None:
        super().__init__(name,hp,atk,df,moves)
        self.weights=weights
    def __str__(self) -> str:
        res=self.name+"\n"
        res+="HP:"+str(self.hp)+"/"+str(self.maxhp)+"\n"
        res+="ATK:"+str(self.atk)+"\n"
        res+="DEF:"+str(self.df)+"\n"
        res+="Moves\n"
        for i in range(len(self.moves)):
            res+=self.moves[i]
            if(i<len(self.moves)-1):
                res+=", "
        res+="\n"
        return res


class Player(Entity):
    def __init__(self,name,hp,atk,df,moves) -> None:
        self.mana=3
        self.maxmana=self.mana
        self.level=0
        super().__init__(name,hp,atk,df,moves)
    def __str__(self) -> str:
        res=self.name+"\n"
        res+="HP:"+str(self.hp)+"/"+str(self.maxhp)+"\n"
        res+="ATK:"+str(self.atk)+"\n"
        res+="DEF:"+str(self.df)+"\n"
        res+="MANA:"+str(self.mana)
        return res
    def resetstats(self):
        self.hp=self.maxhp
        self.atk=self.maxatk
        self.df=self.maxdf
        self.mana=self.maxmana
    def levelup(self):
        self.level+=1
        
        self.maxhp+=4
        self.maxatk+=1
        self.atk=player.maxatk
        self.hp=player.maxhp
        if(self.level==2 or self.level==4):
            self.maxdf+=1
            self.df=self.maxdf
        if(self.level==3):
            self.moves.append(specialmoves[idx])
        
        #Upgrade move
        if(self.level==2 or self.level==5):
            if(testing):
                    movetoupgrade=random.randint(0,3)
                    while("+" in player.moves[movetoupgrade]):
                        movetoupgrade=random.randint(0,3)
                    print("Done")
            else:
                valid=False
                while(not valid):
                    print("Upgrade")
                    for i in range(4):
                        print("Select",i,"to upgrade",player.moves[i])
                    movetoupgrade=input()
                    if(movetoupgrade>=0 and movetoupgrade<=3 and "+" not in player.moves[movetoupgrade]):
                        valid=True
            
            player.moves[movetoupgrade]=player.moves[movetoupgrade]+"+"
                        

def handlemoves():
    '''
    Heavy Swing-Hit Hard
    Bulk Up-Increase atk and df
    Energy Drain-Heal and deal damage
    Flare-Deal massive damage, but lower your own stats
    Targeted Stab- Lower enemey atk and df
    Piercing Wound- Ignore enemy df
    '''

def handleplayermove():
    global player
    global enemy
    damage=0

    print("Player select a move")
    for i in range(len(player.moves)):
        print(i,player.moves[i])
    
    validmove=False
    while(not validmove):
        movenum=int(input(""))
        if(movenum==0):
            validmove=True
            if(player.mana<player.maxmana):
                player.mana+=1
        if(movenum==1):
            validmove=True

        elif(movenum>1 and player.mana>0):
            validmove=True
            if(movenum>3):
                player.mana-=2
            else:
                player.mana-=1
        else:
            print("Not enough mana")


    playermove=player.moves[movenum]
    print("\n\n\n")
    resulttext=""
    if(playermove=="Attack"):
        damage=player.atk-enemy.df
        resulttext+=enemy.name+" took "+str(damage)+" damage.\n"
    elif(playermove=="Attack+"):
        damage=player.atk-enemy.df
        player.atk+=1
        player.df+=1
        resulttext+=enemy.name+" took "+str(damage)+" damage.\n"
        resulttext+=player.name+" gained 1 ATK and 1 DEF.\n"
    elif(playermove=="Recharge"):
        player.mana=player.mana+2
        player.mana=min(player.mana,player.maxmana)
        resulttext+=player.name+" recovered 2 mana"
    elif(playermove=="Recharge+"):
        player.mana=player.mana+2
        player.mana=min(player.mana,player.maxmana)
        player.hp+=8
        resulttext+=player.name+" recovered 2 mana and gained 8 HP"

    elif(playermove=="Heavy Swing"):
        damage=int(1.5*player.atk-enemy.df)
        resulttext+=enemy.name+" took "+str(damage)+" damage."
    elif(playermove=="Heavy Swing+"):
        damage=int(1.75*player.atk-enemy.df)
        resulttext+=enemy.name+" took "+str(damage)+" damage."
    elif(playermove=="Bulk Up"):
        player.atk+=2
        player.df+=2
        resulttext+=player.name+" gained 2 ATK and 2 DEF."
    elif(playermove=="Bulk Up+"):
        player.atk+=3
        player.df+=3
        resulttext+=player.name+" gained 3 ATK and 3 DEF."
    elif(playermove=="Burning Blade"):
        damage=int(1.5*player.atk-enemy.df)
        enemy.df-=3
        resulttext+=enemy.name+" took "+str(damage)+" damage.\n"
        resulttext+=enemy.name+" lost 3 DEF"
    
    elif(playermove=="Energy Drain"):
        damage=int(player.atk-enemy.df)
        healamount=min(damage,player.maxhp-player.hp)
        player.hp+=healamount
        resulttext+=enemy.name+" took "+str(damage)+" damage.\n"
        resulttext+=player.name+" healed "+str(healamount)+" health"
    elif(playermove=="Energy Drain+"):
        damage=int(1.5*player.atk-enemy.df)
        healamount=min(damage,player.maxhp-player.hp)
        player.hp+=healamount
        resulttext+=enemy.name+" took "+str(damage)+" damage.\n"
        resulttext+=player.name+" healed "+str(healamount)+" health"
    elif(playermove=="Channel Power"):
        player.atk+=3
        resulttext+=player.name+" gained 3 ATK."
    elif(playermove=="Channel Power+"):
        player.atk+=5
        resulttext+=player.name+" gained 5 ATK."
    elif(playermove=="Explosion"):
        damage=int(2*player.atk)
        player.atk-=2
        player.df-=2
        resulttext+=enemy.name+" took "+str(damage)+" damage.\n"
        resulttext+=player.name+" lost 2 ATK and 2 DEF"
    
    elif(playermove=="Targeted Stab"):
        damage=int(0.75*player.atk-enemy.df)
        enemy.df-=1
        resulttext+=enemy.name+" took "+str(damage)+" damage.\n"
        resulttext+=enemy.name+" lost 1 DEF."
    elif(playermove=="Targeted Stab"):
        damage=int(player.atk-enemy.df)
        enemy.df-=2
        resulttext+=enemy.name+" took "+str(damage)+" damage.\n"
        resulttext+=enemy.name+" lost 2 DEF."
    elif(playermove=="Piercing Wound"):
        damage=player.atk
        resulttext+=enemy.name+" took "+str(damage)+" damage.\n"
    elif(playermove=="Piercing Wound+"):
        damage=int(1.5*player.atk)
        resulttext+=enemy.name+" took "+str(damage)+" damage.\n"
    elif(playermove=="1000 Knives"):
        damage=enemy.hp/3
        resulttext+=enemy.name+" took "+str(damage)+" damage.\n"
    
    else:
        print("ERROR")
        damage=player.atk-enemy.df
        resulttext+=enemy.name+" took "+str(damage)+" damage.\n"
    enemy.hp-=damage
    print(player.name,"used",playermove)
    print(resulttext)
    pass

def handleenemymove():
    global player
    global enemy
    damage=0

    '''
    Wild Stab
    Bulk Up
    Fireball
    Recover
    Heavy Swing
    Targeted Stab
    Energy Drain
    Chaos Blade
    '''

    roll=random.randint(0,99)
    enemymove=""
    resulttext=""
    moveloc=len(enemy.moves)-1
    weightsum=0
    for i in range(len(enemy.weights)):
        weightsum+=enemy.weights[i]
        if(roll<weightsum):
            moveloc=i
            break
    enemymove=enemy.moves[moveloc]
    
    
    if(enemymove=="Wild Stab"):
        damage=2*enemy.atk-player.df
        enemy.atk-=1
        enemy.df-=1
        resulttext+=player.name+" took "+str(damage)+" damage.\n"
        resulttext+=enemy.name+" lost 1 ATK and 1 DEF"
    elif(enemymove=="Battle Cry"):
        enemy.atk+=2
        resulttext+=enemy.name+"gained 2 ATK."
    elif(enemymove=="Fireball"):
        damage=enemy.atk
        resulttext+=player.name+" took "+str(damage)+" damage.\n"
    elif(enemymove=="Recover"):
        healamount=min(enemy.maxhp-enemy.hp,10)
        enemy.hp+=healamount
        resulttext+=enemy.name+"healed "+str(healamount)+" HP."
    elif(enemymove=="Heavy Swing"):
        damage=int(1.5*enemy.atk-player.df)
        resulttext+=player.name+" took "+str(damage)+" damage.\n"
    elif(enemymove=="Energy Drain"):
        damage=int(0.75*enemy.atk-player.df)
        enemy.hp+=damage
        resulttext+=player.name+" took "+str(damage)+" damage.\n"
        resulttext+=enemy.name+" healed "+str(damage)+" HP."
    elif(enemymove=="Draining Punch"):
        damage=int(1*enemy.atk-player.df)
        enemy.hp+=damage
        resulttext+=player.name+" took "+str(damage)+" damage.\n"
        resulttext+=enemy.name+" gained "+str(damage)+" HP."
    elif(enemymove=="Chaos Blade"):
        damage=int(1.5*enemy.atk-player.df)
        enemy.atk+=2
        enemy.df+=1
        resulttext+=player.name+" took "+str(damage)+" damage.\n"
        resulttext+=enemy.name+" gained 2 ATK and 1 DEF."
    elif(enemymove=="Targeted Stab"):
        damage=int(0.75*enemy.atk-player.df)
        player.df-=1
        resulttext+=player.name+" took "+str(damage)+" damage.\n"
        resulttext+=player.name+" lost 1 DEF."
    elif(enemymove=="Stab and Slash"):
        damage=int(1.5*enemy.atk-player.df)
        player.atk-=1
        player.df-=1
        resulttext+=player.name+" took "+str(damage)+" damage.\n"
        resulttext+=player.name+" lost 1 ATK and 1 DEF."
    elif(enemymove=="Intimidating Roar"):
        player.atk-=1
        player.df-=1
        resulttext+=player.name+" lost 1 ATK and 1 DEF."
    elif(enemymove=="Crunch"):
        damage=int(2*enemy.atk-player.df)
        resulttext+=player.name+" took "+str(damage)+" damage.\n"
    elif(enemymove=="Shadowflame"):
        damage=int(0.5*enemy.atk-player.df)
        enemy.atk+=3
        resulttext+=player.name+" took "+str(damage)+" damage.\n"
        resulttext+=enemy.name+" gained 3 ATK"
    elif(enemymove=="Mana Drain"):
        damage=int(enemy.atk-player.df)
        player.mana-=1
        resulttext+=player.name+" took "+str(damage)+" damage.\n"
        resulttext+=player.name+" lost 1 mana"
    elif(enemymove=="Energy Drain+"):
        damage=int(enemy.atk-player.df)
        enemy.hp+=damage
        resulttext+=player.name+" took "+str(damage)+" damage.\n"
        resulttext+=enemy.name+" healed "+str(damage)+" HP."
    elif(enemymove=="Chaos Blade+"):
            damage=int(1.5*enemy.atk-player.df)
            enemy.atk+=3
            enemy.df+=2
            resulttext+=player.name+" took "+str(damage)+" damage.\n"
            resulttext+=enemy.name+" gained 2 ATK and 1 DEF."
    elif(enemymove=="Mana Drain+"):
            damage=int(enemy.atk-player.df)
            player.mana=0
            resulttext+=player.name+" took "+str(damage)+" damage.\n"
            resulttext+=player.name+" lost all mana"
    elif(enemymove=="Final Destination"):
        damage=player.hp//2
        resulttext+=player.name+"lost half their health!"
    else:
        damage=enemy.atk-player.df
        resulttext+=player.name+" took "+str(damage)+" damage.\n"
    player.hp-=damage
    print(enemy.name,"used",enemymove)
    print(resulttext)

    pass


def nextbattle():
    global idx
    global enemyon
    global enemyon
    enemyon+=1

    player.levelup()
    player.resetstats()

    
    

    print("Next Battle!")
    print("Battle ",(enemyon+1),"/",len(enemies),sep="")
    time.sleep(1)
    print("\n\n\n")
    startbattle()

def startbattle():
    global player
    global enemy

    enemy=Enemy(enemies[enemyon]["name"],enemies[enemyon]["hp"],enemies[enemyon]["atk"],enemies[enemyon]["df"],enemies[enemyon]["moves"],enemies[enemyon]["weights"])

    while(player.hp>0 and enemy.hp>0):
        print("Player:",player)
        print()
        print("Enemy:",enemy)
        print()

        handleplayermove()
        if(enemy.hp<=0):
            break
        time.sleep(1)

        handleenemymove()
        if(player.hp<=0):
            break
    
    if(player.hp<=0):
        print("Game Over. Enemies defeated: ",enemyon,"/",len(enemies),sep="")
    else:
        if(enemyon<len(enemies)-1):
            nextbattle()
        else:
            print("You win!")

def main():
    global player
    global playerclasses
    global enemyon
    global idx
    idx=0
    if(not testing):
        selecttext="Select your character:\n"
        selecttext+="0: Warrior- Hit hard\n"
        selecttext+="1: Mage- Buff up\n"
        selecttext+="2: Rogue- Be crafty\n"
        idx=int(input(selecttext))
    else:
        enemyon=testround
        idx=testclass
    print(playerclasses[idx])
    player=Player(playerclasses[idx]["name"],playerclasses[idx]["hp"],playerclasses[idx]["atk"],playerclasses[idx]["df"],playerclasses[idx]["moves"])
    
    if(testing):
        for i in range(enemyon):
            player.levelup()
           
    startbattle()

main()
