from xml.etree.ElementTree import tostring, Element
from src import Filestat, SystemInfo
from src.auxiliary_functions import *

from xml.dom import minidom


class XmlRaport(object):
    mainBranch = Element('INFO')

    def render_service_raport(self, service, name):

        children = [Element('service', name=str(i), attrib={"state": "up"}) for i in service]

        self.mainBranch.extend(children)
        rough_str = tostring(self.mainBranch).decode("utf-8")
        reparsed = minidom.parseString(rough_str)

        if os.path.exists(f"report/{XmlRaport.__name__}_{get_date()}.xml"):
            debug("info", "File exists")
        else:
            write(reparsed, XmlRaport.__name__)

    def render_os_info_raport(self, os_info, name):
        root = Element('OS_DETAIL')
        children = [Element('os_detail', name=i[0], attrib={"value": f"{i[1]}"}) for i in os_info]

        root.extend(children)
        rough_str = tostring(root).decode("utf-8")
        reparsed = minidom.parseString(rough_str)

        if os.path.exists(f"report/{name}_{get_date()}.xml"):
            debug("info", "File exists")
        else:
            write(reparsed, name)


class Xml_fascade(object):

    def __init__(self):
        self.dir_check = Filestat()
        self.system_info = SystemInfo.SystemInfo()


DirCheck


def write(self):
    pass
