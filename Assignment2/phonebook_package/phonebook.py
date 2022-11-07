#####################################################################################
#   This module is developed by ENG2002-Group7                                   
#   
#   Collaborators for tasks:
#       Task 0: 
#       Task 1:
#       Task 2:
#       Task 3:
#       Task 4:                                                                          
#####################################################################################

import os

class phoneRec:
    def __init__(self, name, nickname, phoneNo, email, lastCallDate, group):
        self.name = name
        self.nickname = nickname
        self.phoneNo = phoneNo
        self.email = email
        self.lastCallDate = lastCallDate
        self.group = group
        

    
class phoneBk:
    def __init__(self, useFilePath = True, phoneRecList = -1):
        self.family = []
        self.friend = []
        self.junk = []

        self.group = [-1, "Family", "Friend", "Junk"]   #group 1-Family 2-Friend 3-Junk
        self.filePath = -1
 

        self.sys_init(self, useFilePath, phoneRecList)

        

    def sys_init(self, useFilePath, phoneRecList):
                                                        #0: Everything OK; -1: File not exist; 
        if(phoneRecList != -1):
            if(useFilePath):
                self.ph_database_access(phoneRecList)
                

            else:
                for i in range(0, len(phoneRecList)):
                    self.add_rec(phoneRecList[i], phoneRecList[i].group)
        else:
            pass
            


    def add_rec(self, phRec, grp):                      
                                                        #group 1-Family 2-Friend 3-Junk
        if(grp == 1):
            self.family.append(phRec)
        if(grp == 2):
            self.friend.append(phRec)
        if(grp == 3):
            self.junk.append(phRec)

    def del_rec(self, grp, phNo):                       #Task 0
        pass

    def show_latest_sorted_rec(self, grp):              #Task 1
        pass

    def check_email(self, grp):                         #Task 2
        pass

    def show_name_sorted_rec(self, ascending):          #Task 3
                                                            # ascending = 0: Descending
                                                            # ascending = 1: Ascending
        pass                

    def copy_to_group(self, PhNo, grp):                 #Task 4
        pass

    def menu():
        pass

    def ph_database_access(self, filePath):
        
        if(os.path.isfile(filePath)):
            ph_database = open(filePath, "r")

            while(True):
                recSour = ph_database.readline()
                if(recSour == ""):
                    break
                recSplit = recSour.split("///")             #Maybe need some encrytion or decryption
                recTemp = phoneRec(recSplit[0], recSplit[1], recSplit[2], recSplit[3], recSplit[4], recSplit[5])
                self.add_rec(recTemp, recSplit[5])
        
        else:
            return -1




