#####################################################################################
#   This is for programming develop and debug only, but not for the final product   
#                                                                                   
#####################################################################################

import datetime
import phonebook_package.phonebook as pb
import user_management_system.user_management_sys as ums



def main():
    user = ums.UserManageSys()
    phR = [pb.phoneRec("64216528", 1, "QIN Qijun", "QuintinUmi", "qqj030212@gmail.com", str(datetime.datetime.now())),
            pb.phoneRec("19877555671", 2, "QQJ", "QTN", "qqj030212@163.com", str(datetime.datetime.now())), 
            pb.phoneRec("13207758249", 1, "Wu Fang", "Lao Ma", "wufang0668@163.com", str(datetime.datetime.now()))]
    if(user.userAccess):
        
        pbFilePath = user.uDBRootPath[0] + ':\\PhoneBookSystem\\' + str(user.userInfo.userID) + ".pb"
        uPhoneRec = pb.phoneBk(pbFilePath, phR)    
        uPhoneRec.built_in_menu()

if __name__ == "__main__":
    main()
