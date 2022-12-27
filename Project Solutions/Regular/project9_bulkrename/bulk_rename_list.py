import os
import copy


def main():
    foldername="Positive Attitude Test"
    #Changing Low Level, Medium Level and High Level to Basic Level, Intermediate Level and Advanced Level
    originalnames=["LL","ML","HL"]
    replacenames=["BL","IL","AL"]
    
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
            
            for i in range(len(originalnames)):
                if(mode=="prepend"):
                    if(not replacenames[i] in newfilename and originalnames[i] in newfilename):
                        newfilename =originalnames[i]+filenameparts[0]+filetype
                elif(mode=="append"):
                    if(not replacenames[i] in newfilename and originalnames[i] in newfilename):
                        newfilename =filenameparts[0]+originalnames[i]+filetype
                else:
                    if(originalnames[i] in newfilename):
                        newfilename=filename.replace(originalnames[i],replacenames[i])
            
           
            if(filename!=newfilename):
                 # foldername/filename, if .py file is outside folder
                src =foldername+"/"+filename  
                dst =foldername+"/"+newfilename
                
                # rename() function will
                # rename all the files
                print("Renaming",filename,"to",newfilename)
                os.rename(src, dst)

main()