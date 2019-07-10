import socket  

address = (socket.gethostbyname('127.0.0.1'), 31500)  
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
  
while True:  
    msg = input()  
    if not msg:  
        break  
    s.sendto(str(msg).encode('utf-8'), address)  
  
s.close()  
