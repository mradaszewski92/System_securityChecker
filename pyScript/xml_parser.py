# XML PARSER MODULE

import xml.etree.ElementTree as ET

tree = ET.parse("report/xml_raport.xml")
elem = root = tree.getroot()
general_res = []

for i in range(0, len(elem)):
    if len(elem[i]) >= 2:
        res_A = elem[i][0].items()
        res_B = elem[i][1].items()
        res_A_state= res_A[0]
        res_B_ip= res_B[0]
        if res_A_state[1] == "up":
            print(res_B_ip[1])
