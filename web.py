import socket   

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.one.org.ma/FR/stageone/contact.asp', 80))
cmd = 'GET http://www.one.org.ma/FR/stageone/contact.asp HTTP/1.1\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
