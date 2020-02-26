import socket

HOST = 'localhost'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
op = 'n'
while op == 'n':
    print('SISTEMA DE ECUACIONES LINEALES 2*2')
    print('Ax + By = C')
    print('Dx + Ey = F')
    a = input('Digite el valor de A:')
    b = input('Digite el valor de B:')
    c = input('Digite el valor de C:')
    d = input('Digite el valor de D:')
    e = input('Digite el valor de E:')
    f = input('Digite el valor de F:')
    datos = a, b, c, d, e, f
    s.sendall(datos)
    
    data = s.recv(1024)
    cadena = data.decode("utf-8")
    print('El cliente recibio: ' + cadena)
    op = input('Deseas salir?: y/n ')
    
s.close()    