import socket

m = 0
F = input('Если вы хотите ввести номер порта и имя хоста, напишите да:')
if F == 'да' or F == 'Да':
    host = input('Введите имя хоста:')
    port_number = int(input('Введите номер порта:'))
    m += 1

sock = socket.socket()
sock.setblocking(1)

if m == 0:
    sock.connect(('localhost', 9090))
else:
    sock.connect((host,port_number))

while True:
    msg = input('Введите сообщение: ')
    sock.send(msg.encode())
    data = sock.recv(1024)
    print("Сообщение от сервера :", data.decode())
    if msg == 'exit':
        break

sock.close()