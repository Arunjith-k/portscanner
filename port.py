''import'''
import socket



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)



#port = 1000
for portx in range(1,100):
    try:
        s.connect(('ad.samclass.info', portx))
        r = s.recv(1024)
        if 'congratulations' in r.decode('utf8'):
            print('[!] HIDDEN SERVICE FOUND: %s ~ %s' % (portx, r.decode('utf8'$
            s.close()
            break

