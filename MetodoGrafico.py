from tkinter import *
import random
import sympy as sym
from functools import cmp_to_key

class ecuacion:
    def __init__(self,x,y,resultado):
        self.coex = x
        self.coey = y
        self.resultado = resultado
        
    def getcoex(self):
        return self.coex
    
    def getcoey(self):
        return self.coey
    
    def getresultado(self):
        return self.resultado
    
    
class inecuaciones(ecuacion):
    def __init__(self,x,y,signo,resultado):
        self.signo = signo
        ecuacion.__init__(self,x,y,resultado)

    def evaluar(self,punto):
        evaluo1 = float(punto[0])
        evaluo2 = float(punto[1])
        temp=(ecuacion.getcoex(self)*evaluo1)+(ecuacion.getcoey(self)*evaluo2)
        if self.signo == 3:
            if temp <= ecuacion.getresultado(self):
                return True
            return False
        elif self.signo == 4:
            if temp >= ecuacion.getresultado(self):
                return True
            return False
        elif self.signo == 1:
            if temp < ecuacion.getresultado(self):
                return True
            return False
        elif self.signo == 2:
            if temp > ecuacion.getresultado(self):
                return True
            return False
        
    def mostrar(self):
        return self.coex,self.coey,self.signo,self.resultado

def crearInecuaciones(ventana, numInec, maxmin, objX, objY):
    matriz = []
    matrizSignos = []
    for i in range(numInec):
        matriz.append([])
        matrizSignos.append([])
        for j in range(4):
            matriz[i].append(None)
            matrizSignos[i].append(None)

    opSignos = list(range(numInec))
    for i in range(numInec):
        opSignos[i]=IntVar()
    coorX1 = 30
    coorX2 = 100
    coorX3 = 200
    coorX4 = 600
    coorY = 280
    auxiliar=list()
    for i in range(numInec):
        for j in range(4):
            matriz[i][j] = Entry(ventana, width='10')
            if j == 0:
                matriz[i][j].place(x=coorX1, y=coorY)
            if j == 1:
                matriz[i][j].place(x=coorX2, y=coorY)
            if j == 2:
                for k in range(4):
                    if k == 0:
                        matrizSignos[i][k] = Radiobutton(ventana, text='<', font=("Times", 15), bg="#00BFFF",
                                                         variable=opSignos[i], value=1)
                    if k == 1:
                        matrizSignos[i][k] = Radiobutton(ventana, text='>', font=("Times", 15), bg="#00BFFF",
                                                         variable=opSignos[i], value=2)
                    if k == 2:
                        matrizSignos[i][k] = Radiobutton(ventana, text='<=', font=("Times", 15), bg="#00BFFF",
                                                         variable=opSignos[i], value=3)
                    if k == 3:
                        matrizSignos[i][k] = Radiobutton(ventana, text='>=', font=("Times", 15), bg="#00BFFF",
                                                         variable=opSignos[i], value=4)
                    matrizSignos[i][k].place(x=coorX3, y=coorY - 5)
                    coorX3 += 100
                coorX3 = 200
            if j == 3:
                matriz[i][j].place(x=coorX4, y=coorY)
        coorY += 25
    btnGraficar = Button(ventana, text='Graficar', command=lambda: metodoSimplexGrafico(ventana, matriz, numInec, maxmin, objX, objY),
                         font=("Times", 15), state=DISABLED)
    btnGraficar.place(x=400, y=coorY + 25)
    btnGenerar = Button(ventana, text='Verificar', command= lambda: verificar(matriz, opSignos, numInec, maxmin, objX, objY, btnGraficar) ,
                        font=("Times", 15))
    btnGenerar.place(x=250, y=coorY + 25)    

def verificar(matriz, opSignos, numInec, maxmin, objX, objY, btnGraficar):
    if maxmin.get() == 0:
        btnGraficar['state'] = DISABLED
        return False
    
    for i in range(numInec):
        if opSignos[i].get() == 0:
            btnGraficar['state'] = DISABLED
            return False
        opSigno = opSignos[i].get()
        matriz[i][2] = opSigno
            
    if objX.get()=="" or objY.get()=="" or float(objX.get())<0 or float(objY.get())<0:
        btnGraficar['state'] = DISABLED
        return False
    
    for i in range(numInec):
        if matriz[i][0].get()=="" or matriz[i][1].get()=="" or matriz[i][3].get()=="" or float(matriz[i][0].get())<0 or float(matriz[i][1].get())<0:
            btnGraficar['state'] = DISABLED
            return False
    btnGraficar['state'] = NORMAL
    return True


