import socket
import threading

ip = "localhost"
port = 9090
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((ip, port))
print("Включение сервера")
print("Ожидание подключения пользователя..")
while True:
    server.listen(1)
    conn, addr = server.accept()

    print ("Новое подключение: ", addr)


    print ("Подключение от: ", addr[0])
    while True:
        data = conn.recv(2048)
        msg = data.decode()
        if msg == 'exit':
            break
        print (f"Сообщение от {addr[0]}: {msg}")
        conn.send(bytes(msg, 'UTF-8'))
    print ("Клиент ", addr[0], " отключился...")


