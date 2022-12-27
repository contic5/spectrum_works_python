myfile=open("pokemon_type_matchups.csv")
multipliers=[]

#Get lines
lines=myfile.readlines()
for i in range(len(lines)):
    lines[i] = lines[i]. rstrip('\n') 
    lines[i] = lines[i]. strip('\ufeff')

#Get multipliers and add them to 2d list multipliers
for i in range(len(lines)):
    if(i>0):
        curmultipliers=lines[i].split("\t")
        curmultipliers=curmultipliers[1:]
        curmultipliers=[float(i) for i in curmultipliers]
        multipliers.append(curmultipliers)

typenames=lines[0].split("\t")
typenames=typenames[1:]
print(typenames)

#Set up variables
attacktype="Fire"
type1="Water"
type2="Dragon"

attacktype_loc=0
type1_loc=0
type2_loc=-1

#Calculate locations in list for typenames
for i in range(len(typenames)):
    if(typenames[i]==attacktype):
        attacktype_loc=i
    if(typenames[i]==type1):
        type1_loc=i
    if(typenames[i]==type2):
        type2_loc=i

#Multiply based on the 2d list multipliers to determine the damage multiplier.
multiplier=1
multiplier=multipliers[attacktype_loc][type1_loc]
if(type2_loc!=-1):
    multiplier*=multipliers[attacktype_loc][type2_loc]

if(type2!=""):
    print("A ",attacktype," type move hits a ",type1," ",type2," type Pokémon for x",multiplier," damage",sep="")
else:
    print("A ",attacktype," type move hits a ",type1," type Pokémon for x",multiplier," damage",sep="")