def cmp_tuplas(a, b):
   if a[0]>b[0]:
      return 1
   elif a[0]<b[0]:
      return -1
   else:
       if a[1]>b[1]:
          return 1
       elif a[1]<b[1]:
          return -1
       else:
          return 0


def metodoSimplexGrafico(ventana,matriz, numInec, maxmin, objX, objY):
    rectas = []
    for i in range(numInec):
        for j in range(4):
            if j != 2:
                matriz[i][j] = float(matriz[i][j].get())
    for i in range(numInec):
        if matriz[i][0] != 0: # Volviendo y=0 y despejando x
            pa = (matriz[i][3] / matriz[i][0], 0)
        if matriz[i][1] != 0: # Volviendo x=0 y despejando y
            pb = (0, matriz[i][3] / matriz[i][1])
        if matriz[i][0] == 0:
            pa = (160, pb[1])
        if matriz[i][1] == 0:
            pb = (pa[0], 160)
        rectas.append((pa,pb))
    numRectas = len(rectas)
    for i in range(numRectas):
        for j in range(i + 1, numRectas):
            coorX, coorY = hallarIntersecciones((matriz[i][0], matriz[i][1], matriz[i][3]),
                                                (matriz[j][0], matriz[j][1], matriz[j][3]))
            if coorX >= 0 and coorY >= 0:
                if rectas.count((coorX, coorY)) == 0:
                    rectas.append(((coorX, coorY)))
    temp = list()
    temp2 = list()
    cont=0
    for j in range(numInec):
        temp2.append(rectas[j][0])
        temp2.append(rectas[j][1])
    for i in range(numInec,len(rectas)):
        temp2.append(rectas[i])
    temp2.append((0,0))
    for l in matriz:
        ine = inecuaciones(l[0], l[1], l[2], l[3])
        temp.append(ine)
    puntosaprobados=list()
    puntosreprobados=list()

    for i in temp2:
        for j in temp:
            if j.evaluar(i):
                if puntosaprobados.count(i) == 0:
                    if puntosreprobados.count(i) == 0:
                        puntosaprobados.append(i)
            else:
                puntosreprobados.append(i)
                if puntosaprobados.count(i) != 0:
                    puntosaprobados.remove(i)
       
    punto = (-1,-1)             
    if maxmin.get() == 1:
        resultado = 0
        for i in puntosaprobados:
            resX = float(objX.get())*i[0]
            resY = float(objY.get())*i[1]
            if (resX + resY) > resultado:
                resultado = resX + resY
                punto = i
    else:
        resultado = 1000000
        for i in puntosaprobados:
            resX = float(objX.get())*i[0]
            resY = float(objY.get())*i[1]
            if (resX + resY) < resultado:
                resultado = resX + resY
                punto = i
    
#################################################################################################
    t = Toplevel(ventana)
    t.geometry("500x500")

    canvas = Canvas(t, width=500, height=500)
    canvas.pack()
    canvas.create_line(10, 500-10, 490, 500-10)
    canvas.create_line(10, 500-10, 10, 10)
    aumento = 3

    for i in range(numInec):
        canvas.create_line(10+rectas[i][0][0]*aumento,490-rectas[i][0][1]*aumento,10+rectas[i][1][0]*aumento,490-rectas[i][1][1]*aumento, fill = colorAleatorio() , width = 3)
    clave_ordenacion = cmp_to_key(cmp_tuplas)
    listaPrueba2 = list()
    listaPrueba = list()
    print(puntosaprobados)
    listaPrueba2 = sorted(puntosaprobados, key=clave_ordenacion)
    print(listaPrueba2)
    for i in listaPrueba2:
        listaPrueba.append(10+i[0]*aumento)
        listaPrueba.append(490-i[1]*aumento)
        coor = '(' + str(i[0]) + ',' + str(i[1]) + ')'
        a = Label(canvas, text=coor, font=("Times",7))
        a.place(x=10+i[0]*aumento, y=490-i[1]*aumento)

    canvas.create_polygon(listaPrueba, fill = colorAleatorio())
    result = "El valor de Z es: " + str(resultado) + '\n en el punto ' + str(punto) 
    result2 = "Puntos de la zona factible: \n"
    for i in puntosaprobados:
        result2 += str(i) + ', \n' 
    lblResultados = Label(canvas, text=result, font=("Times",12))
    lblResultados.place(x=100,y=20)
    lblResultados2 = Label(canvas, text=result2, font=("Times",12))
    lblResultados2.place(x=100,y=70)

