from check_if_exist import get_date, get_path_exists,HEADER,DEBUG, get_checksum



class DirCheck(object):
    
    DIRECTORY=["etc", "home", "media", "mnt" , "root", "sbin", "tmp", "usr", "/usr/bin", "var"]

    def check_dir(self):

        # if get_path_exists(f"report/system_info_{get_date()}.xml"):
        #     print("File exists")
        # else:
        for DIR in self.DIRECTORY:

            HEADER("[INFO]", f"{DIR}")

            if get_path_exists(f"/{DIR}"):
                path = f"/{DIR}"
                DEBUG("\t[INFO]", get_checksum(path))
            else:
                DEBUG("\t[INFO]", "FILE DOESN'T exists")



DirCheck().check_dir()




