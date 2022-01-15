from operator import contains
from random import choice

class Letter:


    def __init__(self):
        pass
    def Email(self):
        
        Email_adress=input("Please Enter your popppleton email address:")# it asks for user email address of  popppleton
        if "@" in Email_adress:
            subemail=Email_adress.split("@")
            
            
            if len(subemail)==2:
                if len(subemail[0])>=2:
        
                    if subemail[1]== "pop.ac.uk":
                        print("Hi",subemail[0],"! Thank you, and Welcome to PopChat!")
                        self.Talk(subemail[0])

            else:
                print("Your Email is Wrong. Please enter the correct email address")
                exit()
        else:
            print("Your Email is Wrong. Please enter the correct email address")
            exit()
        
            
    def Talk(self,name:str):
        


           
        User=input("Please enter some inputs:")
        if User.upper()=="NI!":
            exit()
        else:
            if "library" in User.lower(): #it translates library to uppercase
                print("The library is closed today.")
            elif "wifi" in User.lower():
                print("WiFi is excellent across the campus.")
            elif "deadline" in User.lower():
                print("Your deadline has been extended by two working days.")
            elif "laptop" in User.lower():
                print("Your laptop is aser.")
            elif "college" in User.lower(): #it translates college to uppercase
                print("you study in popppleton.")
            elif "mobile" in User.lower():
                print("Your mobile is dead")
            
            elif User.lower()=="bye" or User.lower()=="exit" or User.lower()=="Goodbye": #the code exits if the given words are inputs
                exit()
            

            else:
                List_string=["Hmmm", "Oh, yes, I see","Tell me more"]
                print(choice(List_string))
        self.Talk(name)        
                  

if __name__=='__main__':
    _main_obj=Letter()
    _main_obj.Email()               