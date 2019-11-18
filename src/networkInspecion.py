from baseclass import BaseClass
import time
from measurement import Measurement
import socket
import ipaddress
import json
import subprocess


#  [!][!]ss -4 -a| grep --color '^udp\|^tcp\|' lub ss -t-a -p
#  [!][!]ps -p pid -O user
#  [!]ss -4 state listening;
#  ss [opcja] state
#  ss -4 state listening
# sprawdzanie podjerzanych pidow z ss
# ps -e
# [!]ps au[!]
# mozna polaczyc z whois -a( najwięcej informacji)

class NetworkInspection(BaseClass, Measurement):
    __local_ip = dict()
    __execution_time = list()
    __active_interfaces = {}
    __listening_and_non_Listening_soc_ipv4_udp = dict()
    __listening_and_non_Listening_soc_ipv4_pid = dict()
    __connection_pid = dict()

    def collect_local_ip(self):
        start = time.time()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            sock.connect(("google.com", 80))
            if True:
                self.__local_ip['Local ip'] = [sock.getsockname()[0]]
                sock.close()  # CLOSE SOCKET
                end = time.time()
                self.__execution_time.append(("local_ip", end - start))
        except Exception as err:
            print(err)
            sock.close()

    def collect_active_network_interfaces(self):
        start = time.time()
        interfaces = subprocess.run("netstat -i | awk '{print $1}'",
                                    shell=True,
                                    capture_output=True,
                                    universal_newlines=True).stdout.split("\n")

        interfaces_stat = subprocess.run("netstat -i | awk '{print $3}'",
                                         shell=True,
                                         capture_output=True,
                                         universal_newlines=True).stdout.split("\n")

        tmp_arr = list()
        remove = ['Kernel', 'Iface', '']
        for active_interface in interfaces:
            if active_interface not in remove:
                tmp_arr.append([active_interface, "active"])

        remove_1 = ['table', 'RX-OK', '']
        tmp_active_interface_stat = []
        for active_interface_stat in interfaces_stat:
            if active_interface_stat not in remove_1:
                tmp_active_interface_stat.append(active_interface_stat)

        for i in range(0, len(tmp_active_interface_stat)):
            tmp_arr[i].append(tmp_active_interface_stat[i])

        self.__active_interfaces['active network interfaces'] = tmp_arr
        end = time.time()
        self.__execution_time.append(("active network interfaces", end - start))

    def collect_connection_tcp_udp(self):
        # ss -4 -a| grep --color '^udp\|^tcp\|'

        data = subprocess.run("ss -4 -a",
                              shell=True,
                              capture_output=True,
                              universal_newlines=True).stdout.split("\n")

        connection_len = len(data)
        connection_result = []

        for position in range(1, connection_len):

            tmp_data = data[position].split(" ")
            tmp_arr = []

            for i in range(0, len(tmp_data)):
                if tmp_data[i] != '':
                    tmp_arr.append(tmp_data[i])
            connection_result.append(tmp_arr)

        self.__listening_and_non_Listening_soc_ipv4_udp['connection_tcp_udp'] = connection_result

    def collect_connection_tcp_udp_verbose(self):
        # ss -4 -a -p !! must be run as root
        active_connection = subprocess.run("ss -4 -a -p -e",
                                           shell=True,
                                           capture_output=True,
                                           universal_newlines=True).stdout.split("\n")

        connection_len = len(active_connection)

        result_active_connection = []

        for position in range(1, connection_len):

            tmp_data = active_connection[position].split(" ")
            tmp_arr = []

            for i in range(0, len(tmp_data)):
                if tmp_data[i] != '':
                    tmp_arr.append(tmp_data[i])
            result_active_connection.append(tmp_arr)

        self.__listening_and_non_Listening_soc_ipv4_pid['connection_tcp_udp_verbose'] = result_active_connection

    def collect_PID_connection(self):
        active_connection = subprocess.run("ss -4 -a -p -e",
                                           shell=True,
                                           capture_output=True,
                                           universal_newlines=True).stdout.split("\n")

        connection_len = len(active_connection)

        result_active_connection = []

        for position in range(1, connection_len):

            tmp_data = active_connection[position].split(" ")
            tmp_arr = []

            for i in range(0, len(tmp_data)):
                if tmp_data[i] != '':
                    tmp_arr.append(tmp_data[i])
            result_active_connection.append(tmp_arr)

        self.__listening_and_non_Listening_soc_ipv4_pid['connection_tcp_udp_verbose'] = result_active_connection
        better_arr = []

        for i in range(0, len(result_active_connection) - 1):
            tmp_arr = []
            for j in [0, 1, 4, 5, 6, 7, 8]:
                tmp_arr.append(result_active_connection[i][j])
            better_arr.append(tmp_arr)

        name_pid_array = []
        for i in range(0, len(better_arr)):
            tmp_arr = []
            length = len(better_arr[i][4].split(":")[1].split(","))
            if length == 3:
                name = better_arr[i][4].split(":")[1].split(",")[0].replace("(", "")
                pid = better_arr[i][4].split(":")[1].split(",")[1].split("=")[1]
                file_descriptor = better_arr[i][4].split(":")[1].split(",")[2].replace(")", "").split("=")[1]
                tmp_arr.append([name, pid])

            else:
                n = better_arr[i][4].split(":")[1].split(",")[0].replace("(", "")
                p = better_arr[i][4].split(":")[1].split(",")[1].split("=")[1]
                fd = better_arr[i][4].split(":")[1].split(",")[2].split("=")[1].replace(")", "")
                # n2 = better_arr[i][4].split(":")[1].split(",")[3].replace("(", "")
                # p2 = better_arr[i][4].split(":")[1].split(",")[4].split("=")[1]
                # fd2 = better_arr[i][4].split(":")[1].split(",")[5].split("=")[1].replace(")", "")
                tmp_arr.append([n, p])
            name_pid_array.append(tmp_arr)

        self.__connection_pid['PID_connection'] = name_pid_array

    # --------------------------------------------

    def get_local_ip(self):
        return self.__local_ip

    def get_execution_time(self):
        return self.__execution_time

    def get_active_interfaces_dict(self):
        return self.__active_interfaces

    def get_active_interfaces_json(self):
        return json.dumps(self.__active_interfaces)

    def get_connection_tcp_udp_dict(self):
        return self.__listening_and_non_Listening_soc_ipv4_udp

    def get_connection_tcp_udp_json(self):
        return json.dumps(self.__listening_and_non_Listening_soc_ipv4_udp)

    def get_connection_tcp_udp_verbose_dict(self):
        return self.__listening_and_non_Listening_soc_ipv4_pid

    def get_connection_tcp_udp_verbose_json(self):
        return json.dumps(self.__listening_and_non_Listening_soc_ipv4_pid)

    def write_logs(self, path):
        pass


obj = NetworkInspection()
obj.collect_active_network_interfaces()
obj.collect_local_ip()
obj.collect_connection_tcp_udp()
obj.collect_PID_connection()
