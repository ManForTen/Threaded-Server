import socket
import threading

threads = []

def port(ip, port):
    sock = socket.socket()
    try:
        sock.connect((ip, port))
        print(f"Порт {port} открыт\n")
    except (ConnectionError, OSError):
        pass
    sock.close()

ip_ = input("Выберите ip: ")
port1 = 0
print('Запуск сканирования!')
while port1 < 65500:
    if threading.active_count():
        t = threading.Thread(target=port, args=(ip_, port1))
        t.start()
        threads.append(t)
        port1 = port1 + 1

print('Сканирование завершено!')
