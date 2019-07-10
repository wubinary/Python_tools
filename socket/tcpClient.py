import socket
 
target_host = socket.gethostbyname("www.google.com")
target_port = 80
 
# create socket
# AF_INET 代表使用標準 IPv4 位址或主機名稱
# SOCK_STREAM 代表這會是一個 TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# client 建立連線
client.connect((target_host, target_port))
 
# 傳送資料給 target
msg = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
client.send(str(msg).encode('utf-8'))
 
# 接收資料
response = client.recv(4096).decode('utf-8')
 
# 印出資料信息
print(response)
