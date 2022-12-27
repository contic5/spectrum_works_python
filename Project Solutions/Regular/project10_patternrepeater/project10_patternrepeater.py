import numpy as np
from PIL import Image

#Colors for image
emptycolor=[0,0,100] #Dark Blue
fullcolor=[150,150,255] #Light Blue

#Scale up 2d list and convert it to an array
def pattern_list_to_color_arr(lst,tile_x_size=1,tile_y_size=1):
    #Calculate size of resulting array
    lst_width=len(lst[0])
    lst_height=len(lst)
    arr_width=lst_width*tile_x_size
    arr_height=lst_height*tile_y_size

    #Create array
    arr = np.zeros((arr_width, arr_height, 3), dtype=np.uint8)

    for i in range(lst_height):
        for j in range(lst_width):
            #Fill tile_x_size by tile_y_size square with fullcolor
            if(lst[i][j]==1):
                for a in range(tile_y_size):
                    for b in range(tile_x_size):
                        arr[tile_x_size*j+a,tile_y_size*i+b]=fullcolor
            
            #Fill tile_x_size by tile_y_size square with emptycolor 
            else:
                for a in range(tile_y_size):
                    for b in range(tile_x_size):
                        arr[tile_x_size*j+a,tile_y_size*i+b]=emptycolor
    
    return arr

#Repeat list as pattern
def list_to_pattern_list(pattern,x_repeat=1,y_repeat=1):

    #Calculate size of pattern
    orig_w=len(pattern[0])
    orig_h=len(pattern)
    patternw=orig_w*x_repeat
    patternh=orig_h*y_repeat

    #Create repeated_pattern list
    repeated_pattern = np.empty((patternh, patternw)).tolist()
    print(len(repeated_pattern[0]),len(repeated_pattern))
    for i in range(patternh):
        for j in range(patternw):

            #Find equivalent position in the original pattern.
            orig_y_loc=i%orig_h
            orig_x_loc=j%orig_w
            repeated_pattern[i][j]=pattern[orig_y_loc][orig_x_loc]
    return repeated_pattern

def main():
    #Starting 2d pattern
    pattern=[
    [0,0,1,0,0],
    [0,1,0,1,0],
    [1,0,0,0,1],
    [0,0,0,0,0],
    [0,0,0,0,0]
    ]

    #Generate repeated pattern
    repeated_pattern=list_to_pattern_list(pattern,10,3)
    print(len(repeated_pattern[0]),len(repeated_pattern))
    
    for i in range(len(repeated_pattern)):
        for j in range(len(repeated_pattern[0])):
            if(repeated_pattern[i][j]==1):
                print("X",end="")
            else:
                print(".",end="")
        if(i<len(repeated_pattern)-1):
            print()
    print()
main()