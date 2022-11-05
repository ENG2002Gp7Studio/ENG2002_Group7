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


class phoneRec:
    def __init__(self, name, nickname, phoneNo, email, lastCallDate):
        self.name = name
        self.nickname = nickname
        self.phoneNo = phoneNo
        self.email = email
        self.lastCallDate = lastCallDate

    
class phoneBk:
    def __init__(self):
        self.family = []
        self.friend = []
        self.junk = []

        self.group = [-1, "Family", "Friend", "Junk"]

    def add_rec(self, phRec, grp):                      
                                                        #group 1-Family 2-Friend 3-Junk
        if(grp == 1):
            self.family.append(phRec)
        if(grp == 2):
            self.friend.append(phRec)
        if(grp == 3):
            self.junk.append(phRec)

    def del_rec(self, phNo):                            #Task 0
        pass

    def show_latest_sorted_rec(self, grp):              #Task 1
        pass

    def check_email(self):                              #Task 2
        pass

    def show_name_sorted_rec(self, ascending):          #Task 3
                                                            # ascending = 0: Descending
                                                            # ascending = 1: Ascending
        pass                

    def move_to_group(self, PhNo, grp):                 #Task 4
        pass
