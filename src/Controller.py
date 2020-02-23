from xml.etree.ElementTree import Element
from src import SystemInfo


class Controler(SystemInfo.SystemInfo):

    object_list = []

    def __init__(self):
        super().__init__()
        self.object_list.append(SystemInfo.SystemInfo())
        self.object_list.append(SystemInfo.ServiceInfo())

    def render_xml(self):
        self.object_list[0]
        self.object_list[1]
        mainBranch = Element('raport')
        child_sysInfo = [Element("system c")]

    def get_system_info(self):
        return self.object_list[0].os_info_s

    def get_service_info(self):
        return self.object_list[1].active_services

    def __str__(self):
        return "Controller"


test = Controler()
print(test.render_xml())
