from src.auxiliary_functions import get_path_exists, header, debug, get_checksum
import time
import json
import subprocess
from Filestat import FileStat
from measurement import Measurement

class InspectDirectories(FileStat, Measurement):
    __directory = ["etc", "home", "media", "mnt", "root", "sbin", "tmp", "usr", "usr/bin", "var"]
    __hidden_files_dict = dict()
    __hidden_files_details_dict = dict()
    execution_time = list()
    __catalog_checksums = dict()
    __writer = object

    def walk_trough_dir(self):

        start = time.time()  # start measurement
        tmp_arr = list()

        for directory in self.__directory:

            if get_path_exists(f"/{directory}"):
                tmp_arr.append((get_checksum(directory), f"/{directory}"))
            else:
                debug("[INFO]", "File doesn't exists")

        self.__catalog_checksums['Catalog checksums'] = tmp_arr

        end = time.time()  # finish the measurement
        self.execution_time.append(("walk_trough_dir", end - start))

    def collect_hidden_files(self, path):
        """ Method return hidden files , without any special detail and add to dict"""
        start = time.time()
        command = f"ls -lA /{path}" + " | awk '{print $9}'" + " | grep \"^\\.\""
        tmp_arr = list()
        hidden_file = subprocess.run(command,
                                     shell=True,
                                     capture_output=True,
                                     universal_newlines=True)
        hidden_file_list = hidden_file.stdout.split("\n")

        for index in hidden_file_list:
            tmp_arr.append((index, "hidden"))

        end = time.time()
        self.__hidden_files_dict['Hidden file'] = tmp_arr
        self.execution_time.append(("collect_hidden_files", end - start))

    def collect_hidden_files_details(self, path):

        start = time.time()
        command = f"ls -lA /{path}" + " | awk '{print $9}'" + " | grep \"^\\.\""
        tmp_arr = list()
        hidden_file = subprocess.run(command,
                                     shell=True,
                                     capture_output=True,
                                     universal_newlines=True)
        hidden_file_list = hidden_file.stdout.split("\n")

        for index in hidden_file_list:
            full_path = path + "/" + index
            self.__file_name = subprocess.run("stat -c %n /{}".format(full_path), shell=True, capture_output=True,
                                              universal_newlines=True)  # -file name

            self.__file_type = subprocess.run("stat -c %F /{}".format(full_path), shell=True, capture_output=True,
                                              universal_newlines=True)  # -file type

            self.__id_owner = subprocess.run("stat -c %u /{}".format(full_path), shell=True, capture_output=True,
                                             universal_newlines=True)  # -user ID of owner

            self.__group_owner = subprocess.run("stat -c %G /{}".format(full_path), shell=True, capture_output=True,
                                                universal_newlines=True)  # -group name of owner

            self.__user_owner = subprocess.run("stat -c %U /{}".format(full_path), shell=True, capture_output=True,
                                               universal_newlines=True)  # -user name of owner

            self.__access_right = subprocess.run("stat -c %A /{}".format(full_path), shell=True, capture_output=True,
                                                 universal_newlines=True)  # -access rights in human readable form

            self.__mount_point = subprocess.run("stat -c %m /{}".format(full_path), shell=True, capture_output=True,
                                                universal_newlines=True)  # -mount point

            self.__hard_links = subprocess.run("stat -c %h /{}".format(full_path), shell=True, capture_output=True,
                                               universal_newlines=True)  # -number of hard links

            self.__total_size = subprocess.run("du -shb /{} ".format(full_path) + "| awk '{print $1}'", shell=True,
                                               capture_output=True,
                                               universal_newlines=True)  # -total size, in bytes

            self.__last_access = subprocess.run("stat -c %x /{} ".format(full_path), shell=True,
                                                capture_output=True,
                                                universal_newlines=True)  # -total size, in bytes

            self.__last_modification = subprocess.run("stat -c %y /{} ".format(full_path), shell=True,
                                                      capture_output=True,
                                                      universal_newlines=True)  # -total size, in bytes

            self.__last_status_change = subprocess.run("stat -c %z /{} ".format(full_path), shell=True,
                                                       capture_output=True,
                                                       universal_newlines=True)  # -total size, in bytes

            tmp_arr.append([("file_name", self.__file_name.stdout.strip("\n")),
                            ("Attribute", "hidden"),
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
        self.__hidden_files_details_dict['Hidden file'] = tmp_arr
        self.execution_time.append(("collect_hidden_files_details", end - start))

    def get_hidden_file_dict(self):
        return self.__hidden_files_dict

    def get_hidden_file_dict_json(self):
        return json.dumps(self.__hidden_files_dict)

    def get_hidden_files_details_dict(self):
        return self.__hidden_files_details_dict

    def get_directory_control_sum_dict(self):
        """ :return data as dict"""
        return self.__catalog_checksums

    def get_directory_control_sum_json(self):
        """:return data as json"""
        return json.dumps(self.__catalog_checksums)

    def get_execution_time(self):
        """abstract method :return data as float"""
        return self.execution_time

    def write_logs(self, path="."):
        """ write result walk_trough_dir(__catalog_checksums) to file """

        with open(f"{path}", "w") as self.__writer:
            data = self.__catalog_checksums['Catalog checksums']

            for i in range(0, len(data)):
                data_line = str(self.__catalog_checksums['Catalog checksums'][i][0]) + " " \
                       + str(self.__catalog_checksums['Catalog checksums'][i][1] + "\n")
                self.__writer.writelines(data_line)


obj = InspectDirectories()
obj.walk_trough_dir()
obj.collect_hidden_files("home/reg3x")
obj.collect_hidden_files_details("home/reg3x")
print(obj.get_hidden_file_dict())
