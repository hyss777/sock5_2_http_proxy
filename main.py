import socks
import socket
#socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"192.168.17.111",7070)
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"127.0.0.1",7070)
socket.socket = socks.socksocket
from python_proxy import start_server
if __name__ == '__main__':
    start_server()

