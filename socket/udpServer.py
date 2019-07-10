import socket  
  
address = (socket.gethostbyname('127.0.0.1'), 31500)  
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
s.bind(address)  
  
while True:  
    data, addr = s.recvfrom(2048)  
    if not data:  
        print("client has exist")  
        break  
    print("received:", data.decode('utf-8'), "from", addr ) 
  
s.close()  
