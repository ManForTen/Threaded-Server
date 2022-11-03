import socket
import threading

f = open('log.txt', 'w')
class ClientThreading(threading.Thread):
    def __init__(self, addr, conn):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        print("----------------------------")
        print (f"Новое подключение от {self.addr}")
        print("----------------------------")

    def run(self):
        f.write('Подключен:' + self.addr[0] + '\n')
        print (f"Подключение от {self.addr}")
        print("----------------------------")
        while True:
            data = self.conn.recv(2048)
            msg = data.decode()
            if msg == 'exit':
                break
            f.write(msg + '\n')
            print (f"Сообщение от {self.addr}: {msg}")
            self.conn.send(msg.encode())
            if msg == 'server off':
                self.conn.close()
                break
        f.write('Отключение клиента!' + '\n')
        print (f"Клиент {self.addr} отключился!")


ip = "localhost"
port = 9131
TYPE = socket.AF_INET
PROTOCOL = socket.SOCK_STREAM
sock = socket.socket(TYPE,PROTOCOL)
sock.bind((ip, port))
print("Включение сервера!")
print("Ожидание подключения клиента...")
while True:
    sock.listen(5)
    conn, addr = sock.accept()
    thread = ClientThreading(addr[0], conn)
    thread.start()


