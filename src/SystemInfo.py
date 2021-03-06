import subprocess
from subprocess import PIPE
import time
import os
import json


info = "[*]"


class SystemInfo(Measurement):
    os_info_dict: dict = {}
    os_info_list: list = []
    __execution_time = list()

    def os_info(self):

        try:
            start = time.time()

            default_shell = os.environ['SHELL']
            user_name = os.environ['LOGNAME']
            hostName = subprocess.run("hostname", stdout=PIPE).stdout.decode("utf-8")
            osVersion = subprocess.run(["uname", "-v"], stdout=PIPE).stdout.decode("utf-8")
            Architecture = subprocess.run(["uname", "-m"], stdout=PIPE).stdout.decode("utf-8")
            kernel_y = subprocess.run("grep '^VERSION=' /etc/os-release | awk '{print $1}'",
                                      shell=True,
                                      capture_output=True,
                                      universal_newlines=True).stdout.split("=")[1].replace("\"", "")
            end = time.time()

            os_info: list = [("Hostname", hostName),
                             ("Username", user_name),
                             ("OS_VERSION", osVersion),
                             ("Architecture", Architecture),
                             ("Default_shell", default_shell),
                             ("Kernel", kernel_y)]

            self.os_info_dict['os_info'] = os_info
            self.os_info_list = os_info
            end = time.time()

            self.__execution_time.append(("os_info", end - start))

        except subprocess.TimeoutExpired as timeExpired:
            print(timeExpired)
            return None

    def get_osInfo_dict(self):
        """:return os info as dict"""
        return self.os_info_dict

    def get_osInfo_list(self):
        """:return os info as list"""
        return self.os_info_list

    def get_osInfo_list_json(self):
        """:return os info as json"""
        return json.dumps(self.get_osInfo_dict())

    def get_execution_time(self):
        pass

    def write_logs(self, path):
        pass

    def __str__(self):
        return "System info"


class ServiceInfo(Measurement):

    __execution_time = list()
    active_services_list = []
    active_services_dict = {}


    def service_info(self):

        start = time.time()
        service = subprocess.run("service --status-all | grep + ",
                                 shell=True,
                                 capture_output=True).stdout.decode("utf-8").split("\n")

        # APPEND ACTIVE SERVICE TO tmpArr: list
        tmp_arr = []
        for i in range(0, len(service)):
            if service[i] != "":
                tmp_arr.append((service[i].split(" ")[5], "up"))

        end = time.time()

        self.active_services_list = tmp_arr
        self.active_services_dict['service_info'] = tmp_arr

        self.__execution_time.append(("service_info", end - start))

    def get_execution_time(self):
        """ :return time execution"""
        return self.__execution_time

    def get_active_service_list(self):
        """ :return all active service in system as list"""
        return self.active_services_list

    def get_active_service_dict(self):
        """ :return all active service in system as list as dictionary"""
        return self.active_services_dict

    def get_active_service_list_json(self):
        """ :return all active service in system as json"""
        return json.dumps(self.active_services_dict)

    def write_logs(self, path):
        pass

    def __str__(self):
        return "Service_Info"
