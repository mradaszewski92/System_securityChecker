import subprocess
from subprocess import Popen, PIPE
import os
import time
from xml.etree.ElementTree import Element,tostring
from xml.dom import minidom
from check_if_exist import get_date, get_path_exists,HEADER,DEBUG
import os

info = "[*]"

class SystemInfo(object):

    def systeminfo(self):

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

            print(info, "HOSTNAME: ", hostName,
                  info, "OS_VERSION: ", osVersion,
                  info, "Architecture: ", Architecture,
                  info, "Kernel: ", kernel_y,
                  info, "User_name: ", user_name, "\n",
                  info, "Default_shell: ", default_shell, "\n",
                  end - start
                  )

            return hostName, user_name, osVersion, Architecture, default_shell, kernel_y

        except subprocess.TimeoutExpired as timeExpired:
            print(timeExpired)
            return None

    def service_info(self):

        start = time.time()

        service = subprocess.run("service --status-all | grep + ",
                                 shell=True,
                                 capture_output=True).stdout.decode("utf-8").split("\n")

        active_services: list = []

        for i in range(0, len(service)):

            if service[i] != "":
                active_services.append(service[i].split(" ")[5])
        end = time.time()

        active_services.append((end - start))

        return active_services

class XmlRaport(object):

    def render_service_raport(self, service):


        root = Element('Root')
        children = [Element('service', name=str(i), attrib={"state": "up"}) for i in service]

        root.extend(children)
        rough_str = tostring(root).decode("utf-8")
        reparsed = minidom.parseString(rough_str)

        if os.path.exists(f"report/system_info_{get_date()}.xml"):
            DEBUG(info, "File exists")
        else:
            with open(f"report/system_info_{get_date()}.xml", "a") as active_service:
                active_service.write(reparsed.toprettyxml(indent="    "))
            active_service.close()


service = SystemInfo().service_info()
XmlRaport().render_service_raport(service)
