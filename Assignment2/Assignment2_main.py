#####################################################################################
#   This module is developed by ENG2002-Group7                                   
#   
#   Collaborators: 
#       LIN Ju 21106434D
#       NI Rongheng 21102803D
#       QIN Qijun 21101279D
#   
#   Workshop: https://github.com/ENG2002Gp7Studio/ENG2002_Group7
#####################################################################################

#######################################################################################################################
#   This code is an example to present the application of the User Manage System and PhoneBook System    
#   
#   The whole program is divided into User Manage System(UMS) and PhoneBook System(PB), which are two sets of 
#   databases system. UMS enables the management of user databases. At the same time, the UMS database can be 
#   linked to the PB database, with different users corresponding to different data units in PB. 
# 
#   The two systems are highly independent and can be applied separately to different scenarios and requirements. 
#   Both systems provide external interfaces to different systems, as long as the parameters are provided.  
# 
#   For more information, pleaes read the readme.txt.                                                                           
########################################################################################################################

import os
import sys
import datetime
import phonebook_package.phonebook as pb
import user_management_system.user_management_sys as ums



def main():
    user = ums.UserManageSys()  # User initialisation (Connect to the database and access a certain user)
                                # The specific database address can be passed into the class, 
                                #   and then the system will use this address.
                                # It can also accept UserName and Pwd as parameters. Once checked against the database,
                                #   this class will return the properties of this user
                                # If no parameters are provided, the system will use the default addressing for database.

    # ums.show_user_database(user.uDBRootPath)
    # input()
            
    if(user.userAccess):        # Successful Checking, then entry the user interface
        
        while(True):
                                # Greeting set up to make a more beautiful menu
            timeList = pb.phoneBk.time_split_str(pb.phoneBk, datetime.datetime.now())

            if(0 <= int(timeList[3]) <= 5):
                greeting = "Good morning"
            if(5 < int(timeList[3]) <= 12):
                greeting = "Good morning"
            if(12 < int(timeList[3]) <= 17):
                greeting = "Good afternoon"
            if(17 < int(timeList[3]) <= 23):
                greeting = "Good evening"

            while(True):
                os.system("cls")
                print("**********************************************************************")
                print("*   {}, dear {}  ".format(greeting, user.userInfo.userName))
                print("*                                                                    *")
                print("*   Please Choose the option below:                                  *")
                print("*                                                                    *")
                print("*   1. Enter Phone Book System                                       *")
                print("*   2. Change Password                                               *")
                print("*   3. Log out                                                       *")
                print("*   4. Exit                                                          *")
                print("*                                                                    *")
                print("**********************************************************************")

                ip = str(input("\nInput the number and Enter to continue: "))
                if('1' <= ip <= '4'):
                    break
            
            if(ip == '1'):
                                                    # Set the address for interfacing to the phonebook database   
                pbFilePath = user.uDBRootPath[0] + ':\\PhoneBookSystem\\' + str(user.userInfo.userID) + ".pb"   
                uPhoneBK = pb.phoneBk(pbFilePath)   # Connect to the PB database and assign properties to the PB class
                uPhoneBK.built_in_menu()            # Enter PB menu


            if(ip == '2'):
                os.system("cls")
                print("Please input your original password: \n")
                oriPwd = input()
                t1, t2, pwdCheck, t4 = user.user_check(user.userInfo.userID, oriPwd)    # Check the user and password
                                                                        # Return 0: Access OK, -1: Wrong Pwd, -2: User is not in database, -3: Database path error
                if(pwdCheck == -1):
                    print("\nWrong Password!\n")
                    os.system("PAUSE")
                    continue
                if(pwdCheck == 0):
                    while(True):
                        os.system("cls")
                        print("UserName: {}".format(user.userInfo.userName))
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
                    user.user_database_write(user.userInfo.userName, nd_pwd, True, user.userInfo.userID) # Write new data in database
                    os.system("cls")
                    print("Please input your Password:\n\n" + len(st_pwd) * '*')
                    print("\nPlease input your Password again:\n\n" + len(st_pwd) * '*')
                    print("\nChange password successfully!\n")
                    os.system("PAUSE")

                else:
                    sys.exit("Unknown Error!")  # There may be 2 situations: 
                                                # Database file path is not available; ''
                                                # The database has been tampered with so that the user information cannot be found during the runtime

            if(ip == '3'):
                user.user_log_out() # Log out
                os.system("cls")
                print(">>>>>>>>>>>>>>>>>>>>")
                print("  Log out success!  ")
                print(">>>>>>>>>>>>>>>>>>>>\n")
                os.system("PAUSE")
                user.built_in_menu()
                continue
            if(ip == '4'):
                user.exit_show()    # Exit
                exit(0)

if __name__ == "__main__":
    main()
