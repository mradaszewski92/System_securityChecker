import os
import datetime
import hashlib
import subprocess

def get_path_exists(path):
    """ :return True id directory/files exist"""
    return os.path.exists(path)

def get_date():
    """ :return date time as day_mounth_years"""
    return datetime.datetime.now().strftime("%d_%b_%Y")

def HEADER(type_msg, communicate):
    """ Decorating function: header"""
    print("")
    print(f"----------- {type_msg} {communicate}  ------------")

def DEBUG(type_msg, communicate):
    """ Decorating function: header"""
    print(f"{type_msg}{communicate}")

def get_checksum(path: str):
    """ :return returns the checksum based on the file size"""
    command = "du -shb /{} 2>/dev/null".format(path) + "| awk '{print $1}'"

    size_in_byte = subprocess.run(command,
                                  shell= True,
                                  capture_output=True,
                                  universal_newlines=True)

    value = size_in_byte.stdout
    hash = hashlib.new('sha1')
    hash.update(value.encode('utf-8'))

    return hash.hexdigest()

def write(reparsed,name):
    """ :name - raport name"""
    with open(f"report/{name}_{get_date()}.xml", "a") as active_service:
        active_service.write(reparsed.toprettyxml(indent="    "))
    active_service.close()

