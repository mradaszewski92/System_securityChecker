from auxiliary_functions import get_date, get_path_exists, header, debug, get_checksum
import subprocess
import json


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


class GetFileDetail(object):
    file_detail_dict = {}
    file_detail_list = []
    file_name = ""
    file_type = ""
    id_of_owner = ""
    group_of_owner = ""
    user_of_owner = ""
    access_right = ""
    mount_point = ""
    hard_links = ""
    total_size = ""
    last_access = ""
    last_modification = ""
    last_status_change = ""

    def get_singleFileDetails(self, file: str):
        """ Method return a"""
        tmp_arr = []
        self.file_name = subprocess.run("stat -c %n /{}".format(file), shell=True, capture_output=True,
                                        universal_newlines=True)  # -file name
        self.file_type = subprocess.run("stat -c %F /{}".format(file), shell=True, capture_output=True,
                                        universal_newlines=True)  # -file type
        self.id_of_owner = subprocess.run("stat -c %u /{}".format(file), shell=True, capture_output=True,
                                          universal_newlines=True)  # -user ID of owner
        self.group_of_owner = subprocess.run("stat -c %G /{}".format(file), shell=True, capture_output=True,
                                             universal_newlines=True)  # -group name of owner
        self.user_of_owner = subprocess.run("stat -c %U /{}".format(file), shell=True, capture_output=True,
                                            universal_newlines=True)  # -user name of owner
        self.access_right = subprocess.run("stat -c %A /{}".format(file), shell=True, capture_output=True,
                                           universal_newlines=True)  # -access rights in human readable form
        self.mount_point = subprocess.run("stat -c %m /{}".format(file), shell=True, capture_output=True,
                                          universal_newlines=True)  # -mount point
        self.hard_links = subprocess.run("stat -c %h /{}".format(file), shell=True, capture_output=True,
                                         universal_newlines=True)  # -number of hard links
        self.total_size = subprocess.run("du -shb /{} ".format(file) + "| awk '{print $1}'", shell=True,
                                         capture_output=True,
                                         universal_newlines=True)  # -total size, in bytes

        self.last_access = subprocess.run("stat -c %x /{} ".format(file), shell=True,
                                          capture_output=True,
                                          universal_newlines=True)  # -total size, in bytes
        self.last_modification = subprocess.run("stat -c %y /{} ".format(file), shell=True,
                                                capture_output=True,
                                                universal_newlines=True)  # -total size, in bytes
        self.last_status_change = subprocess.run("stat -c %z /{} ".format(file), shell=True,
                                                 capture_output=True,
                                                 universal_newlines=True)  # -total size, in bytes

        tmp_arr.append([("file_name", self.file_name.stdout.strip("\n")),
                        ("file_type", self.file_type.stdout.strip("\n")),
                        ("id_of_owner", self.id_of_owner.stdout.strip("\n")),
                        ("group_of_owner", self.group_of_owner.stdout.strip("\n")),
                        ("user_of_owner", self.user_of_owner.stdout.strip("\n")),
                        ("access_right", self.access_right.stdout.strip("\n")),
                        ("mount_point", self.mount_point.stdout.strip("\n")),
                        ("hard_links", self.hard_links.stdout.strip("\n")),
                        ("last_access", self.last_access.stdout.strip("\n")),
                        ("last_modification", self.last_modification.stdout.strip("\n")),
                        ("last_status_change", self.last_status_change.stdout.strip("\n")),
                        ("total_size", self.total_size.stdout.strip("\n"))
                        ]
                       )
        self.file_detail_dict['file_details'] = tmp_arr
        self.file_detail_list = tmp_arr

    def get_multipleFileDetails(self, files: list):
        """ Method return a"""
        tmp_arr = []
        for file in files:
            self.file_name = subprocess.run("stat -c %n /{}".format(file), shell=True, capture_output=True,
                                            universal_newlines=True)  # -file name
            self.file_type = subprocess.run("stat -c %F /{}".format(file), shell=True, capture_output=True,
                                            universal_newlines=True)  # -file type
            self.id_of_owner = subprocess.run("stat -c %u /{}".format(file), shell=True, capture_output=True,
                                              universal_newlines=True)  # -user ID of owner
            self.group_of_owner = subprocess.run("stat -c %G /{}".format(file), shell=True, capture_output=True,
                                                 universal_newlines=True)  # -group name of owner
            self.user_of_owner = subprocess.run("stat -c %U /{}".format(file), shell=True, capture_output=True,
                                                universal_newlines=True)  # -user name of owner
            self.access_right = subprocess.run("stat -c %A /{}".format(file), shell=True, capture_output=True,
                                               universal_newlines=True)  # -access rights in human readable form
            self.mount_point = subprocess.run("stat -c %m /{}".format(file), shell=True, capture_output=True,
                                              universal_newlines=True)  # -mount point
            self.hard_links = subprocess.run("stat -c %h /{}".format(file), shell=True, capture_output=True,
                                             universal_newlines=True)  # -number of hard links
            self.total_size = subprocess.run("du -shb /{} ".format(file) + "| awk '{print $1}'", shell=True,
                                             capture_output=True,
                                             universal_newlines=True)  # -total size, in bytes

            self.last_access = subprocess.run("stat -c %x /{} ".format(file), shell=True,
                                              capture_output=True,
                                              universal_newlines=True)  # -total size, in bytes
            self.last_modification = subprocess.run("stat -c %y /{} ".format(file), shell=True,
                                                    capture_output=True,
                                                    universal_newlines=True)  # -total size, in bytes
            self.last_status_change = subprocess.run("stat -c %z /{} ".format(file), shell=True,
                                                     capture_output=True,
                                                     universal_newlines=True)  # -total size, in bytes

            tmp_arr.append([("file_name", self.file_name.stdout.strip("\n")),
                            ("file_type", self.file_type.stdout.strip("\n")),
                            ("id_of_owner", self.id_of_owner.stdout.strip("\n")),
                            ("group_of_owner", self.group_of_owner.stdout.strip("\n")),
                            ("user_of_owner", self.user_of_owner.stdout.strip("\n")),
                            ("access_right", self.access_right.stdout.strip("\n")),
                            ("mount_point", self.mount_point.stdout.strip("\n")),
                            ("hard_links", self.hard_links.stdout.strip("\n")),
                            ("last_access", self.last_access.stdout.strip("\n")),
                            ("last_modification", self.last_modification.stdout.strip("\n")),
                            ("last_status_change", self.last_status_change.stdout.strip("\n")),
                            ("total_size", self.total_size.stdout.strip("\n"))
                            ])

        self.file_detail_dict['file_details'] = tmp_arr
        self.file_detail_list = tmp_arr

    def get_files_detail_dict(self):
        return self.file_detail_dict

    def get_files_detail_list(self):
        return self.file_detail_list

    def get_files_detail_json(self):
        return json.dumps(self.file_detail_dict)

    def get_file_name(self):
        return self.file_name

    def get_file_type(self):
        return self.file_type

    def get_id_of_owner(self):
        return self.id_of_owner

    def get_group_of_owner(self):
        return self.group_of_owner

    def get_user_of_owner(self):
        return self.user_of_owner

    def get_access_right(self):
        return self.access_right

    def get_mount_point(self):
        return self.mount_point

    def get_hard_links(self):
        return self.hard_links

    def get_total_size(self):
        return self.total_size

