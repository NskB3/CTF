import os, socket
import time
class machine:
	def __init__(self):
		pass
	@classmethod
	def menu(self):
		print("You Are defending!!\nOnly Works for Debian/Ubuntu Based Distros! Best Choice:\nKali 2018.2")
		print("Get to work and patch the vulnerabilities,\nIn Another Terminal!")
	@classmethod
	def connection_from_servers(self):
		global list
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.bind(("", 1337))
		sock.listen(5)
		conn, addr = sock.accept()
		print("	Got connection from client")
		for i in range(1, 3):
			os.system(str(conn.recv(65536)))
		list = []
		conn.close()
		sock.close()
	@classmethod
	def append_from_client(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.bind(("", 1338))
		sock.listen(5)
		conn, addr = sock.accept()
		print("Got connection from client!")
		list.append(conn.recv(65536))
def start():
	machine.menu()
	machine.connection_from_servers()
	machine.append_from_client()
start()