def hallarIntersecciones(r1, r2):
    if r1[1] != 0 and r2[1] != 0 : 
        y1 = (-r1[0] / r1[1], r1[2] / r1[1])
        y2 = (-r2[0] / r2[1], r2[2] / r2[1])
        coorX = (y2[1] - y1[1]) / (y1[0] - y2[0])
        coorY = (y1[0] * coorX + y1[1])
    else:
        if r1[1] == 0:
            y2 = (-r2[0] / r2[1], r2[2] / r2[1])
            coorX = r1[2] / r1[0]
            coorY = (y2[0]*coorX) + y1[1]
        if r2[1] == 0:
            y1 = (-r1[0] / r1[1], r1[2] / r1[1])
            coorX = r2[2] / r2[0]
            coorY = (y1[0]*coorX) + y1[1] 
    return coorX, coorY

def colorAleatorio():
    number_of_colors = 8

    color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
    return color[0]

def vista():
    ventana = Tk()
    ventana.geometry("800x550")
    ventana.title("Metodo simplex grafico")
    ventana.config(bg="#00BFFF")
    ventana.config(bd=20)

    lblSaludo = Label(ventana, text='Bienvenido!!!', font=("Times", 15), bg="#00BFFF")
    lblSaludo.place(x=350, y=30)
    opProblema = IntVar()
    lblProblema = Label(ventana, text='Digite la funcion objetivo: ', font=("Times",15), bg="#00BFFF")
    lblProblema.place(x=30, y=80)
    rbOpmax = Radiobutton(ventana, text='Maximizar', font=("Times", 15), bg="#00BFFF", variable=opProblema, value=1)
    rbOpmax.place(x=250, y=75)
    rbOpmin = Radiobutton(ventana, text='Minimizar', font=("Times", 15), bg="#00BFFF", variable=opProblema, value=2)
    rbOpmin.place(x=370, y=75)
    
    lblZ = Label(ventana, text='Z = ', font=("Times",15), bg="#00BFFF")
    lblZ.place(x=500, y=80)
    
    coefObjX = Entry(ventana, width='7')
    coefObjX.place(x=540, y=82)
    lblX = Label(ventana, text='x', font=("Times",15), bg="#00BFFF")
    lblX.place(x=590, y=77)
    
    coefObjY = Entry(ventana, width='7')
    coefObjY.place(x=620, y=82)
    lblY = Label(ventana, text='y', font=("Times",15), bg="#00BFFF")
    lblY.place(x=670, y=77)

    lblInec = Label(ventana, text='Digite el numero de inecuaciones: ', font=("Times", 15), bg="#00BFFF")
    lblInec.place(x=30, y=120)
    numInecuaciones = Entry(ventana)
    numInecuaciones.place(x=315, y=125)
    btnInecuaciones = Button(ventana, text='Confirmar', command=lambda: crearInecuaciones(ventana, int(numInecuaciones.get()), opProblema, coefObjX, coefObjY), font=("Times", 15))
    btnInecuaciones.place(x=200, y=160)
    btnReiniciar = Button(ventana, text='Reiniciar', command = lambda: reiniciar(ventana), font=("Times", 15))
    btnReiniciar.place(x=400, y=160)

    lblCoefx = Label(ventana, text='Coef x: ', font=("Times", 15), bg="#00BFFF")
    lblCoefx.place(x=30, y=230)
    lblCoefy = Label(ventana, text='Coef y: ', font=("Times", 15), bg="#00BFFF")
    lblCoefy.place(x=100, y=230)
    lblCoefy = Label(ventana, text='Opcion: ', font=("Times", 15), bg="#00BFFF")
    lblCoefy.place(x=350, y=230)
    lblCoefy = Label(ventana, text='Valor: ', font=("Times", 15), bg="#00BFFF")
    lblCoefy.place(x=600, y=230)

    ventana.mainloop()
    
def reiniciar(ventana):
    ventana.destroy()
    vista()

vista()