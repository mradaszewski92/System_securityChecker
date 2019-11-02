import socket

SocCKet = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    SocCKet.connect(("google.com",80))
    if True:
        IP_Address=SocCKet.getsockname()[0]
        SocCKet.close()
        print(IP_Address)
except:
    SocCKet.close()
