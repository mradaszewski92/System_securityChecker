import subprocess
from subprocess import Popen, PIPE
import os
import time
import os
import XmlRaport
from my_tool import write

info = "[*]"

class SystemInfo(object):

    os_info_s = []

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
            self.os_info_s = os_info
     
        except subprocess.TimeoutExpired as timeExpired:
            print(timeExpired)
            return None

    def __str__(self):
        return "Os_info"


class ServiceInfo(object):
    active_services = []
    time = 0.0
    def service_info(self):

        start = time.time()
        service = subprocess.run("service --status-all | grep + ",
                                 shell=True,
                                 capture_output=True).stdout.decode("utf-8").split("\n")

        # APPEND ACTIVE SERVICE TO self.active_services
        tmpArr =[]
        for i in range(0, len(service)):
            if service[i] != "":
                tmpArr.append(service[i].split(" ")[5])

        end = time.time()

        self.time = end-start
        self.active_services

    def get_execution_time(self):
        return self.time

    def __str__(self):
        return "Service_Info"

