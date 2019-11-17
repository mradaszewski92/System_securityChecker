import subprocess
import json
from abc import ABC
import time
from baseclass import BaseClass
from measurement import Measurement


class FileStat(Measurement, BaseClass):
    __file_detail_dict = {}
    __file_details_dict = {}
    __file_name = ""
    __file_type = ""
    __id_owner = ""
    __group_owner = ""
    __user_owner = ""
    __access_right = ""
    __mount_point = ""
    __hard_links = ""
    __total_size = ""
    __last_access = ""
    __last_modification = ""
    __last_status_change = ""

    def collect_data_single_file_details(self, file_path: str):
        """ Method collect data about single file, and assignee data to list"""
        start = time.time()
        tmp_arr = list()

        self.__file_name = subprocess.run("stat -c %n /{}".format(file_path), shell=True, capture_output=True,
                                          universal_newlines=True)  # -file name
        self.__file_type = subprocess.run("stat -c %F /{}".format(file_path), shell=True, capture_output=True,
                                          universal_newlines=True)  # -file type
        self.__id_owner = subprocess.run("stat -c %u /{}".format(file_path), shell=True, capture_output=True,
                                         universal_newlines=True)  # -user ID of owner
        self.__group_owner = subprocess.run("stat -c %G /{}".format(file_path), shell=True, capture_output=True,
                                            universal_newlines=True)  # -group name of owner
        self.__user_owner = subprocess.run("stat -c %U /{}".format(file_path), shell=True, capture_output=True,
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
                        ("id_owner", self.__id_owner.stdout.strip("\n")),
                        ("group_owner", self.__group_owner.stdout.strip("\n")),
                        ("user_owner", self.__user_owner.stdout.strip("\n")),
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
        end = time.time()
        self.__execution_time.append(("collect_data_single_file_details", end - start))

    def collect_data_multiple_file_details(self, files_path: list):
        """" Method collect data about multiple files, and assignee to list. Method has additional loop inside"""
        start = time.time()
        tmp_arr = list()
        for file in files_path:
            self.__file_name = subprocess.run("stat -c %n /{}".format(file), shell=True, capture_output=True,
                                              universal_newlines=True)  # -file name
            self.__file_type = subprocess.run("stat -c %F /{}".format(file), shell=True, capture_output=True,
                                              universal_newlines=True)  # -file type
            self.__id_owner = subprocess.run("stat -c %u /{}".format(file), shell=True, capture_output=True,
                                             universal_newlines=True)  # -user ID of owner
            self.__group_owner = subprocess.run("stat -c %G /{}".format(file), shell=True, capture_output=True,
                                                universal_newlines=True)  # -group name of owner
            self.__user_owner = subprocess.run("stat -c %U /{}".format(file), shell=True, capture_output=True,
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
                            ("id_owner", self.__id_owner.stdout.strip("\n")),
                            ("group_owner", self.__group_owner.stdout.strip("\n")),
                            ("user_owner", self.__user_owner.stdout.strip("\n")),
                            ("access_right", self.__access_right.stdout.strip("\n")),
                            ("mount_point", self.__mount_point.stdout.strip("\n")),
                            ("hard_links", self.__hard_links.stdout.strip("\n")),
                            ("last_access", self.__last_access.stdout.strip("\n")),
                            ("last_modification", self.__last_modification.stdout.strip("\n")),
                            ("last_status_change", self.__last_status_change.stdout.strip("\n")),
                            ("total_size", self.__total_size.stdout.strip("\n"))
                            ])
        end = time.time()
        self.__file_details_dict['file_details'] = tmp_arr
        self.__execution_time.append(("collect_data_multiple_file_details", end - start))

    def write_logs(self, path):
        max_len = len(self.__file_details_dict["file_details"])
        data = self.__file_details_dict["file_details"]

        with open(f"{path}", "w") as writer:

            for col in range(0, len(data)):
                for row in range(0, len(data[0])):
                    writer.writelines(data[col][row][0] + " : " + data[col][row][1] + "\n")
                writer.writelines("-----------------------------------\n")

    def get_execution_time(self):
        return self.__execution_time

    def get_files_detail_dict(self):
        return self.__file_detail_dict

    def get_files_detail_json(self):
        return json.dumps(self.__file_detail_dict)

    def get_file_name(self):
        return self.__file_name.stdout

    def get_file_type(self):
        return self.__file_type.stdout

    def get_id_owner(self):
        return self.__id_owner.stdout

    def get_group_owner(self):
        return self.__group_owner.stdout

    def get_user_owner(self):
        return self.__user_owner.stdout

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


obj = FileStat()

obj.collect_data_multiple_file_details(["home/reg3x", "home/reg3x/Documents/test"])
obj.write_logs("../report/FIlestat")
