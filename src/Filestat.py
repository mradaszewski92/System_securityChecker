from auxiliary_functions import get_date, get_path_exists, header, debug, get_checksum
import subprocess
import json

class Filestat(object):
    __file_detail_dict = {}
    __file_detail_list = []
    __file_name = ""
    __file_type = ""
    __id_of_owner = ""
    __group_of_owner = ""
    __user_of_owner = ""
    __access_right = ""
    __mount_point = ""
    __hard_links = ""
    __total_size = ""
    __last_access = ""
    __last_modification = ""
    __last_status_change = ""

    def collectData_singleFileDetails(self, file_path: str):
        """ Method return a"""
        tmp_arr = []
        self.__file_name = subprocess.run("stat -c %n /{}".format(file_path), shell=True, capture_output=True,
                                          universal_newlines=True)  # -file name
        self.__file_type = subprocess.run("stat -c %F /{}".format(file_path), shell=True, capture_output=True,
                                          universal_newlines=True)  # -file type
        self.__id_of_owner = subprocess.run("stat -c %u /{}".format(file_path), shell=True, capture_output=True,
                                            universal_newlines=True)  # -user ID of owner
        self.__group_of_owner = subprocess.run("stat -c %G /{}".format(file_path), shell=True, capture_output=True,
                                               universal_newlines=True)  # -group name of owner
        self.__user_of_owner = subprocess.run("stat -c %U /{}".format(file_path), shell=True, capture_output=True,
                                              universal_newlines=True)  # -user name of owner
        self.__access_right = subprocess.run("stat -c %A /{}".format(file_path), shell=True, capture_output=True,
                                             universal_newlines=True)  # -access rights in human readable form
        self.__mount_point = subprocess.run("stat -c %m /{}".format(file_path), shell=True, capture_output=True,
                                            universal_newlines=True)  # -mount point
        self.__hard_links = subprocess.run("stat -c %h /{}".format(file_path), shell=True, capture_output=True,
                                           universal_newlines=True)  # -number of hard links
        self.__total_size = subprocess.run("du -shb /{} ".format(file_path) + "| awk '{print $1}'", shell=True,
                                           capture_output=True,
                                           universal_newlines=True)  # -total size, in bytes

        self.__last_access = subprocess.run("stat -c %x /{} ".format(file_path), shell=True,
                                            capture_output=True,
                                            universal_newlines=True)  # -total size, in bytes
        self.__last_modification = subprocess.run("stat -c %y /{} ".format(file_path), shell=True,
                                                  capture_output=True,
                                                  universal_newlines=True)  # -total size, in bytes
        self.__last_status_change = subprocess.run("stat -c %z /{} ".format(file_path), shell=True,
                                                   capture_output=True,
                                                   universal_newlines=True)  # -total size, in bytes

        tmp_arr.append([("file_name", self.__file_name.stdout.strip("\n")),
                        ("file_type", self.__file_type.stdout.strip("\n")),
                        ("id_of_owner", self.__id_of_owner.stdout.strip("\n")),
                        ("group_of_owner", self.__group_of_owner.stdout.strip("\n")),
                        ("user_of_owner", self.__user_of_owner.stdout.strip("\n")),
                        ("access_right", self.__access_right.stdout.strip("\n")),
                        ("mount_point", self.__mount_point.stdout.strip("\n")),
                        ("hard_links", self.__hard_links.stdout.strip("\n")),
                        ("last_access", self.__last_access.stdout.strip("\n")),
                        ("last_modification", self.__last_modification.stdout.strip("\n")),
                        ("last_status_change", self.__last_status_change.stdout.strip("\n")),
                        ("total_size", self.__total_size.stdout.strip("\n"))
                        ]
                       )
        self.__file_detail_dict['file_details'] = tmp_arr
        self.__file_detail_list = tmp_arr

    def collectData_multipleFileDetails(self, files_path: list):
        """ Method return a"""
        tmp_arr = []
        for file in files_path:
            self.__file_name = subprocess.run("stat -c %n /{}".format(file), shell=True, capture_output=True,
                                              universal_newlines=True)  # -file name
            self.__file_type = subprocess.run("stat -c %F /{}".format(file), shell=True, capture_output=True,
                                              universal_newlines=True)  # -file type
            self.__id_of_owner = subprocess.run("stat -c %u /{}".format(file), shell=True, capture_output=True,
                                                universal_newlines=True)  # -user ID of owner
            self.__group_of_owner = subprocess.run("stat -c %G /{}".format(file), shell=True, capture_output=True,
                                                   universal_newlines=True)  # -group name of owner
            self.__user_of_owner = subprocess.run("stat -c %U /{}".format(file), shell=True, capture_output=True,
                                                  universal_newlines=True)  # -user name of owner
            self.__access_right = subprocess.run("stat -c %A /{}".format(file), shell=True, capture_output=True,
                                                 universal_newlines=True)  # -access rights in human readable form
            self.__mount_point = subprocess.run("stat -c %m /{}".format(file), shell=True, capture_output=True,
                                                universal_newlines=True)  # -mount point
            self.__hard_links = subprocess.run("stat -c %h /{}".format(file), shell=True, capture_output=True,
                                               universal_newlines=True)  # -number of hard links
            self.__total_size = subprocess.run("du -shb /{} ".format(file) + "| awk '{print $1}'", shell=True,
                                               capture_output=True,
                                               universal_newlines=True)  # -total size, in bytes

            self.__last_access = subprocess.run("stat -c %x /{} ".format(file), shell=True,
                                                capture_output=True,
                                                universal_newlines=True)  # -total size, in bytes
            self.__last_modification = subprocess.run("stat -c %y /{} ".format(file), shell=True,
                                                      capture_output=True,
                                                      universal_newlines=True)  # -total size, in bytes
            self.__last_status_change = subprocess.run("stat -c %z /{} ".format(file), shell=True,
                                                       capture_output=True,
                                                       universal_newlines=True)  # -total size, in bytes

            tmp_arr.append([("file_name", self.__file_name.stdout.strip("\n")),
                            ("file_type", self.__file_type.stdout.strip("\n")),
                            ("id_of_owner", self.__id_of_owner.stdout.strip("\n")),
                            ("group_of_owner", self.__group_of_owner.stdout.strip("\n")),
                            ("user_of_owner", self.__user_of_owner.stdout.strip("\n")),
                            ("access_right", self.__access_right.stdout.strip("\n")),
                            ("mount_point", self.__mount_point.stdout.strip("\n")),
                            ("hard_links", self.__hard_links.stdout.strip("\n")),
                            ("last_access", self.__last_access.stdout.strip("\n")),
                            ("last_modification", self.__last_modification.stdout.strip("\n")),
                            ("last_status_change", self.__last_status_change.stdout.strip("\n")),
                            ("total_size", self.__total_size.stdout.strip("\n"))
                            ])

        self.__file_detail_dict['file_details'] = tmp_arr
        self.__file_detail_list = tmp_arr

    def get_files_detail_dict(self):
        return self.__file_detail_dict

    def get_files_detail_list(self):
        return self.__file_detail_list

    def get_files_detail_json(self):
        return json.dumps(self.__file_detail_dict)

    def get_file_name(self):
        return self.__file_name.stdout

    def get_file_type(self):
        return self.__file_type.stdout

    def get_id_of_owner(self):
        return self.__id_of_owner.stdout

    def get_group_of_owner(self):
        return self.__group_of_owner.stdout

    def get_user_of_owner(self):
        return self.__user_of_owner.stdout

    def get_access_right(self):
        return self.__access_right.stdout

    def get_mount_point(self):
        return self.__mount_point.stdout

    def get_hard_links(self):
        return self.__hard_links.stdout

    def get_total_size(self):
        return self.__total_size.stdout

    def __str__(self):
        return "collectData_multipleFileDetails"


obj = Filestat()
obj.collectData_singleFileDetails("/etc")
print(obj.get_file_name())