print("Stop! Who would cross the Bridge of Death\nMust answer me these questions three, 'ere the other side he see.\n")
name=input("What is your name? ") #takes input from user
name= name.upper() #.upper converts the string in uppercase
if name=="ARTHUR":
    print("My liege! You may pass!")
elif name.upper()!="ARTHUR":
    quest= input("What is your quest?")
    quest= quest.upper() 
    if "GRAIL" in quest: #loop checks quest string has grail or not
        color=input("What is your favourite color?")
        color=color.upper()
        if color[0]==name[0]:
            print("You may pass!")
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril.")
    else:
         print("Only those who seek the Grail may pass.")
             
        

