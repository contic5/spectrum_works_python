#percent of ads that show the product quickly per year.
#Ads go from 2000-2020
import matplotlib.pyplot as plt
import numpy as np

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

def graphbykeyname(keyname):
    lines = []
    categories=[]
    ads_by_year=[]
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

    '''
    Matplot-lib Plotting
    https://pythonguides.com/matplotlib-best-fit-line/
    '''

    xpoints=[]
    ypoints=[]
    for i in range(len(ads_by_year)):
        xpoints.append(int(key_byyear[i]["year"])-2000)
        ypoints.append(int(key_byyear[i]["value"]))
    
    xpoints=np.array(xpoints)
    ypoints=np.array(ypoints)
    np.polyfit(xpoints, ypoints, 1)

    theta = np.polyfit(xpoints, ypoints, 1)
    y_line = theta[1] + theta[0] * xpoints

    #plt.xticks(np.arange(min(xpoints), max(xpoints)+1, 1.0))
    plt.ylim([0, 100])
    plt.scatter(xpoints, ypoints)
    plt.plot(xpoints, y_line, 'r')
    plt.title('Best fit line for Year vs '+writtenkeyname)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')

    plt.show()
    return

def main():
    keynames=["funny","show_product_quickly","patriotic","celebrity","danger","animals"]
    for keyname in keynames:
        graphbykeyname(keyname)
main()
