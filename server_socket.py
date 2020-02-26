import socket

def resolverEcuaciones(a, b, c, d, e, f):
    #x = c/a - b/aY

HOST = ''
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

print(conn, 'conectado por ', addr)

while 1:
    data = conn.recv(1024)
    print(type(data))
    resolverEcuaciones(data[0], data[1], data[2], data[3], data[4], data[5])
    
    
    #cadena = data.decode("utf-8")
    #print("El servidor recibio: " + cadena)
    if not data:
        break
    conn.sendall(data)
conn.close()