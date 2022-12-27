import pandas as pd

class Threshold:
    def __init__(self,keyname,value,abovethreshold) -> None:
        self.keyname=keyname
        self.value=value
        self.abovethreshold=abovethreshold

class Filter:
    def __init__(self,keyname,value,equalto):
        self.keyname=keyname
        self.value=value
        self.equalto=equalto

def main():
    restaurantfile=open("Top100RestaurantChains.csv","r")

    restaurants=[]
    lines=restaurantfile.readlines()
    lineon=0
    for line in lines:
        line = line. rstrip('\n') 
        line = line. strip('\ufeff')
        if(lineon==0):
            categories=line.split(",")
        else:
            parts=line.split(",")
            restaurant={}
            for category,part in zip(categories,parts):
                if(part.isdecimal()):
                    restaurant[category]=int(part)
                else:
                    restaurant[category]=part
            restaurants.append(restaurant)
        lineon+=1
    
    filters=[]

    '''Not in the mood for burgers, chicken, or Mexican. Also in the mood for casual dining'''

    '''
    filters.append(Filter("MENU CATEGORY","Burger",False))
    filters.append(Filter("MENU CATEGORY","Chicken",False))
    filters.append(Filter("MENU CATEGORY","Mexican",False))
    '''
    filters.append(Filter("SEGMENT","Casual Dining",True))

    #filters.append(Filter("MENU CATEGORY","Italian/Pizza",True))

    for filteritem in filters:
        restaurantscopy=[]
        for restaurant in restaurants:
            if(filteritem.equalto==True and restaurant[filteritem.keyname]==filteritem.value):
                restaurantscopy.append(restaurant)
            if(filteritem.equalto==False and restaurant[filteritem.keyname]!=filteritem.value):
                restaurantscopy.append(restaurant)
        restaurants=restaurantscopy
    for category in categories:
        print(category,end=" ")
    print(end="\n\n")

    pd.set_option('display.max_rows', 10)

    df = pd.DataFrame(restaurants, columns = categories)
    df.index+=1
    print(df)
    

main()