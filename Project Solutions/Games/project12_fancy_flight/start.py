import names
import random

difficultynames=["0","1","2","3","4"]
totaldifficulties=len(difficultynames)

totalscores=5

#Difference between the scores for each difficulty
diff_score_diff=200
indiv_score_diff=diff_score_diff//totalscores
randomscore_diff=indiv_score_diff//totalscores
print(randomscore_diff)

for i in range(totaldifficulties):
    difficultyname=difficultynames[i].lower()
    highscorefile=open("highscores_"+difficultyname+".txt","w")
    res=""
    for j in range(totalscores):
        name=names.get_first_name()
        score=diff_score_diff*(totaldifficulties-i)+indiv_score_diff*(totalscores-j)
        score+=random.randint(0,randomscore_diff)
        res+=name+","+str(score)
        if(j<5-1):
            res+="\n"
    highscorefile.write(res)