import os
import datetime
import hashlib
import subprocess

def get_path_exists(path):
    """ :return true or false dopend on if exists"""
    return os.path.exists(path)

def get_date():

    date = datetime.datetime.now().strftime("%d_%b_%Y")
    return date



def HEADER(type_msg, communicate):
    print("")
    print(f"----------- {type_msg} {communicate}  ------------")


def DEBUG(type_msg, communicate):
    print(f"{type_msg}{communicate}")

def get_checksum(path: str):
    command = "du -shb /{} 2>/dev/null".format(path) + "| awk '{print $1}'"

    size_in_byte = subprocess.run(command,
                                      shell=True,
                                      capture_output=True,
                                      universal_newlines=True)

    value = size_in_byte.stdout
    hash = hashlib.new('sha1')
    hash.update(value.encode('utf-8'))

    return hash.hexdigest()