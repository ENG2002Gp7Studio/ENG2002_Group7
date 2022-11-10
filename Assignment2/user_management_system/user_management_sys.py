
import os
import sys
import datetime

class UserInfo:
    def __init__(self, userID, userName):
        self.userID = userID
        self.userName = userName


class UserManageSys:

    def __init__(self, uDBRootPath = -1, userInfo = -1, userPwd = -1):  
                                                #User system init
        self.userInfo = userInfo
        self.userDataBase = []
        self.uDBDisk = -1
        self.uDBRootPath = uDBRootPath
        self.userAccess = False
        t1, t2, self.sys_status, t3 = self.sys_init(userPwd)

    
    def sys_init(self, userPwd = -1):
        
        if(self.uDBRootPath == -1):
            return self.built_in_menu()
        else:
            if(self.file_location_detect() == -3):
                return -3, -3, -3, -3
            if(self.userInfo == -1):
                return -2, -2, -2, -2
            return self.user_check(self.userInfo.userName, userPwd)



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

            ip = str(input("\nInput the number and Enter to continue: "))
            if('1' <= ip <= '3'):
                break

        if(ip == "1"):
            
            while(True):
                os.system("cls")
                ipUserID = input("Please input user NAME or ID: ")  
                userID, userName, userStatus, uIndex = self.user_check(ipUserID)    
                                                                                # -3: File Path not avialable; -2: User not exist; -1: Password Error; 
                                                                                # 0: Access; 1: User exist
                if(userStatus == -2):    
                    while(True):
                        os.system("cls")
                        print("**********************************************************************")
                        print("Dear {}, ".format(ipUserID))
                        print("You haven't an account yet. Do you want to")
                        print("1. Create an Account With User Name \"{}\"".format(ipUserID))
                        print("2. Change User")
                        print("3. Exit")
                        print("**********************************************************************")
                        ip = str(input("Input the number and Enter to continue: "))
                        if('1' <= ip <= '3'):
                            break

                    if(ip == '1'):
                        if(not self.user_name_check(ipUserID)):
                            print("\nYour user name is too short or too long (2~32 characters)\nPlease Change User!\n")
                            os.system("PAUSE")
                            continue

                        while(True):
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
                        
                        self.user_database_write(ipUserID, nd_pwd)
                        userID, userName, userStatus, uIndex = self.user_check(ipUserID)
                        pwdLen = len(nd_pwd)
                        nd_pwd = 0
                        self.userInfo = UserInfo(userID, userName)
                        self.userAccess = True

                        self.sign_up_show(pwdLen, userID, userName)
                        return userID, userName, userStatus, uIndex


                    if(ip == '2'):
                        continue

                    if(ip == '3'):
                        self.exit_show()
                        exit(0)

                if(userStatus == 1):

                    for i in range(5, -1, -1):
                        
                        os.system("cls")
                        print("UserName: {}".format(ipUserID))
                        ipUserPwd = input("Please input password: ")
                        userID, userName, userStatus, uIndex = self.user_check(ipUserID, ipUserPwd)
                        pwdLen = len(ipUserPwd)
                        ipUserPwd = 0
                        if(userStatus == 0):
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
                    exit(0)

                if(userStatus == -3):
                    return -3, -3, -3, -3

        if(ip == "2"):

            while(True):
               
                while(True):
                    os.system("cls")
                    ipUserName = input("Please input your user NAME (2~32 Characters): ")  
                    if(self.user_name_check(ipUserName)):
                        break
                    else:
                        print("\nYour user name is too short or too long (2~32 characters)\nPlease re-input!")

                userID, userName, userStatus, uIndex= self.user_check(ipUserName)    

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
            exit(0)


    def log_in_show(self, pwdLen, userID, userName):
        os.system("cls")
        print("UserName: {}".format(userName))
        print("Please input password: " + pwdLen * '*')
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("                     Login in success!                         ")
        print("---------------------------------------------------------------")
        print("Login in Date: {}".format(datetime.datetime.now()))
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



    def user_sign_up(self, ipUserName, userPwd, ipUserID = False):

        self.user_log_out()
        userID, userName, userSataus, uIndex = self.user_check(ipUserName) 
        if(userSataus == 1):
            self.sys_status = -4
            return -4, -4, -4, -4
        if(userSataus == -2):
            a = self.user_database_write(ipUserName, userPwd, False, ipUserID)
            self.userInfo = UserInfo(ipUserID, ipUserName)
            self.userAccess = True
            self.sys_status = 0
            return userName, userPwd, a, uIndex
        
    def user_log_in(self, ipUserName, userPwd):
        userID, userName, userSataus, uIndex = self.user_check(ipUserName, userPwd)
        if(userSataus == 0):
            self.userInfo = UserInfo(userID, userName)
            self.userAccess = True
            self.sys_status = 0
            return userID, userName, userSataus, uIndex
        else:
            self.sys_status = userSataus
            return userID, userName, userSataus, uIndex

    def user_log_out(self):
        self.userInfo = -1
        self.userAccess = False
        self.sys_status = -2
        return 0

    def user_del(self, ipUserName, userPwd):
        userID, userName, userSataus, uIndex = self.user_check(ipUserName, userPwd)
        if(userSataus == 0):
            pass




    def user_check(self, userID, userPwd = -1):
        
        userAll = self.user_database_read()
        if(userPwd == -1):

            if(userAll == -2):
                return -2, -2, -2, -2

            if(userAll == -3):
                return -3, -3, -3, -3
            
            uIndex = 0
            for user in userAll:
                if(self.ums_encryption(userID) in user):
                    return self.ums_decryption(user[0]), self.ums_decryption(user[1]), 1, uIndex
                uIndex += 1

            return -2, -2, -2, -2

        else:

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


    def user_database_write(self, userName, userPwd, ins = False, userID = False):

        if(ins == False or ins <= 0):

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
            
            userFile = open(self.uDBRootPath + "\\userDataBase.ums", 'w', encoding='utf-8')
            for i in range(0, len(userAll)):

                userAll = userFile.write(userAll[i])
                
            userFile.close()
            return 0

            


    def database_built_up(self, uDBRootPath, userImport:list = -1, Pwd:list = -1):

        if(not os.path.exists(uDBRootPath)):
            os.mkdir(uDBRootPath)
        f_temp = open(uDBRootPath + "\\sysInit.check", "w")
        f_temp.close()
        f_temp = open(uDBRootPath + "\\userDataBase.ums", 'w')
        f_temp.close()

        if(os.path.isfile(uDBRootPath + "\\sysInit.check")):
            self.uDBDisk = uDBRootPath[0]
            self.uDBRootPath = uDBRootPath
            if(userImport != -1):
                for i in range(0, len(userImport)):
                    self.user_database_write(userImport[i].userName, Pwd[i], False, userImport[i].userID)
            self.user_log_out()
        else:
            self.uDBDisk = -1
            self.uDBRootPath = -1
            return -1

   

    def file_location_detect(self):

        locationAccess = False
        
        if(self.uDBRootPath != -1):
            if(os.path.isfile(self.uDBRootPath + "\\sysInit.Check") and
               os.path.isfile(self.uDBRootPath + "\\userDataBase.ums")):
               self.uDBDisk = self.uDBRootPath[0]
               locationAccess = True
               return 0
            else:
               return -3
                                 
        
        fileDisk = 'Z'
        while(fileDisk >= 'A'):
            rootPathTemp = fileDisk + ":\\UserManagementSystem"
            if(os.path.isfile(rootPathTemp + "\\sysInit.check") and 
                os.path.isfile(rootPathTemp + "\\userDataBase.ums")):
                locationAccess = True
                break
            if(os.path.isfile(rootPathTemp + "\\userDataBase.ums")):
                f_temp = open(rootPathTemp + "\\sysInit.check", "w")
                f_temp.close()
                locationAccess = True
                break
            if(os.path.isfile(rootPathTemp + "\\sysInit.check")):
                f_temp = open(rootPathTemp + "\\userDataBase.ums", "w")
                f_temp.close()
                self.uDBDisk = fileDisk
                self.uDBRootPath = rootPathTemp
                return 0

            fileDisk = chr(ord(fileDisk) - 1)
        
        if(locationAccess):
            self.uDBDisk = fileDisk
            self.uDBRootPath = rootPathTemp
        else:
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




def show_user_database(fileRootPath):
    if(os.path.isfile(fileRootPath + "\\userDataBase.ums")):
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
    return 0

