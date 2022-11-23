#####################################################################################
#   This module is developed by ENG2002-Group7                                   
#   
#   Collaborators for tasks:
#       Task 0: QIN Qijun
#       Task 1: QIN Qijun
#       Task 2: LIN Ju
#       Task 3: NI Rouheng + QIN QIjun
#       Task 4: QIN Qijun
#       Program structure and database constructor: QIN Qijun
#       
#####################################################################################

import os
import sys

class phoneRec:

    rec_type = ["Phone Number", "Group", "Name", "Nickname", "Email", "The last datetime of Phone Call"]

    ##
    # @brief    Set database fields
    #
    # @note     PhoneNo & group is the two Private Keys 
    #
    def __init__(self, phoneNo, group, name, nickname, email, lastCallDate):
        self.phoneNo = phoneNo 
        self.group = int(group)
        self.name = name
        self.nickname = nickname
        self.email = email
        self.lastCallDate = lastCallDate


  
class phoneBk:

    ##
    # @param    (str)filePath               Databse path
    # @param    (bool)syncing_from_databse  True: Get sync from the database
    # @param    (list)phoneRecList          -1:                         Nothing to do
    #                                       A list of (class)phoneRec:  Add record to 3 groups of list
    #      
    def __init__(self, filePath, syncing_from_databse = True, phoneRecList = -1):
        self.family = []
        self.friend = []
        self.junk = []

        self.group = [-1, "Family", "Friend", "Junk", "All"]   #group 1-Family 2-Friend 3-Junk
        self.filePath = -1
 

        self.ph_status = self.sys_init(filePath, syncing_from_databse, phoneRecList)

        

    def sys_init(self, filePath, syncing_from_databse = True, phoneRecList = -1):
                                                        #0: Everything OK; -1: File not exist; -2: Database Conflict
        
        if(self.ph_database_access(filePath) == 0): # database can access

            self.filePath = filePath  # set database path
            if(syncing_from_databse):           
                self.ph_syncing_from_database() # True -> Get sync from the database
            if(phoneRecList != -1):
                self.add_recs(phoneRecList)     # Add record to 3 groups of list
            return 0
                

        else:
            return -1
            


    def add_rec(self, phRec):       # add a record only, return a list with an element that cannot add in                
                                                        #group 1-Family 2-Friend "3"-Junk
        if(self.ph_conflict_check(phRec.phoneNo, phRec.group)):  # Check whether the phRec has exist
            return [phRec]
        if(phRec.group == 1):
            self.family.append(phRec)
        if(phRec.group == 2):
            self.friend.append(phRec)
        if(phRec.group == 3):
            self.junk.append(phRec)
        return []   

    def add_recs(self, phRecList):  # add records, return a list of phRec that cannot add in                    
                                                        #group 1-Family 2-Friend 3-Junk
        conflictList = []
        for phRec in phRecList:
            if(self.ph_conflict_check(phRec.phoneNo, phRec.group)):  # check whether the phRec has exist
                conflictList.append(phRec)
                continue
            if(phRec.group == 1):
                self.family.append(phRec)
            if(phRec.group == 2):
                self.friend.append(phRec)
            if(phRec.group == 3):
                self.junk.append(phRec)

        return conflictList     # return repetitive phRec

    def split_group(self, sourList):    # give a list of phRec, split it into 3 group

        family = []
        friend = []
        junk = []
        for i in range(0, len(sourList)):
            if(sourList[i].group == 1):
                family.append(sourList[i])
            if(sourList[i].group == 2):
                friend.append(sourList[i])
            if(sourList[i].group == 3):
                junk.append(sourList[i])

        return family, friend, junk


    def ph_rec_retrieve(self, recList, phNo, grp = 0):  # Search phRec by phone number in the list based on given group
                                                        # if grp = 0, the function will search all the group

        res = []
        for phRec in recList:
            if(phRec.phoneNo == phNo and (phRec.group == grp or grp == 0)):
                res.append(phRec)

        return res


    def del_rec(self, phNo, grp):                       #Task 0, delete a phRec by phone number and given group
        
        grp = int(grp)
        if(grp == 1):
            phRec = self.ph_rec_retrieve(self.family, phNo, 1)
            if(phRec == []):
                return []
            self.family.remove(phRec[0])

        if(grp == 2):
            phRec = self.ph_rec_retrieve(self.friend, phNo, 2)
            if(phRec == []):
                return []
            self.friend.remove(phRec[0])

        if(grp == 3):
            phRec = self.ph_rec_retrieve(self.junk, phNo, 3)
            if(phRec == []):
                return []
            self.junk.remove(phRec[0])

        return [phRec[0]]   # if delete successfully, then return a list of phRec, otherwise return empty list



    def latest_sorted_rec(self, phRecList):              #Task 1, show sorted phone records based on last-call datetime

        sel_group = []
        datetimeError = []
        sorted_group = []
        for i in range(len(phRecList)):
            t = phRecList[i]
            sorted_group.append(phoneRec(t.phoneNo, t.group, t.name, t.nickname, t.email, t.lastCallDate))

        for i in range(0, len(phRecList)):
            tempList = phRecList[i]
            tempList.lastCallDate = tempList.lastCallDate + '0' * 16    #
            tempList.lastCallDate = tempList.lastCallDate[:16]          # To make the length of datatime the same
            if(tempList.lastCallDate.isnumeric()):                      #
                sel_group.append(tempList)                              #
            else:
                datetimeError.append(phRecList[i].lastCallDate.isnumeric())

        if(len(phRecList) > 0):
            for i in range(1, len(sorted_group)):               # Bubble Sort, compare last call datatime
                for j in range(0, len(sorted_group) - i):
                    if sel_group[j].lastCallDate < sel_group[j + 1].lastCallDate:
                        sorted_group[j], sorted_group[j + 1] = sorted_group[j + 1], sorted_group[j] # Source data
                        sel_group[j], sel_group[j + 1] = sel_group[j + 1], sel_group[j]             # Edited data for comparing
            
        return sorted_group + datetimeError

    #NOT DONE                                           #Task 2
    #Return -1 refers to invalidation, while 0 refers to validization
    def verify_one_email(self, email_address):
            # check if there is only one '@'
            at = 0
            for element in email_address:
                if element == '@':
                    at = at + 1

            if at != 1:
                return False

            # Ensure no illegal spacing
            for element in email_address:
                if element == ' ':
                    return False

            # check '.' after @
            pos = email_address.find('@')
            dotcheck = email_address[pos+1:] #To ensure that . is not right after @
            if '.' not in dotcheck:
                return False


            # check if it contains valid characters including 0-9, upper and lower case letters, '.' , '@',and '_'
            pos = email_address.find('@')
            left = email_address[pos-1:pos]
            #right = email_address[pos:]
            if left.isalpha() == False and left.isdigit() == False:
                #if right.element.isalpha() == False and right.element.isdigit() == False:
                #if element != '.' and element != '@' and element != '_':
                return False
            
            return True
    
    # def check_email(self):    
        
        # # main
        # email_address = input('Please input your email for verification: ')
        # #check_email(email_address)
        # if verify_one_email(email_address) == -1:
        #     print('No invalid emails found in this user group.')
        # else:
        #     print('Invalid Email!')

        # invalid = []
        # def verifyfamily():
        #     for i in range(0, len(self.family)):    
        #         if (not self.verify_one_email(self.family[i].email)):
        #             invalid.append(self.family[i])
        #         return invalid
        # def verifyfriend():
        #     for i in range(0, len(self.friend)):    
        #         if (not self.verify_one_email(self.friend[i].email)):
        #             invalid.append(self.friend[i])
        #         return invalid
        # def verifyjunk():
        #     for i in range(0, len(self.junk)):    
        #         if (not self.verify_one_email(self.junk[i].email)):
        #             invalid.append(self.junk[i])
        #         return invalid
        # def verifyall():
        #     for i in range(0, len(self.family)):    
        #         if (not self.verify_one_email(self.family[i].email)):
        #             invalid.append(self.family[i])
        #     for i in range(0, len(self.friend)):    
        #         if (not self.verify_one_email(self.friend[i].email)):
        #             invalid.append(self.friend[i])
        #     for i in range(0, len(self.junk)):    
        #         if (not self.verify_one_email(self.junk[i].email)):
        #             invalid.append(self.junk[i])
        #     return invalid

  
    
    def nickname_sorted_rec(self, phRecList, ascending = 1):          #Task 3
                                                            # ascending = 1: Descending
                                                            # ascending = 2: Ascending
        sorted_group = phRecList

        if(ascending == 2):
            sort_mode = -1
        else:
            sort_mode = 1

        if(len(phRecList) > 0):
            for i in range(1, len(sorted_group)):               # Bubble Sort, compare nickname
                for j in range(0, len(sorted_group) - i):
                    if(self.str_compare(sorted_group[j].nickname, sorted_group[j + 1].nickname) * sort_mode > 0):
                        sorted_group[j], sorted_group[j + 1] = sorted_group[j + 1], sorted_group[j]     

        return sorted_group 


    def copy_to_group(self, phNo, ori_grp, tar_grp):             #Task 4, copies the phone record of a user-input phone number from 
                                                                    # one user-given group to another user-given group.

        all_group = [-1, self.family, self.friend, self.junk]
        phRec = self.ph_rec_retrieve(all_group[ori_grp], phNo)
        if(len(phRec) == 0):
            return [-1]
        phRec[0].group = tar_grp
        return self.add_rec(phRec[0])

    


    ##
    # @brief    Check for phone number conflicts in the database or in the specified group
    #
    # @param    (str)phoneNo            Phone Number
    # @param    (int)group              -1: check in the database; 1/2/3: check in given group
    # @param    (int)check_in_database  True: Check conflict in database; False: Check conflict in given group
    #
    # @return   True: have conflict; False: have not conflict
    #
    # @note     Need to access database successfully before use it if check_in_database = True. 
    #               To reset the database path, use phoneBK.ph_databse_access(filePath)
    #
    def ph_conflict_check(self, phoneNo, grp, check_in_database = False):
        grp = int(grp)                                        
        ph_conflict = False
        if(not check_in_database):      # check in the given group
            if(grp == 1):
                for phRec in self.family:
                    if(phRec.phoneNo == phoneNo):
                        ph_conflict = True
            if(grp == 2):
                for phRec in self.friend:
                    if(phRec.phoneNo == phoneNo):
                        ph_conflict = True
            if(grp == 3):
                for phRec in self.junk:
                    if(phRec.phoneNo == phoneNo):
                        ph_conflict = True

        else:                           # check in the database
            ph_database = open(self.filePath, "r")
            while(True):
                recSour = ph_database.readline()
                if(recSour == ""):
                    break
                recSplit = recSour.split("///") 
                if(recSplit[0] == phoneNo and recSplit[1] == grp):
                    ph_conflict = True
                    break
            ph_database.close()
        
        return ph_conflict


    ##
    # @brief    Write a list of data in the tail of database
    #
    # @param    (list)phRecList     a list of (class)phoneRec
    #
    # @return   A list of (class)phoneRec that cannot write in database
    #
    # @note     Need to access database successfully before use it. 
    #               To reset the database path, use (class)phoneBK.ph_databse_access(filePath)
    #
    def ph_database_write(self, phRecList):

        phRecConflictList = []
        phWriteInList = []
        
        for phRec in phRecList:
            if(self.ph_conflict_check(phRec.phoneNo, phRec.group, True)): # check conflict
                phRecConflictList.append(phRec)
            else:
                phWriteInList.append(phRec)

        ph_database = open(self.filePath, "a") 
        for phRec in phWriteInList:                 # Write in database in a spacific format
            ph_database.write(phRec.phoneNo + "///" + str(phRec.group) + "///" + phRec.name + "///" + phRec.nickname + "///" + 
                                phRec.email + "///" + phRec.lastCallDate + "\n")
        
        ph_database.close()
        return phRecConflictList

    ##
    # @brief    Read a list of all data in the tail of database
    # 
    # @return   A list of (class)phoneRec that cannot write in database
    #
    # @note     Need to access database successfully before use it. 
    #               To reset the database path, use (class)phoneBK.ph_databse_access(filePath) 
    #
    def ph_database_read(self):

        ph_database = open(self.filePath, "r")

        databaseRecList = []
        while(True):
            recSour = ph_database.readline()
            if(recSour == ""):
                break
            recSplit = recSour.split("///")             #Maybe need some encrytion or decryption
            recTemp = phoneRec(recSplit[0], recSplit[1], recSplit[2], recSplit[3], recSplit[4], recSplit[5])
            databaseRecList.append(recTemp)
        
        return databaseRecList
            
            
    ##
    # @brief    Get sync from the database
    # After using this function, all data in the database will be automatically synchronized to the 3 groups
    # 
    # @return   0 = success
    #
    # @note     Need to access database successfully before use it. 
    #               To reset the database path, use (class)phoneBK.ph_databse_access(filePath) 
    #
    def ph_syncing_from_database(self):

        ph_database = open(self.filePath, "r")

        # clear the 3-group list
        self.family = []
        self.friend = []
        self.junk = []
        while(True):
            recSour = ph_database.readline()
            if(recSour == ""):
                break
            recSplit = recSour.split("///")           
            recSplit[5] = recSplit[5][0: len(recSplit[5]) - 1]  # cancel '\n'
            recTemp = phoneRec(recSplit[0], int(recSplit[1]), recSplit[2], recSplit[3], recSplit[4], recSplit[5])
            self.add_rec(recTemp)
        
        ph_database.close()
        return 0

    ##
    # @brief    Sync to database
    # After using this function, the data from the 3 groups will overwrite the database
    # 
    # @return   0 = success
    #
    # @note     Need to access database successfully before use it. 
    #               To reset the database path, use (class)phoneBK.ph_databse_access(filePath) 
    #
    def ph_syncing_to_database(self):

        ph_database = open(self.filePath, "w")
        ph_database.close()

        self.ph_database_write(self.family)
        self.ph_database_write(self.friend)
        self.ph_database_write(self.junk)

        return 0

    ##
    # @brief    Compare the difference between 3 group list and database
    #
    # @param    (list)recList   A list of (class)phRec for comparison
    # 
    # @return   (list)databaseHaveNot, (list)phRecListHaveNot
    #           - Return two list of (class)phRec
    #           -- databaseHaveNot:  Data that exists in 3-group lists but not in the database
    #           -- phRecListHaveNot: Data that exists in the database but not in the three lists
    #
    # @note     Need to access database successfully before use it. 
    #               To reset the database path, use (class)phoneBK.ph_databse_access(filePath) 
    #        
    def compare_database(self, recList):

        databaseHaveNot = []
        phRecListHaveNot = []

        databaseList = self.ph_database_read()
        family, friend, junk = self.split_group(databaseList)
        for i in range(0, len(recList)):                            # use 3-g list to compare database
            if(recList[i].group == 1 and not recList[i] in family):
                phRecListHaveNot.append(recList[i])
                continue
            if(recList[i].group == 2 and not recList[i] in friend):
                phRecListHaveNot.append(recList[i])
                continue
            if(recList[i].group == 3 and not recList[i] in junk):
                phRecListHaveNot.append(recList[i])
                continue

        family, friend, junk = self.split_group(recList)
        for i in range(0, len(databaseList)):                       # use database to compare 3-g list
            if(databaseList[i].group == 1 and not databaseList[i] in family):
                databaseHaveNot.append(recList[i])
                continue
            if(databaseList[i].group == 2 and not databaseList[i] in friend):
                databaseHaveNot.append(recList[i])
                continue
            if(databaseList[i].group == 3 and not databaseList[i] in junk):
                databaseHaveNot.append(recList[i])
                continue

        return databaseHaveNot, phRecListHaveNot


    ##
    # @brief    Access database
    # If the database is valid, access it; if not, create a new database; if it cannot be created, return an error value
    #
    # @param    (str)filePath   The path of the database
    # 
    # @return   0: Access; -1: File not exist
    #        
    def ph_database_access(self, filePath):
        
        if(self.isfile(filePath)):   # file exist, return 0
            self.filePath = filePath
            return 0
        
        else:
            filePath_temp = filePath.split("\\")
            fileRootPath = filePath_temp[0]
            for i in range(1, len(filePath_temp) - 1):      # get root path from filePath
                fileRootPath += "\\" + filePath_temp[i]

            if(not os.path.exists(fileRootPath)):   # create folder use root path
                os.makedirs(fileRootPath)
            
            try:
                f = open(filePath, "w")
            except IOError:
                return -1
            f.close()
            if(self.isfile(filePath)):   # create file use filePath
                self.filePath = filePath
                return 0
            else:
                return -1
    


    def time_split_str(self, timeStr):  
                                        # e.g. 20221111120345 -> [2022, 11, 11, 12, 03, 45]
                                        # or 2022-11-11 12:03:45 -> [2022, 11, 11, 12, 03, 45]

        timeStr = str(timeStr)
        if(len(timeStr) < 20):
            if(timeStr[len(timeStr) - 1] == '\n'):
                timeStr = timeStr[0: len(timeStr) - 1]
            timeStr += 'x' * (20 - len(timeStr))
                
        if(len(timeStr.split('-')) > 1):            
            year = timeStr[0: 4]
            month = timeStr[5: 7]
            day = timeStr[8: 10]
            hour = timeStr[11: 13]
            minite = timeStr[14: 16]
            second = timeStr[17: 19]

        else:
            year = timeStr[0: 4]
            month = timeStr[4: 6]
            day = timeStr[6: 8]
            hour = timeStr[8: 10]
            minite = timeStr[10: 12]
            second = timeStr[12: 14]

        return [year, month, day, hour, minite, second]


    def time_combine(self, timeList, mode = 1):
                                                # e.g. [2022, 11, 11, 12, 03, 45] -> 20221111120345         (mode = 1)
                                                #                              or -> 2022-11-11 12:03:45    (mode = 2)
        if(mode == 1):
            return timeList[0] + timeList[1] + timeList[2] + timeList[3] + timeList[4] + timeList[5]
        if(mode == 2):
            return timeList[0] + '-' + timeList[1] + '-' + timeList[2] + ' ' + timeList[3] + ':' + timeList[4] + ':' + timeList[5]


    def pb_encryption(self, ip):

        op = ""
        for i in range(0, len(ip)):
            op += chr(ord(ip[i]) + 35409)

        return op

    def pb_decryption(self, ip):

        op = ""
        for i in range(0, len(ip)):
            op += chr(ord(ip[i]) - 35409)

        return op

    def str_compare(self, str1, str2):
        if(str1 < str2):
            return -1
        if(str1 == str2):
            return 0
        if(str1 > str2):
            return 1

    def isfile(self, filePath):             # Check whether the file can access
        try:
            t_try = open(filePath, 'r')
        except IOError:
            return False
        t_try.close()
        return True



    def built_in_menu(self):
        while(True):
            while(True):
                system("cls")
                print("**********************************************************************")
                print("*   Welcome to use ENG2002 Group7 Phone Book System!                 *")
                print("*   Your Database Path: {}".format(self.filePath))
                print("*                                                                    *")
                print("*   Please Choose the option below:                                  *")
                print("*                                                                    *")
                print("*   1. Add Phone Record                                              *")
                print("*   2. Delete Phone Record (Task 0)                                  *")
                print("*   3. Show Phone Record sorted by latest Datetime (Task 1)          *")
                print("*   4. Check Email Correctness (Task 2)                              *")
                print("*   5. Show Phone Record sorted by Name (Task 3)                     *")
                print("*   6. Copy Phone Record to Group...                                 *")
                print("*   7. Show Phone Record                                             *")
                print("*   8. Exit                                                          *")
                print("*                                                                    *")
                print("**********************************************************************")

                ip = str(input("\nInput the number and Enter to continue: ")) + '0'
                ip = ip[0]
                if('1' <= ip <= '8'):
                    break

            if(ip == '1'):
                while(True):
                    system("cls")
                    ip1 = 0
                    print("**********************************************************************")
                    print("*   (Add Record) Please Choose Group                                 *")
                    print("*                                                                    *")
                    print("*   1. Family                                                        *")
                    print("*   2. Friend                                                        *")
                    print("*   3. Junk                                                          *")
                    print("*   4. Return to menu                                                *")
                    print("*                                                                    *")
                    print("**********************************************************************")

                    ip1 = str(input("\nInput the number and Enter to continue: ")) + '0'
                    ip1 = ip1[0]
                    if('1' <= ip <= '4'):
                        break
                
                if(ip1 == '4'):
                    continue

                recInput = []
                system("cls")
                for i in range(0, len(phoneRec.rec_type)):
                    if(i == len(phoneRec.rec_type) - 1):
                        print("\nPlease input {}: ".format(phoneRec.rec_type[i]))
                        print("(Format: year + month + day + hour + minute + second)")
                        print("(E.g.: 9/Nov/2022 23:01:45 --> 20221109230145)\n")
                        recInput.append(input())
                        break

                    if(i == 1):
                        recInput.append(ip1)
                        continue
                    recInput.append(input("Please input {}: ".format(phoneRec.rec_type[i])))
                
                recAdd = phoneRec(recInput[0], recInput[1], recInput[2], recInput[3], recInput[4], recInput[5])
                system("cls")
                if(self.add_rec(recAdd) == []):
                    self.ph_syncing_to_database()
                    print("\nAdding Complete!\n\nThe new record is:\n")
                    print("Group: {}\nName: {}\nPhone Number: {}\nNickname: {}\nEmail: {}\nLast call Datetime: {}\n".format(
                        self.group[recAdd.group], recAdd.name, recAdd.phoneNo, recAdd.nickname, 
                        recAdd.email, self.time_combine(self.time_split_str(recAdd.lastCallDate), 2)
                    ))
                else:
                    print("\nAdding failed! The record has been exist!\n")
                system("PAUSE")



            if(ip == '2'):
                while(True):
                    system("cls")
                    ip2 = 0
                    print("**********************************************************************")
                    print("*   (Delete Record) Please Choose Group                              *")
                    print("*                                                                    *")
                    print("*   1. Family                                                        *")
                    print("*   2. Friend                                                        *")
                    print("*   3. Junk                                                          *")
                    print("*   4. Return to menu                                                *")
                    print("*                                                                    *")
                    print("**********************************************************************")

                    ip2 = str(input("\nInput the number and Enter to continue: ")) + '0'
                    ip2 = ip2[0]
                    if('1' <= ip2 <= '4'):
                        break

                if(ip2 == '4'):
                    continue

                system("cls")
                print("Delete From Group - {}".format(self.group[int(ip2)]))
                print("\nPlease input the phone number:\n")
                phNo = input()
                delRec = self.del_rec(phNo, int(ip2))
                if(delRec == []):
                    print("\nFailed to delete. The record is not exist!\n")
                    system("PAUSE")
                else:
                    self.ph_syncing_to_database()
                    print("\nDelete successfully!\nThe deleted record is:\n")
                    print("Group: {}\nName: {}\nPhone Number: {}\nNickname: {}\nEmail: {}\nLast call Datetime: {}\n".format(
                        self.group[delRec[0].group], delRec[0].name, delRec[0].phoneNo, delRec[0].nickname, 
                        delRec[0].email, self.time_combine(self.time_split_str(delRec[0].lastCallDate), 2)))
                    system("PAUSE")

            if(ip == '3'):
                while(1):
                    system("cls")
                    ip3 = 0
                    print("**********************************************************************************")
                    print("*   (Show sorted phone records (last-call datetime)) Please Choose Group:        *")
                    print("*                                                                                *")
                    print("*   1. Family                                                                    *")
                    print("*   2. Friend                                                                    *")
                    print("*   3. Junk                                                                      *")
                    print("*   4. All                                                                       *")
                    print("*   5. Return to menu                                                            *")
                    print("*                                                                                *")
                    print("**********************************************************************************")
                    
                    
                    ip3 = str(input("\nInput the number and Enter to continue: ")) + '0'
                    ip3 = ip3[0]
                    if('1' <= ip3 <= '5'):
                        break
                if(ip3 == '5'):
                    continue
                
                all_group = [-1, self.family, self.friend, self.junk]
                if('1' <= ip3 <= '3'):
                    sorted_group = self.latest_sorted_rec(all_group[int(ip3)])
                if(ip3 == '4'):
                    sorted_group = self.latest_sorted_rec(all_group[1] + all_group[2] + all_group[3])

                print("\nPhone record of group {} sorted by call datetime: \n".format(self.group[int(ip3)]))
                print("     Phone Number | Name | Nickname | Email | Last call datetime")
                for phRec in sorted_group:
                    self.print_one_rec(phRec)
                
                print()
                system("PAUSE")


            if(ip == '4'):
                invalid = []
                while(1):
                    print("**********************************************************************")
                    print("*   (Check Email Validity) Please Choose Group:                      *")
                    print("*                                                                    *")
                    print("*   1. Family                                                        *")
                    print("*   2. Friend                                                        *")
                    print("*   3. Junk                                                          *")
                    print("*   4. All                                                           *")
                    print("*   5. Return to menu                                                *")
                    print("*                                                                    *")
                    print("**********************************************************************")
                    
                    ip4 = 0
                    ip4 = str(input("\nInput the number and Enter to continue: ")) + '0'
                    ip4 = ip4[0]
                    if('1' <= ip4 <= '5'):
                        break

                if(ip4 == '5'):
                    continue
                    
                if(ip4 == '1'):
                    for i in range(0, len(self.family)):
                        if (not self.verify_one_email(self.family[i].email)):
                            invalid.append(self.family[i])

                if(ip4 == '2'):
                    for i in range(0, len(self.friend)): 
                        if (not self.verify_one_email(self.friend[i].email)): 
                            invalid.append(self.friend[i])

                if(ip4 == '3'):
                    for i in range(0, len(self.junk)): 
                        if (not self.verify_one_email(self.junk[i].email)): 
                            invalid.append(self.junk[i])
                                
                if(ip4 == '4'):
                    for i in range(0, len(self.family)):
                        if (not self.verify_one_email(self.family[i].email)):
                            invalid.append(self.family[i])
                    for i in range(0, len(self.friend)): 
                        if (not self.verify_one_email(self.friend[i].email)): 
                            invalid.append(self.friend[i])
                    for i in range(0, len(self.junk)): 
                        if (not self.verify_one_email(self.junk[i].email)): 
                            invalid.append(self.junk[i])
                #return invalid

                
                #invalid = self.check_email()
                if len(invalid) == 0:
                    print("No invalid email address is found.")
                if len(invalid) != 0:
                    for i in range (0,len(invalid)):
                        print("The {}'s email '{}' is invalid.".format(invalid[i].nickname, invalid[i].email))

                system("PAUSE")


            if(ip == '5'):
                while(1):
                    system("cls")
                    ip5 = 0
                    print("**************************************************************************")
                    print("*   (Show sorted phone records (nickname)) Please Choose Group:          *")
                    print("*                                                                        *")
                    print("*   1. Family                                                            *")
                    print("*   2. Friend                                                            *")
                    print("*   3. Junk                                                              *")
                    print("*   4. All                                                               *")
                    print("*   5. Return to menu                                                    *")
                    print("*                                                                        *")
                    print("**************************************************************************")
                    
                    
                    ip5 = str(input("\nInput the number and Enter to continue: ")) + '0'
                    ip5 = ip5[0]
                    if('1' <= ip5 <= '5'):
                        break

                if(ip5 == '5'):
                    continue


                while(1):
                    system("cls")
                    sort_mode = 0
                    print("**************************************")
                    print("*   Sort by:                         *")
                    print("*                                    *")
                    print("*   1. Ascending                     *")
                    print("*   2. Descending                    *")
                    print("*                                    *")
                    print("**************************************")
                    
                    
                    sort_mode = str(input("\nInput the number and Enter to continue: ")) + '0'
                    sort_mode = sort_mode[0]
                    if('1' <= sort_mode <= '2'):
                        break
                
            
                all_group = [-1, self.family, self.friend, self.junk]
                if('1' <= ip5 <= '3'):
                    sorted_group = self.nickname_sorted_rec(all_group[int(ip5)], int(sort_mode))
                if(ip5 == '4'):
                    sorted_group = self.nickname_sorted_rec(all_group[1] + all_group[2] + all_group[3], int(sort_mode))

                print("\nPhone record of group {} sorted by nickname: \n".format(self.group[int(ip5)]))
                print("     Nickname | Name | Phone Number | Email | Last call datetime")
                for phRec in sorted_group:
                    print("     {} | {} | {} | {} | {}".format(phRec.nickname, phRec.name, phRec.phoneNo, 
                                                        phRec.email, self.time_combine(self.time_split_str(phRec.lastCallDate), 2)))
                
                print()
                system("PAUSE")
                

            if(ip == '6'):
                while(1):
                    system("cls")
                    ip6 = 0
                    print("**************************************************************************")
                    print("*   (Copy phone record to group...) Please Choose Group:                 *")
                    print("*                                                                        *")
                    print("*   1. Family                                                            *")
                    print("*   2. Friend                                                            *")
                    print("*   3. Junk                                                              *")
                    print("*   4. Return to menu                                                    *")
                    print("*                                                                        *")
                    print("**************************************************************************")
                    
                    
                    ip6 = str(input("\nInput the number and Enter to continue: ")) + '0'
                    ip6 = ip6[0]
                    if('1' <= ip6 <= '4'):
                        break

                if(ip6 == '4'):
                    continue

                system("cls")

                print("(Copy phone record to group...) Please input phone number (input '#' to cancel):\n")
                ip_phNo = input()
                if(ip_phNo == '#'):
                    continue
                all_group = [-1, self.family, self.friend, self.junk]
                ori_rec = self.ph_rec_retrieve(all_group[int(ip6)], ip_phNo)
                if(ori_rec == []):
                    print("\nCannot find phone record '{}' in group {}\n".format(ip_phNo, self.group[int(ip6)]))
                    system("PAUSE")
                    continue
                
                while(1):
                    system("cls")
                    ip6a = 0
                    print("**********************************************************************************")
                    print("     Phone Number | Name | Nickname | Email | Last call datetime")
                    self.print_one_rec(ori_rec[0])
                    print("*                                                                                *")
                    print("*   (Copy phone record to group...) Copy the record to group...:                 *")
                    print("*                                                                                *")
                    print("*   1. Family                                                                    *")
                    print("*   2. Friend                                                                    *")
                    print("*   3. Junk                                                                      *")
                    print("*   4. Cancel                                                                    *")
                    print("*                                                                                *")
                    print("**********************************************************************************")
                    
                    
                    ip6a = str(input("\nInput the number and Enter to continue: ")) + '0'
                    ip6a = ip6a[0]
                    if('1' <= ip6a <= '4'):
                        break

                if(ip6a == '4'):
                    continue
                
                conflictList = self.copy_to_group(ip_phNo, int(ip6), int(ip6a))
                if(conflictList == [-1]):
                    print("\nCannot find phone record '{}' in group {}\n".format(ip_phNo, self.group[int(ip6)]))
                    system("PAUSE")
                elif(conflictList == []):
                    self.ph_syncing_to_database()
                    print("\nCopy Successfully!\n")
                    system("PAUSE")
                else:
                    print("The phone record\n")
                    print("     Phone Number | Name | Nickname | Email | Last call datetime")
                    self.print_one_rec(conflictList[0])
                    print("\nhas exist in group {}\n".format(self.group[int(ip6a)]))
                    system("PAUSE")


            if(ip == '7'):
                system("cls")
                while(True):
                    print("Show phone record from...\n")
                    print("1. Current variable record")
                    print("2. Database")
                    print("3. Return to menu")
                    ip1 = str(input("\nInput the number and Enter to continue: ")) + '0'
                    ip1 = ip1[0]
                    if('1' <= ip1 <= '3'):
                        break
                if(ip1 == '3'):
                    continue
                if(ip1 == '1'):
                    fromDatabase = False
                if(ip1 == '2'): 
                    fromDatabase = True
                
                while(True):
                    print("\nChoose the group to show\n")
                    print("1. Family")
                    print("2. Friend")
                    print("3. Junk")
                    print("4. All")
                    print("5. Return to menu")
                    ip1 = str(input("\nInput the number and Enter to continue: ")) + '0'
                    ip1 = ip1[0]
                    if('1' <= ip1 <= '5'):
                        break
                if(ip1 == '5'):
                    continue
                if(ip1 == '4'):
                    grp = -1
                else:
                    grp = int(ip1)

                self.show_phone_rec(grp, fromDatabase)

            if(ip == '8'):
                self.exit_show()
                return 0



    def print_one_rec(self, phRec):
        print("     {} | {} | {} | {} | {}".format(phRec.phoneNo, phRec.name, phRec.nickname, 
                                                        phRec.email, self.time_combine(self.time_split_str(phRec.lastCallDate), 2)))

    def show_phone_rec(self, grp = -1, fromDatabase = False):
        if(fromDatabase):
            recGrpList = self.split_group(self.ph_database_read())
        else:
            recGrpList = []
            recGrpList.append(self.family)
            recGrpList.append(self.friend)
            recGrpList.append(self.junk)

        system("cls")
        if(grp == 1 or grp == -1):
            print("\n{}: ".format(self.group[1]))
            print("     Phone Number | Name | Nickname | Email | Last call datetime")
            for phRec in recGrpList[0]:
                print("     {} | {} | {} | {} | {}".format(phRec.phoneNo, phRec.name, phRec.nickname, 
                                                        phRec.email, self.time_combine(self.time_split_str(phRec.lastCallDate), 2)))
        if(grp == 2 or grp == -1):
            print("\n{}: ".format(self.group[2]))
            print("     Phone Number | Name | Nickname | Email | Last call datetime")
            for phRec in recGrpList[1]:
                print("     {} | {} | {} | {} | {}".format(phRec.phoneNo, phRec.name, phRec.nickname, 
                                                    phRec.email, self.time_combine(self.time_split_str(phRec.lastCallDate), 2)))
        if(grp == 3 or grp == -1):
            print("\n{}: ".format(self.group[3]))
            print("     Phone Number | Name | Nickname | Email | Last call datetime")
            for phRec in recGrpList[2]:
                print("     {} | {} | {} | {} | {}".format(phRec.phoneNo, phRec.name, phRec.nickname, 
                                                    phRec.email, self.time_combine(self.time_split_str(phRec.lastCallDate), 2)))
        
        system("PAUSE")
        
        

    def exit_show(self):
        system("cls")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(" Thank you ")
        print("             for using ")
        print("                         ENG2002 Group7")
        print("                                         Smart Phone Book System!    ")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        system("PAUSE")

def system(command):
        if(command.upper() == "CLS"):
            for i in range(25):
                print()
            return 0
        if(command.upper() == "PAUSE"):
            input("Please input anything to continue...      ")
            return 0


