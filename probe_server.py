import sys
from socket import socket, AF_INET, SOCK_STREAM

ENCODING = 'utf-8'
# response = b'HTTP/1.0 200 OK\r\nContent-Length: 11\r\nContent-Type: text/html; charset=UTF-8\r\n\r\nHello World\r\n'
response = b'HTTP/1.0 200 OK'


def send_message(sock, message):
    """
    Отправка сообщения
    :param sock: сокет
    :param message: словарь сообщения
    :return: None
    """
    # сообщение переводим в байты
    b_message = message.encode(ENCODING)
    # Отправляем
    sock.send(b_message)


try:
    address = sys.argv[1]
except IndexError:
    address = ''
try:
    port = int(sys.argv[2])
except IndexError:
    port = 7777
except ValueError:
    print('Порт должен быть целым числом')
    sys.exit(0)

if __name__ == '__main__':
    server = socket(AF_INET, SOCK_STREAM)
    # address = ''
    # port = 7777
    server.bind((address, port))
    server.listen(5)
    while True:
        client, address = server.accept()
        byte_message = client.recv(1024)
        print(byte_message)
        message = byte_message.decode(ENCODING)
        print(message)

        client.send(response)

        client.close()
