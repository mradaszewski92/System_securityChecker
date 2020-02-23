#!/usr/bin/python3.7
import subprocess
import pprint
import json


class Filestat(object):
    information_collected = {"file_name": "stat -c %n /{}",
                             "file_type": "stat -c %F /{}",
                             "id_owner": "stat -c %u /{}",
                             "group_owner": "stat -c %G /{}",
                             "user_owner": "stat -c %U /{}",
                             "access_right": "stat -c %A /{}",
                             "mount_point": "stat -c %m /{}",
                             "hard_links": "stat -c %h /{}",
                             "last_access": "stat -c %x /{}",
                             "last_modification": "stat -c %y /{} ",
                             "last_status_change": "stat -c %z /{} ",
                             }
    __file_detail_dict = {}
    __dict_files_details = {}

    def collect_details_data_for_single_file(self, file_path: str):
        """ Method collect data about single file, and assignee data to list"""
        single_object_details = dict()

        for key in self.information_collected.keys():
            res = subprocess.run(self.information_collected[key].format(file_path), shell=True, capture_output=True,
                                 universal_newlines=True).stdout.strip("\n")
            single_object_details[key] = res

        object_size = subprocess.run("du -shb /{} ".format("etc") + "| awk '{print $1}'",
                                     shell=True, capture_output=True,
                                     universal_newlines=True).stdout.strip("\n")

        single_object_details["total_size"] = object_size

        print(single_object_details)
        return single_object_details

    def collect_details_data_for_list_of_files(self, files_path: list):
        """" Method collect data about multiple files, and assignee to list. Method has additional loop inside
            :return nothing
        """
        tets = list()

        for file in files_path:
            tmp_arr = []
            object_size = subprocess.run("du -shb /{} ".format(file) + "| awk '{print $1}'",
                                         shell=True, capture_output=True,
                                         universal_newlines=True).stdout.strip("\n")
            for key in self.information_collected.keys():
                res = subprocess.run(self.information_collected[key].format(file), shell=True, capture_output=True,
                                     universal_newlines=True).stdout.strip("\n")
                tmp_arr.append({key: res})

            tmp_arr.append({"total_size": object_size})
            tets.append(tmp_arr)

        self.__dict_files_details = tets
        print(pprint.pprint(self.__dict_files_details))

    def write_logs(self, path):
        max_len = len(self.__dict_files_details["file_details"])
        data = self.__dict_files_details["file_details"]

        with open(f"{path}", "w") as writer:

            for col in range(0, len(data)):
                for row in range(0, len(data[0])):
                    writer.writelines(data[col][row][0] + " : " + data[col][row][1] + "\n")
                writer.writelines("-----------------------------------\n")

    def __str__(self):
        return "collectData_multipleFileDetails"


if __name__ == "__main__":
    Filestat().collect_details_data_for_list_of_files(['etc', 'home'])
