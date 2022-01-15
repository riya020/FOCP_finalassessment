from Game import Game
from teamResult import teamResult
import csv
class Project():

    filename:str="C:\my_project.assessment\Riya.txt"
    # constructor
    def __init__(self): pass

    def run(self):
        try:
            file = open(self.filename)
            type(file)
            csvreader = csv.reader(file)
            myteam_list=[]
            result_list=[]

            #put each row in a Game class
            for row in csvreader:
                if len(row)==4:
                    t1=Game(row[0],int(row[1]),row[2],int(row[3]))
                    myteam_list.append(t1)

            for eachgame in myteam_list:
                blnteam1found: bool=False
                blnteam2found: bool=False
                # if that team is already in a list update that class in a list otherwise insert
                for team in range(0,len(result_list)):
                     if result_list[team].team_name==eachgame.team1:
                        result_list[team].P+=1
                        if eachgame.team1_score>eachgame.team2_score:
                            result_list[team].W+= 1
                        elif eachgame.team1_score==eachgame.team2_score:
                            result_list[team].D+= 1
                        else:
                            result_list[team].L+= 1
                        result_list[team].F+=int(eachgame.team1_score)
                        result_list[team].A+=int(eachgame.team2_score)
                        result_list[team].Diff+=int(eachgame.team1_score)-int(eachgame.team2_score)

                        blnteam1found=True
                     elif result_list[team].team_name==eachgame.team2:
                         result_list[team].P+=1
                         if eachgame.team1_score<eachgame.team2_score:
                             result_list[team].W+= 1
                         elif eachgame.team1_score==eachgame.team2_score:
                             result_list[team].D+= 1
                         else:
                             result_list[team].L+= 1
                         result_list[team].F+=int(eachgame.team2_score)
                         result_list[team].A+=int(eachgame.team1_score)
                         result_list[team].Diff+=int(eachgame.team2_score)-int(eachgame.team1_score)
                         blnteam2found=True
                     else:
                         pass
                if blnteam1found==False:
                    t1result=teamResult()
                    t1result.team_name=eachgame.team1
                    t1result.P+=1
                    if eachgame.team1_score>eachgame.team2_score:
                        t1result.W+= 1
                    elif eachgame.team1_score==eachgame.team2_score:
                        t1result.D+= 1
                    else:
                        t1result.L+= 1
                    t1result.F+=int(eachgame.team1_score)
                    t1result.A+=int(eachgame.team2_score)
                    t1result.Diff+=int(eachgame.team1_score)-int(eachgame.team2_score)
                    result_list.append(t1result)
                if blnteam2found==False:
                    t2result=teamResult()
                    t2result.team_name=eachgame.team2
                    t2result.P+=1
                    if eachgame.team1_score<eachgame.team2_score:
                        t2result.W+= 1
                    elif eachgame.team1_score==eachgame.team2_score:
                        t2result.D+= 1
                    else:
                        t2result.L+= 1
                    t2result.F+=int(eachgame.team2_score)
                    t2result.A+=int(eachgame.team1_score)
                    t2result.Diff+=int(eachgame.team2_score)-int(eachgame.team1_score)
                    result_list.append(t2result)
            print ("{:<15} {:<6} {:<6} {:<6} {:<6} {:<6} {:<6} {:<6} {:<6}".format('','P','W','D','L','F','A','Diff','Pts'))
            for eachResult in result_list:
                eachResult.Pts= 3* eachResult.W +1* eachResult.D
                print("{:<15} {:<6} {:<6} {:<6} {:<6} {:<6} {:<6} {:<6} {:<6}".format(eachResult.team_name,eachResult.P,eachResult.W,eachResult.D,eachResult.L,eachResult.F,eachResult.A,eachResult.Diff,eachResult.Pts))

        except Exception as error :
            print(f'UNEXPECTED ERROR: {error}')

        




if __name__ == '__main__':
    Project().run()