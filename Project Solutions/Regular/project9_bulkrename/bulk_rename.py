import os
import copy


def main():
    foldername="Positive Attitude Test"
    originalname="LL"
    replacename="BL"
    
    #mode can either equal prepend,append or replace
    validmodes=["prepend","append","replace"]
    mode="prepend"
    if mode not in validmodes:
        print("ERROR. MODE IS INVALID")
        return

    for filename in os.listdir(foldername):
        filenameparts=filename.split(".")
        filetype=filenameparts[1]
        filetype="."+filetype
        if(filetype==".docx"):
            newfilename=copy.deepcopy(filename)
            
            if(mode=="prepend"):
                if(not replacename in newfilename):
                    newfilename =replacename+filenameparts[0]+filetype
            elif(mode=="append"):
                if(not replacename in newfilename):
                    newfilename =filenameparts[0]+replacename+filetype
            else:
                newfilename=filename.replace(originalname,replacename)
            
           
            if(filename!=newfilename):
                 # foldername/filename, if .py file is outside folder
                src =foldername+"/"+filename  
                dst =foldername+"/"+newfilename
                
                # rename() function will
                # rename all the files
                print("Renaming",filename,"to",newfilename)
                os.rename(src, dst)

main()