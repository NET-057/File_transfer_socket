import socket
import sys
import os

host = socket.gethostname()
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 9999
s.bind(('',port))
s.listen(5)

def socket_conn():
    conn,addr = s.accept()
    print("Device is Connected to IP: "+str(addr[0])+ ' and Port: '+str(addr[1]))
    sFileName = conn.recv(1024)
    if os.path.exists(sFileName):
        send_command(conn,sFileName)
    conn.close()
    sys.exit()

def send_command(conn,sFileName):
    uplod = open(sFileName, "rb")
    red = uplod.read(1024)
    while red:
        conn.send(red)
        red = uplod.read(1024)
    print("SENDING COMPLETE")
    uplod.close()



socket_conn()