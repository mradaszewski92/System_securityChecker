from auxiliary_functions import get_date, get_path_exists, header, debug, get_checksum

class CheckDir(object):
    DIRECTORY = ["etc", "home", "media", "mnt", "root", "sbin", "tmp", "usr", "/usr/bin", "var"]

    def check_dir(self):

        # if get_path_exists(f"report/system_info_{get_date()}.xml"):
        #     print("File exists")
        # else:
        for DIR in self.DIRECTORY:

            header("[INFO]", f"{DIR}")

            if get_path_exists(f"/{DIR}"):
                path = f"/{DIR}"
                debug("\t[INFO]", get_checksum(path))
            else:
                debug("\t[INFO]", "FILE DOESN'T exists")

class HiddenFile(object):pass

