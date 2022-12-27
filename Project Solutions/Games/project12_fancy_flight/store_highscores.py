import names
import copy

difficultynames=["0","1","2","3","4"]
scores=[]
maxscores=5

class GameScore:
    def __init__(self,name,score,difficultyid) -> None:
        self.name=name
        self.score=int(score)
        self.difficultyid=difficultyid
    def __str__(self) -> str:
        return self.name+","+str(self.score)

def writehighscores(highscores,filename):
    highscorefile=open(filename,"w")
    res=""
    for i in range(len(highscores)):
        res+=str(highscores[i])
        if(i<len(highscores)-1):
            res+="\n"
    print(res)
    highscorefile.write(res)
    highscorefile.close()

def checknewscore(playerscore,highscores,filename):
    addindex=-1

    #Check if playerscore beat a highscore
    for i in range(len(highscores)):
        if(playerscore.score>highscores[i].score):
            addindex=i
            break
    
    #Only update scores if playerscore actually beat a high score
    if(addindex>-1):
        print(addindex)
        #Copy scores below high score forward
        for i in range(len(scores)-2,addindex-1,-1):
            highscores[i+1]=copy.deepcopy(highscores[i])

        highscores[addindex]=copy.deepcopy(playerscore)

        #Write new high scores
        writehighscores(highscores,filename)
    else:
        print("The player score did not reach the high score list")

def writescore(score,difficultyid):
    playerscore=GameScore("",score,difficultyid)
    highscores=[]

    difficultyid=playerscore.difficultyid
    difficultyname=difficultynames[difficultyid].lower()
    filename="highscores_"+difficultyname+".txt"

    highscorefile=open(filename,"r")
    lines=highscorefile.readlines()

    for line in lines:
        line = line. rstrip('\n') 
        line = line. strip('\ufeff')
        print(line)
        print()
        parts=line.split(",")
        curscore=GameScore(parts[0],parts[1],difficultyid)
        highscores.append(curscore)
    highscorefile.close()
    if(len(highscores)<maxscores):
        highscores.append(playerscore)
        print(highscores)
        writehighscores(highscores,filename)
    else:
        checknewscore(playerscore,highscores,filename)


