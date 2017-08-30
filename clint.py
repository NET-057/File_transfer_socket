import socket
import sys
import os

host = '172.25.18.165'
port = 9999
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
os.chdir(r'D:/')
filename = input('ENTER FILE Name - ')
change = False
while True:
    try:
        s.send(str.encode(filename))
        cmd = s.recv(2048)

        if cmd:
            change = True
            with open(filename,'wb') as f:
                while cmd:
                  f.write(cmd)
                  cmd = s.recv(2048)
                print("dowwnload Complete")
                f.close()
        if change is not True:
            print('FILE NOT FOUND')

        s.close()
        break

    except Exception as e:
        print(e)
        sys.exit()