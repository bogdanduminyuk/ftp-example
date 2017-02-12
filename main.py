# coding: utf-8

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "D:\Cloud.mail.ru", perm="elradfmwM")
authorizer.add_anonymous("D:\YandexDisk")
handler = FTPHandler
handler.authorizer = authorizer
handler.banner = "pyftpdlib based ftpd ready."

address = ('192.168.1.249', 2121)
server = FTPServer(address, handler)

server.max_cons = 256
server.max_cons_per_ip = 5

server.serve_forever()