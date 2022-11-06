#####################################################################################
#   This is for programming develop and debug only, but not for the final product   
#                                                                                   
#####################################################################################

import phonebook_package.phonebook as pb
import user_management_system.user_management_sys as ums


user = ums.UserManageSys()
if(user.userAccess):

    pbFilePath = user.uDBRootPath + '\\phonebook_database\\' + str(user.userInfo.userID)
    # phoneRec = pb.ph_database_access(pbFilePath)    
    # phonebook = pb(phoneRec)
