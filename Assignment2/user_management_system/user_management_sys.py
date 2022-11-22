#############################################################################################################################
#
# Copyright: ENG2002 Group 7
# Author: QIN Qijun 21101279D
# Discription: User Management System
#
# This module is used to implement user management. It creates a user database for saving usernames, user IDs and passwords, 
#   and provides execution functions for various operations on the database.
# The data is stored in a specific storage format provided by the system, and the data information is encrypted.
# The system also provides external interfaces to directly connect with external databases and applications, 
#   as well as embedding into programs. It has a high degree of independence.
#
#############################################################################################################################

import os
import sys
import datetime

##
# @brief    A class includes userID and userName. Used in UMS
#
class UserInfo:
    def __init__(self, userID, userName):
        self.userID = userID
        self.userName = userName

##
# @brief    The main class of the UMS
#
class UserManageSys:
    
    ##
    # @brief    Initialize the system
    # 
    # @param (str)uDBRootPath   The root path of databse. If no address to pass in, the system will search
    #                           an available root path for the database
    # @param (str)userInfo      Used to receive user information from external sources
    # @param (str)userPwd       Used to receive user password form external sources
    #
    def __init__(self, uDBRootPath = -1, userInfo = -1, userPwd = -1):  
                                                #User system init
        self.userInfo = userInfo    # All the information of user store in the type of (class)userInfo
        self.userDataBase = []      # No use
        self.uDBDisk = -1           # The root disk of the path of the database
        self.uDBRootPath = uDBRootPath  # The root path of database
        self.userAccess = False     # To tell the login status of user
        t1, t2, self.sys_status, t3 = self.sys_init(userPwd)    # To initialize the system
        if(self.sys_status < 0):
            self.uDBRootPath = self.sys_status

    
    ##
    # @brief    Initaialize the system (cont.)
    # The system will access the database, check user with password and return the userInfo + status
    # If no root path of database passes in, the system will search an avialable path for database and use built-in menu
    # If pass in the path of databse without userInfo and pwd, the system will only connect to the databse
    # If pass in the path and userInfo only, the system will just check whether the user exist
    # If pass all parameters, the system will execute login function base on the given databse
    #
    # @param (str)userPwd   Password form external sources.
    #
    # @return
    #   - userID, userName, sys_status, index
    #   -- sys_status = 0: User access; 1: User exist, but no pwd to login; -1: Pwd wrong; -2: User not exist; -3: Database cannot find
    #   -- index: The position line of the user data in database
    #
    # @note You don't need to call this function when you initialize. This proccess will finish automatically when using this class
    #
    def sys_init(self, userPwd = -1):
        
        if(self.uDBRootPath == -1):
            return self.built_in_menu()
        else:
            if(self.file_location_detect() == -3):
                return -3, -3, -3, -3
            if(self.userInfo == -1):
                return -2, -2, -2, -2
            return self.user_check(self.userInfo.userName, userPwd)


    ##
    # @brief    defaul menu
    #
    def built_in_menu(self):

        while(self.uDBRootPath == -1):
            self.file_location_detect()

        while(True):
            os.system("cls")
            print("**********************************************************************")
            print("*   Welcome to use ENG2002 Group7 Smart User Management System!      *")
            print("*   Please Choose the option below:                                  *")
            print("*                                                                    *")
            print("*   1. Login-in                                                      *")
            print("*   2. Sign-up                                                       *")
            print("*   3. Exit                                                          *")
            print("*                                                                    *")
            print("**********************************************************************")

            ip = str(input("\nInput the number and Enter to continue: ")) + '0'
            ip = ip[0]
            if('1' <= ip <= '3'):
                break

        if(ip == "1"):
            
            while(True):
                os.system("cls")
                ipUserID = input("Please input user NAME or ID: ")  
                userID, userName, userStatus, uIndex = self.user_check(ipUserID)    
                                                                                # -3: File Path not avialable; -2: User not exist; -1: Password Error; 
                                                                                # 0: Access; 1: User exist
                                                                                # -4: Temporary no use
                if(userStatus == -2):       # User did not exist, entry sign up menu
                    while(True):
                        os.system("cls")
                        print("**********************************************************************")
                        print("Dear {}, ".format(ipUserID))
                        print("You haven't an account yet. Do you want to")
                        print("1. Create an Account With User Name \"{}\"".format(ipUserID))
                        print("2. Change User")
                        print("3. Exit")
                        print("**********************************************************************")
                        ip = str(input("Input the number and Enter to continue: ")) + '0'
                        ip = ip[0]
                        if('1' <= ip <= '3'):
                            break

                    if(ip == '1'):
                        if(not self.user_name_check(ipUserID)):
                            print("\nYour user name is too short or too long (2~32 characters)\nPlease Change User!\n")
                            os.system("PAUSE")
                            continue

                        while(True):                                # Input new pass word and check it
                            os.system("cls")
                            print("UserName: {}".format(ipUserID))
                            print("Please input your Password:\n")
                            st_pwd = input()
                            os.system("cls")
                            print("Please input your Password:\n\n" + len(st_pwd) * '*')
                            print("\nPlease input your Password again:\n")
                            nd_pwd = input()
                            print(" ")

                            if(st_pwd != nd_pwd):
                                print("Two passwords are different, please input again!\n")
                                os.system("PAUSE")
                            else:
                                break
                        
                        self.user_database_write(ipUserID, nd_pwd)                          # Write in database
                        userID, userName, userStatus, uIndex = self.user_check(ipUserID)    # Re-check again
                        pwdLen = len(nd_pwd)
                        nd_pwd = 0
                        self.userInfo = UserInfo(userID, userName)      # Save in userInfo
                        self.userAccess = True

                        self.sign_up_show(pwdLen, userID, userName)     # Display
                        return userID, userName, userStatus, uIndex


                    if(ip == '2'):
                        continue

                    if(ip == '3'):
                        self.exit_show()
                        sys.exit(0)

                if(userStatus == 1):    # Find user and ask user to input pwd

                    for i in range(5, -1, -1):
                        
                        os.system("cls")
                        print("UserName: {}".format(ipUserID))
                        ipUserPwd = input("Please input password: ")
                        userID, userName, userStatus, uIndex = self.user_check(ipUserID, ipUserPwd) # Check pwd
                        pwdLen = len(ipUserPwd)
                        ipUserPwd = 0
                        if(userStatus == 0):    # pwd correct
                            self.userInfo = UserInfo(userID, userName)
                            self.userAccess = True
                            self.log_in_show(pwdLen, userID, userName)
                            return userID, userName, 0, uIndex
                        else:
                            print("\nPassword Error! You have {} time(s) left to try.\n".format(i))
                            os.system("PAUSE")

                    os.system("cls")
                    print("Input wrong password too many times! Please try again later!")
                    os.system("PAUSE")
                    sys.exit(0)

                if(userStatus == -3):       # Database cannot connect
                    return -3, -3, -3, -3

        if(ip == "2"):  # Sign up. The same as ip == '1'

            while(True):
               
                while(True):
                    os.system("cls")
                    ipUserName = input("Please input your user NAME (2~32 Characters): ")  
                    if(self.user_name_check(ipUserName)):
                        break
                    else:
                        print("\nYour user name is too short or too long (2~32 characters)\nPlease re-input!")

                userID, userName, userStatus, uIndex = self.user_check(ipUserName)    

                if(userStatus == -3):
                    return -3, -3, -3, -3
                if(userStatus == 1):
                    print("\nThis user NAME has been exist. Please try another NAME.\n")
                    os.system("PAUSE")
                    continue
                else:
                    break

            while(True):
                os.system("cls")
                print("UserName: {}".format(ipUserName))
                print("Please input your Password:\n")
                st_pwd = input()
                os.system("cls")
                print("Please input your Password:\n\n" + len(st_pwd) * '*')
                print("\nPlease input your Password again:\n")
                nd_pwd = input()
                print("\n")

                if(st_pwd != nd_pwd):
                    print("Two passwords are different, please input again!")
                    os.system("PAUSE")
                else:
                    break
                    
            self.user_database_write(ipUserName, nd_pwd)
            userID, userName, userStatus, uIndex = self.user_check(ipUserName)
            pwdLen = len(nd_pwd)
            nd_pwd = 0

            self.userInfo = UserInfo(userID, userName)
            self.userAccess = True
            self.sign_up_show(pwdLen, userID, userName)

            return userID, userName, userStatus, uIndex

        if(ip == "3"):
            os.system("cls")
            self.exit_show()
            sys.exit(0)


    ##
    # @brief    Display sample
    #
    def log_in_show(self, pwdLen, userID, userName):
        os.system("cls")
        print("UserName: {}".format(userName))
        print("Please input password: " + pwdLen * '*')
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("                     Login in success!                         ")
        print("---------------------------------------------------------------")
        print("Login in Date: \t{}".format(datetime.datetime.now()))
        print("User ID: \t{}".format(userID))
        print("User Name: \t{}".format(userName))
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        os.system("PAUSE")
        os.system("CLS")

    def sign_up_show(self, pwdLen, userID, userName):
        os.system("cls")
        print("UserName: {}".format(userName))
        print("Please input password: " + pwdLen * '*')
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("                         Sign up success!                        ")
        print("-----------------------------------------------------------------")
        print("Sign Up Date: \t{}".format(datetime.datetime.fromtimestamp(int(userID[len(userID) - 10 : len(userID)]))))
        print("User ID: \t{}".format(userID))
        print("User Name: \t{}".format(userName))
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        os.system("PAUSE")
        os.system("CLS")

    def exit_show(self):
        os.system("cls")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(" Thank you ")
        print("             for using ")
        print("                         ENG2002 Group7")
        print("                                         Smart User Management System! ")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        os.system("PAUSE")


    ##
    # @brief    Sign up function
    # This function is provided for external call. 
    # It is no need to call if using built-in menu.
    # 
    # @param (str)ipUserName    The new user name for sign up
    # @param (str)userPwd       The new pwd for sign up
    # @param (str)ipUserID      The new user ID for sign up. If False, the ID will generate automatically
    #
    # @note Need to set (phoneBook).uDBRootPath before use this function
    # 
    # @return
    #   - userID, userName, sys_status, index
    #   -- Discription is at line 64
    #  
    def user_sign_up(self, ipUserName, userPwd, ipUserID = False):

        self.user_log_out()                     
        userID, userName, userSataus, uIndex = self.user_check(ipUserName)  # Check whether the user has exist
        if(userSataus == 1):                        # If exist, then return the exist user
            self.sys_status = 1
            return userID, userName, 1, uIndex
        if(userSataus == -2):                       # If not exist, then write in new user data and return the this user
            a = self.user_database_write(ipUserName, userPwd, False, ipUserID)
            self.userInfo = UserInfo(ipUserID, ipUserName)
            self.userAccess = True
            self.sys_status = 0
            return userName, userPwd, a, uIndex
        

    ##
    # @brief    Login function
    # This function is provided for external call. 
    # It is no need to call if using built-in menu.
    #
    # @param (str)ipUserName    The new user name for sign up
    # @param (str)userPwd       The new pwd for sign up
    #
    # @note Need to set (phoneBook).uDBRootPath before use this function
    #
    # @return
    #   - userID, userName, sys_status, index
    #   -- Discription is at line 64
    #  
    def user_log_in(self, ipUserName, userPwd):
        userID, userName, userSataus, uIndex = self.user_check(ipUserName, userPwd) # Check whether the pwd is correct
        if(userSataus == 0):                            # If correct, then login
            self.userInfo = UserInfo(userID, userName)
            self.userAccess = True
            self.sys_status = 0
            return userID, userName, userSataus, uIndex
        else:                                           # If wrong, return the wrong value
            self.sys_status = userSataus
            return userID, userName, userSataus, uIndex


    ##
    # @brief    Logout function
    # This function is provided for external call. 
    # It is no need to call if using built-in menu.
    #
    # @return 0 = success
    #
    def user_log_out(self):
        self.userInfo = -1
        self.userAccess = False
        self.sys_status = -2
        return 0


    ##
    # @brief    User delete function
    # This function is provided for external call. 
    # It is no need to call if using built-in menu.
    #
    # Temporary undeveloped
    #
    def user_del(self, ipUserName, userPwd):
        userID, userName, userSataus, uIndex = self.user_check(ipUserName, userPwd)
        if(userSataus == 0):
            pass


    ##
    # @brief    Check whether user 1. is exist; 2. pwd is correct
    #
    # @param (str)userID    Pass in user name or user ID
    # @param (str)userPwd   User pwd. If no passing in, the function will check whether the user is exist only.
    #                       If passing in a pwd, the function will also check the pwd.
    #
    # @return 
    #   - userID, userName, sys_status, index
    #   -- sys_status = 0: User access; 1: User exist, but no pwd to login; -1: Pwd wrong; -2: User not exist; -3: Database cannot find
    #   -- index: The position line of the user data in database 
    #
    def user_check(self, userID, userPwd = -1):
        
        userAll = self.user_database_read()     # Get all database user
        if(userPwd == -1):          # No pwd param pass in, check whether user is exist only

            if(userAll == -2):              # No user
                return -2, -2, -2, -2

            if(userAll == -3):              # Database cannot connect
                return -3, -3, -3, -3
            
            uIndex = 0 # To record the position line of the user
            for user in userAll:
                if(self.ums_encryption(userID) in user):
                    return self.ums_decryption(user[0]), self.ums_decryption(user[1]), 1, uIndex
                uIndex += 1

            return -2, -2, -2, -2

        else:                       # pwd pass in, also check whether the pwd is correct

            if(userAll == -2):
                return -2, -2, -2, -2

            if(userAll == -3):
                return -3, -3, -3, -3

            haveUser = False
            for a_user in userAll:
                if(self.ums_encryption(userID) in a_user):
                    haveUser = True
            if(not haveUser):
                return -2, -2, -2, -2
            
            for i in range(0, len(userAll)):

                if(userAll[i][0] == self.ums_encryption(userID) or userAll[i][1] == self.ums_encryption(userID)):
                    if(userAll[i][2] == self.ums_encryption(userPwd)):
                        return self.ums_decryption(userAll[i][0]), self.ums_decryption(userAll[i][1]), 0, i
                    else:
                        return self.ums_decryption(userAll[i][0]), self.ums_decryption(userAll[i][1]), -1, i


    ##
    # @brief    Read user data from database
    #
    # @return   A list of user data list
    #   - (list)userAll = [(list)user_1, (list)user_2, ...] = [[(str)userID, (str)userName, (str)Pwd], ...]
    #
    # @par
    # @code
    #       userAll = user_database_read()
    #       user2_userName = userAll[1][1]
    # @encode
    #
    def user_database_read(self):
                                                                         # ID + Name + Pwd
        if(self.uDBRootPath == -1 or self.file_location_detect() != 0):
            return -3

        userFile = open(self.uDBRootPath + "\\userDataBase.ums", 'r', encoding='utf-8')

        if(len(userFile.readline()) == 0):
            userFile.close()
            return -2

        userFile.seek(0)

        userAll = []
        while(True):

            rd_temp = userFile.readline()

            if(rd_temp == ""):
                break

            user_temp = rd_temp.split('*')
            user_temp[2] = user_temp[2][0:len(user_temp[2]) - 1]

            userAll.append(user_temp)
        
        userFile.close()

        return userAll


    ##
    # @brief    Write user data to database
    #
    # @param (str)userName   User name to write in database
    # @param (str)userPwd    Password name to write in database
    # @param (int)wIndex     Overwrite the specified line in the database
    #                   If no param passing in, the data will append at the file tail
    #                   If param passes in, the data will overwrite in the wIndex line
    # @param (str)userID     User ID to write in database
    #
    # @return   0 = Write in success
    #
    # @par
    # @code
    #       userAll = user_database_read()
    #       user2_userName = userAll[1][1]
    # @encode
    #
    def user_database_write(self, userName, userPwd, wIndex = False, userID = False):

        if(wIndex == False or wIndex <= 0):

            if(userID == False):
                userID = self.user_id_create(userName)

            userFile = open(self.uDBRootPath + "\\userDataBase.ums", 'a', encoding='utf-8')
            w_temp = self.ums_encryption(userID) + '*' + self.ums_encryption(userName) + '*' + self.ums_encryption(userPwd)
            userFile.write(w_temp + '\n')
            userFile.close()    

            return 0

        else:

            userFile = open(self.uDBRootPath + "\\userDataBase.ums", 'r', encoding='utf-8')
            userAll = userFile.readlines()
            userFile.close()

            for i in range(0, len(userAll)):
                
                user_temp = userAll[i].split('*')
                if(user_temp[1] == self.ums_encryption(userName)):
                    userAll[i] = user_temp[0] + '*' + self.ums_encryption(userName) + '*' + self.ums_encryption(userPwd) + '\n'
                    break
            
            userAll[wIndex][0] = userID
            userAll[wIndex][1] = userName
            userAll[wIndex][2] = userPwd

            userFile = open(self.uDBRootPath + "\\userDataBase.ums", 'w', encoding='utf-8')
            for i in range(0, len(userAll)):

                userAll = userFile.write(userAll[i])
                
            userFile.close()
            return 0

            
    ##
    # @brief    Built up database
    # This function is provided for external call. 
    # It is no need to call if using built-in menu.
    # 
    # @param (str)uDBRootPath   The root path of database.
    # @param (list)userImport   A list of (class)UserInfo.
    # @param (list)Pwd          A list of (str)password. Needs to correspond to the (list)userImport
    #
    # @return   0: Database built up success; -1: Database built up failed
    #  
    def database_built_up(self, uDBRootPath, userImport:list = -1, Pwd:list = -1):

        if(not os.path.exists(uDBRootPath)):
            os.mkdir(uDBRootPath)
        f_temp = open(uDBRootPath + "\\sysInit.check", "w")
        f_temp.close()
        f_temp = open(uDBRootPath + "\\userDataBase.ums", 'w')
        f_temp.close()

        if(self.isfile(uDBRootPath + "\\sysInit.check")):
            self.uDBDisk = uDBRootPath[0]
            self.uDBRootPath = uDBRootPath
            if(userImport != -1):
                for i in range(0, len(userImport)):
                    self.user_database_write(userImport[i].userName, Pwd[i], False, userImport[i].userID)
            self.user_log_out()
            return 0
        else:
            self.uDBDisk = -1
            self.uDBRootPath = -1
            return -1

   
    ##
    # @brief    Check or search for file paths
    # This function is to connect to the database
    # If no given root path, i.e. (class)UserManageSys.uDBRootPath = -1, the system will ask user to select an available 
    #   disk and create database files. Each run will automatically look for the files created.
    # If given root path, this function will check whether this path is available.
    # This function will run once when initializing the UserManagementSys class
    #
    # @return   
    #   - 0: Database access; -3: Database cannot find or create
    #  
    def file_location_detect(self):

        locationAccess = False
        
        if(self.uDBRootPath != -1):
            if(self.isfile(self.uDBRootPath + "\\sysInit.Check") and
               self.isfile(self.uDBRootPath + "\\userDataBase.ums")):
               self.uDBDisk = self.uDBRootPath[0]
               locationAccess = True
               return 0
            else:
               return -3
                                 
        
        fileDisk = 'Z'                                              # Search from disk Z~A
        while(fileDisk >= 'A'):                                     
            rootPathTemp = fileDisk + ":\\UserManagementSystem"
            if(self.isfile(rootPathTemp + "\\sysInit.check") and 
                self.isfile(rootPathTemp + "\\userDataBase.ums")):
                locationAccess = True
                break
            if(self.isfile(rootPathTemp + "\\userDataBase.ums")):
                f_temp = open(rootPathTemp + "\\sysInit.check", "w")
                f_temp.close()
                locationAccess = True
                break
            if(self.isfile(rootPathTemp + "\\sysInit.check")):
                f_temp = open(rootPathTemp + "\\userDataBase.ums", "w")
                f_temp.close()
                self.uDBDisk = fileDisk
                self.uDBRootPath = rootPathTemp
                return 0

            fileDisk = chr(ord(fileDisk) - 1)
        
        if(locationAccess):                     # If find the database, then accesss
            self.uDBDisk = fileDisk
            self.uDBRootPath = rootPathTemp
        else:                                   # Ask user to input the disk for store the database
            fileDisk = '0'
            print("Is the first time to use UserManagementSystem(UMS)?")
            print("Please input an accessible Disk(A~Z) for storage the UMS Data")
            print("(NOTE: If the Disk cannot access, the software may crash!)")
            while(not('A' <= fileDisk <= 'Z' or 'a' <= fileDisk <= 'z')):
                fileDisk = input("Disk(Enter '0' to EXIT): ")
                if(fileDisk == '0'):
                    sys.exit(0)
                if(not('A' <= fileDisk <= 'Z' or 'a' <= fileDisk <= 'z')):
                    print("Please input an accessible Disk(A~Z) for storage the UMS Data")

            if(self.database_built_up(fileDisk + ":\\UserManagementSystem")):
                print("System Error: 001\nFile cannot be created!")
                return -3
            else:
                return 0

    ##
    # @brief    Check whether the file path is exist
    #
    # @param    filePath    file path
    #
    def isfile(self, filePath):
        try:
            t_try = open(filePath, 'r')
        except IOError:
            return False
        t_try.close()
        return True

    ##
    # @brief    Functions for name checking, automatic ID generation for easier editing later
    #
    def user_name_check(self, userName):
        if(2 <= len(userName) <= 32):
            return True
        else:
            return False

    def user_id_create(self, userName):
        userID = "0" * 10
        for i in range(0, 10):
            userID = userID[0: i] + str(ord(userName[i % len(userName) - 1]) % 10) + userID[i: len(userID)]
        userID += str(int(datetime.datetime.timestamp(datetime.datetime.now())))
        return userID
    
    ##
    # @brief    A very easy encryption and decryption algorithm
    # This function is to simulate the process of encryption and decryption.
    #
    # @param    (str)ip     Source string
    #
    # @return   (str)op     Proccessed string
    #
    def ums_encryption(self, ip):

        op = ""
        for i in range(0, len(ip)):
            op += chr(ord(ip[i]) + 35409)

        return op

    def ums_decryption(self, ip):

        op = ""
        for i in range(0, len(ip)):
            op += chr(ord(ip[i]) - 35409)

        return op



##
# @brief    To show the data of the database
#
# @param    fileRootPath    The root path of the database
#
# @note     For development and debug only
#
def show_user_database(fileRootPath):
    if(UserManageSys.isfile(fileRootPath + "\\userDataBase.ums")):
        f = open(fileRootPath + "\\userDataBase.ums", 'r', encoding='utf-8')
        while(True):
            user_sour = f.readline()
            if(user_sour == ""):
                return 0
            user_enc = user_sour.split('*')
            user_enc[2] = user_enc[2][0:len(user_enc[2]) - 1]
            print(UserManageSys.ums_decryption(UserManageSys, user_enc[0]) + "\t\t||\t\t" + 
                    UserManageSys.ums_decryption(UserManageSys, user_enc[1]) + "\t\t||\t\t" + 
                    UserManageSys.ums_decryption(UserManageSys, user_enc[2]))
    return -1

