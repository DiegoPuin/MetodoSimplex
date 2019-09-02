import tkinter as tk
import random

####################################LOGICA##################################################### 

def es_primo(numero):
    if numero==2:
        return True
    elif numero < 2 or numero % 2 == 0:
        return False
    for i in range(3, numero, 2):
        if numero % i == 0:
            return False
    return True

def numero_primo_random(n):
    p = random.randrange(n,2*n)
    while not es_primo(p):
        p = p + 1
        if p == 2*n:
            p = n
    return p

def generacionpyq(n):
    p = numero_primo_random(n)
    q = numero_primo_random(n)
    while p==q:
        q = numero_primo_random(n)
    return p,q

def es_coprimo(n,m):
    global lista
    lista = []
    global lista2
    lista2=[]
    for i in range(2,n+1):
        if n%i==0:
            lista.append(i)
    for j in range(2,m+1):
        if m%j==0:
            lista2.append(j)
    for k in range(len(lista)):
        if lista[k] in lista2:
            return False
    return True

def euclides_extendido(a,b):
    s = 1
    t = 0
    sp =0
    tp = 1
    finala = a
    finalb = b
    while b!= 0:
        q = a//b
        r = a % b
        a,s,t,b,sp,tp = b,sp,tp,r,(s - (sp * q)), (t - (tp * q))
    if s < 0:
        s += finalb
    if t < 0:
        t += finala
    return s


def generacion_clave():
    clave_publica = []
    clave_privada = []
    d = 1
    num = int(input("Digite numero mayor o igual a 2: "))
    while num < 2:
        print("Error, debe ser mayor o igual a 2")
        num = int(input("Digite numero mayor o igual a 2: "))
    p,q= generacionpyq(num)
    n = p*q
    clave_privada.append(n)
    clave_publica.append(n)
    phi = (p-1)*(q-1)
    e = random.randrange(1, phi)
    while not es_coprimo(e,phi):
        e = random.randrange(1,phi)
    d = euclides_extendido(e,phi)
    clave_privada.append(d)
    clave_publica.append(e)
    return clave_publica, clave_privada

def mypow(x,n):
    if n==1:
        x=x
    elif n%2==0:
        x= pow(mypow(x,n/2),2)
    elif n%2==1:
        x= x*mypow(x,n-1)
    return x

def cifrado(mensaje_letra, clave):
    mensaje_num= []
    for i in range(len(mensaje_letra)):
        caracter = ord(mensaje_letra[i])
        mensaje_num.append(caracter)
    for j in range(len(mensaje_num)):
        mensaje_num[j] = mypow(mensaje_num[j],clave[1])%clave[0]
    return mensaje_num

def descifrado(mensaje_num,clave):
    mensaje_letra= ""
    for i in range(len(mensaje_num)):
        mensaje_num[i] = mypow(mensaje_num[i], clave[1]) % clave[0]
    for j in range(len(mensaje_num)):
        mensaje_letra = mensaje_letra + chr(mensaje_num[j])
    return mensaje_letra

#clavepriv=[]
#clavepubli=[]
#clavepubli,clavepriv = generacion_clave()
#print(descifrado(cifrado("Hola como estas",clavepubli),clavepriv))

####################################LOGICA#####################################################  


####################################VISTA######################################################    
marco = tk.Tk()
result = tk.StringVar()
campo1 = tk.Entry(marco)

def cerrar():
    marco.destroy()
    
def verEncriptacion():
    text = ""
    varAux = cifrado(campo1.get(), clavepubli)
    for i in range(len(varAux)):
        text = text + str(varAux[i]) + "-"
    result.set(text[:len(text)-1])
    
def verDesencriptacion():
    #Solo falta esta parte
    result.set("Desencriptando...")
  
#Construccion de la ventana
def construirVentana():
    marco.title("RSA")
    marco.geometry("800x210")
    marco.configure(background='#f2f2d4')
                    
    #Construccion de labels
    l_bienvenido = tk.Label(marco, text='Bienvenido al modulo para encriptar y desencriptar con RSA')
    l_bienvenido.grid(row=0, columnspan=3, padx=10, pady=10)
    l_bienvenido.config(fg="blue", bg='#f2f2d4', font=("Verdana", 19))
    
    l_digite = tk.Label(marco, text='Digite el texto:')
    l_digite.grid(row=1, padx=10, pady=10)
    l_digite.config(fg="blue", bg='#f2f2d4', font=("Verdana", 15))
    
    l_resultado = tk.Label(marco, text='Resultado:')
    l_resultado.grid(row=2, padx=10, pady=10)
    l_resultado.config(fg="blue", bg='#f2f2d4', font=("Verdana", 15))
    
    l_respuesta = tk.Label(marco, textvariable = result)
    l_respuesta.grid(row=2, column=1, padx=10, pady=10)
    l_respuesta.config(fg="red", bg='#f2f2d4', font=("Verdana", 15))
    
    #Construccion de campos de entrada                   
    campo1.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
    campo1.config(width=70)
    
    #Construccion de botones
    b_encriptar = tk.Button(marco, text='Encriptar', command=verEncriptacion)
    b_encriptar.grid(row=4, column=0, pady=4)
    b_encriptar.config(font=("Consolas",12), pady=5)
    
    b_desencriptar = tk.Button(marco, text='Desencriptar', command=verDesencriptacion)
    b_desencriptar.grid(row=4, column=1, pady=4)
    b_desencriptar.config(font=("Consolas",12), pady=5)
    
    b_cerrar = tk.Button(marco, text='Cerrar', command=cerrar)
    b_cerrar.grid(row=4, column=2, pady=4)
    b_cerrar.config(font=("Consolas",12), pady=5)
    
    marco.mainloop()

clavepriv=[]
clavepubli=[]
clavepubli,clavepriv = generacion_clave()
construirVentana()

####################################VISTA###################################################### 