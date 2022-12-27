import random
totalplayers=0
players=[]
def setup():
    global totalplayers
    global players

    print("How many players?")
    totalplayers=int(input())
    players=[i for i in range(1,totalplayers+1)]

def handleshift(totalshift):
    global players
    for _ in range(totalshift):
        players=players[1:]+[players[0]]

def playgame():
    global totalplayers
    global players

    print("Start")
    roundon=1
    while(totalplayers>1):
        print("Round ",roundon)
        startshift=random.randint(0,len(players)-1)
        print("Handling start shift of",startshift)
        handleshift(startshift)
        #print(players)

        totalshift=0
        for i in range(len(players)):
            print(players)
            print("First slot gets eliminated.")
            print("Turn",(i+1),"of",len(players))
            print("Player",players[i])
            print("Enter 0 to shift 0 or 1 to shift 1")
            shift=int(input())
            totalshift+=shift
            for j in range(20):
                print()

        totalplayers-=1
        print(players)
        print("Shifting")
        for i in range(totalshift):
            handleshift(1)
            print(players)
        print("Player",players[0],"is eliminated.")
        players=players[1:]
        roundon+=1
    print("Player",players[0],"wins!")


def main():
    print("Hot Potato")
    setup()
    playgame()

if __name__=="__main__":
    main()