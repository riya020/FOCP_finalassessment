e = [] #creating an empty list to store the speed in KPH

u = [] #creating an empty list to store the speed in MPH

total_e:float=0

number_of_record:int=0

#takes input from the user for speed

speed = input("Enter the Reading: ")



#conditon if the speed entered in null

if speed == "":

    print("No reading entered. Nothing to do.")



#else condition if any input is taken

else:

    #loop runs unless a null entry is recorded

    while True:



        #if the speed is null the loop breaks

        if speed == "":

            break



        #condition if the speed is entered in KPH

        elif speed[0].upper() == "E":

            print("Reading saved")



            e.append(round(float(speed[1:]), 1))    #appends the value in the 'e' list

            speed = float(speed[1:])/1.61           #changes the KPH to MPH

            u.append(round(float(speed), 1))        #Appends the value in the 'u' list

            



        elif speed[0].upper() == "U":

            print("Reading saved")

            u.append(round(float(speed[1:]),1))     #appends the value in the 'u' list

            speed = float(speed[1:])*1.61           #changes the MPH to KPH

            e.append(round(float(speed), 1))        #appends the value in the 'e' list



        else:

            print("Unidentified value")             #if the value entered dosent have an 'E' or "U'

            print("Enter a valid value")



        speed = input("Enter the Next Reading: ")   #asks the user for the another reading.



print("\n")                                         #for line break

print("The values in entered order in KPH are: ")

for x in e:                                         #for loop to print the values in 'e' list

    print(x, end="  ")





print("\n")                                         #for line break

print("The values in entered order in MPH are: ")

for x in u:                                         #for loop to print the values in 'u' list

    print(x, end="  ")



for val in e:                                      #for loop to calculate avg  values in 'e' list

    total_e+=val

    number_of_record+=1



avg_e=total_e/number_of_record

avg_u= avg_e/1.61



temp1 = sorted(e)                                   #temporary list to store the sorted 'e' list

temp2 = sorted(u)                                   #temporary list to store the sorted 'u' list



print("\n")                                         #line break

print("Results Summary")

print()                                             #line break

print(len(u),"reading analysed")

print()                                             #line break

print("Average Speed: ",avg_e,"KPH",avg_u,"MPH")

print("Max Speed: ", temp1[len(temp1)-1], "KPH,", temp2[len(temp2)-1], "MPH")       #displays the max speed in KPH and MPH

print("Min Speed: ", temp1[0], "KPH,", temp2[0], "MPH")

                           



total = 0                                          #total variable set to 0.