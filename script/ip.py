import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    sock.connect(("google.com", 80))
    if True:

        IP_Address = sock.getsockname()[0]

        # CLOSE SOCKET
        sock.close()

        # PRINT IP
        print(IP_Address)
except:
    sock.close()
