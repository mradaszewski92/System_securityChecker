from src.auxiliary_functions import get_path_exists, header, debug, get_checksum
import time
import json


class CheckDir(object):

    __directory = ["etc", "home", "media", "mnt", "root", "sbin", "tmp", "usr", "usr/bin", "var"]
    __execution_time = 0.0
    __catalog_checksums = dict()
    __writer = object

    def walk_trough_dir(self):

        start = time.time()  # start measurement
        tmp_arr = list()
        for directory in self.__directory:
            #  header("[INFO]", f"CHECK {directory} directory")

            if get_path_exists(f"/{directory}"):

                #  debug("[INFO]", f"{get_checksum(directory)} for: {directory}")  # Show debug info

                tmp_arr.append((get_checksum(directory), f"/{directory}"))

            else:
                debug("[INFO]", "File doesn't exists")
        self.__catalog_checksums['Catalog checksums'] = tmp_arr

        end = time.time()  # finish the measurement
        self.__execution_time = end - start

    def get_directory_control_sum_dict(self):
        """ :return data as dict"""
        return self.__catalog_checksums

    def get_directory_control_sum_json(self):
        """:return data as json"""
        return json.dumps(self.__catalog_checksums)

    def get_execution_time(self):
        """:return data as float"""
        return self.__execution_time

    def __del__(self):
        pass

class HiddenFile(object): pass
