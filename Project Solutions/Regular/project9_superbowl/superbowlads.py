#percent of ads that show the product quickly per year.
#Ads go from 2000-2020

def is_int(value):
  try:
    int(value)
    return True
  except:
    return False

def is_float(value):
  try:
    float(value)
    return True
  except:
    return False

def getproperties(line,categories):
    parts=line.split(",")
    item={}
    for i in range(0,len(parts)):
        val=parts[i]
        if(is_int(val)):
            val=int(val)
            item[categories[i]]=val
        elif(is_float(val)):
            val=float(val)
            item[categories[i]]=val
        else:
            item[categories[i]]=val
    return item

def sortFunc(item):
  return item['value']

def main():
  lines = []
  categories=[]
  ads_by_year=[]
  keyname="funny"
  writtenkeyname=keyname.replace("_"," ")
  writtenkeyname=writtenkeyname.title()

  key_byyear=[]
  for i in range(21):
    key_byyear.append({"value":0,"year":2000+i})

  for i in range(21):
    ads_by_year.append([])

  origfile=open('superbowlads_studentversion.csv',"r")
  lines = origfile.readlines()

  count = 0
  for line in lines:
      line = line. rstrip('\n') 
      line = line. strip('\ufeff') 
      if(count==0):
          categories=line.split(",")
      else:
          ad=getproperties(line,categories)
          index=int(ad["year"]-2000)
          print(index)
          ads_by_year[index].append(ad)
          
      count += 1

  results=""
  
  print("Ads by year")
  for i in range(len(ads_by_year)):
    total=0
    for j in range(len(ads_by_year[i])):
      if(ads_by_year[i][j][keyname]=="TRUE"):
        total+=1
    total/=len(ads_by_year[i])
    key_byyear[i]["value"]=round(100*total,2)
    key_byyear[i]["year"]=2000+i

  key_byyear.sort(key=sortFunc)
  print(keyname)
  for i in range(len(key_byyear)):
    print(key_byyear[i]["year"],key_byyear[i]["value"])

main()
