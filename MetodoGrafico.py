from tkinter import *

#Arreglar lo de los Radiobutton de signos
#Campos para la funcion objetivo
def crearInecuaciones(ventana, numInec):
    matriz = []
    matrizSignos = []
    for i in range(numInec):
        matriz.append([])
        matrizSignos.append([])
        for j in range(4):
            matriz[i].append(None)
            matrizSignos[i].append(None)
    
    opSignos = list(range(numInec))
    coorX1 = 30
    coorX2 = 100
    coorX3 = 200
    coorX4 = 600
    coorY = 280
    
    for i in range(numInec):
        for j in range(4):
            matriz[i][j] = Entry(ventana, width='10')
            if j==0:    
                matriz[i][j].place(x=coorX1, y=coorY)
            if j==1:
                matriz[i][j].place(x=coorX2, y=coorY)
            if j==2:
                for k in range(4):
                    if k == 0:
                        matrizSignos[i][k] = Radiobutton(ventana, text='<', font=("Times",15), bg="#00BFFF", variable=opSignos[i], value=1)
                    if k == 1:
                        matrizSignos[i][k] = Radiobutton(ventana, text='>', font=("Times",15), bg="#00BFFF", variable=opSignos[i], value=2)
                    if k == 2:
                        matrizSignos[i][k] = Radiobutton(ventana, text='<=', font=("Times",15), bg="#00BFFF", variable=opSignos[i], value=3)
                    if k == 3:
                        matrizSignos[i][k] = Radiobutton(ventana, text='>=', font=("Times",15), bg="#00BFFF", variable=opSignos[i], value=4)
                    matrizSignos[i][k].place(x=coorX3, y=coorY-5)
                    coorX3 += 100
                coorX3 = 200
            if j==3:
                matriz[i][j].place(x=coorX4, y=coorY)
        coorY += 25
    
    btnGenerar = Button(ventana, text='Generar matriz', command = lambda:verificarSigno(matriz, opSignos, numInec) , font=("Times",15))
    btnGenerar.place(x=250, y=coorY+25)
    btnGraficar = Button(ventana, text='Graficar', command = lambda:metodoSimplexGrafico(matriz, numInec) , font=("Times",15))
    btnGraficar.place(x=400, y=coorY+25)

def verificarSigno(matriz, opSignos, numInec):
    for i in range(numInec):
        #opSigno = opSignos[i].get()
        #matriz[i][2] = opSigno
        matriz[i][2] = 3
        
def metodoSimplexGrafico(matriz, numInec):
    rectas = []
    
    for i in range(numInec):
        for j in range(4):
            if j != 2:
                matriz[i][j] = float(matriz[i][j].get())
        
    for i in range(numInec):
        pa = (matriz[i][3]/matriz[i][0], 0) # Volviendo y=0 y despejando x
        pb = (0, matriz[i][3]/matriz[i][1]) # Volviendo x=0 y despejando y
        rectas.append((pa, pb))   
    
    numRectas = len(rectas)
    for i in range(numRectas):
        for j in range(i+1, numRectas):
            coorX, coorY = hallarIntersecciones((matriz[i][0], matriz[i][1], matriz[i][3]), (matriz[j][0], matriz[j][1], matriz[j][3]))
            if coorX>=0 and coorY>=0:
                if rectas.count((coorX, coorY)) == 0:
                    rectas.append((coorX, coorY))
    print(rectas)
            
def hallarIntersecciones(r1, r2):
    y1 = (-r1[0]/r1[1], r1[2]/r1[1])
    y2 = (-r2[0]/r2[1], r2[2]/r2[1])
    coorX = (y2[1] - y1[1]) / (y1[0] - y2[0])
    coorY = (y1[0]*coorX + y1[1])
    return coorX, coorY
    
def vista():
    ventana = Tk()
    ventana.geometry("1000x550")
    ventana.title("Metodo simplex grafico")
    ventana.config(bg="#00BFFF")
    ventana.config(bd=20)
    
    lblSaludo = Label(ventana, text='Bienvenido!!!', font=("Times",15), bg="#00BFFF")
    lblSaludo.place(x=350, y=30)
    lblProblema = Label(ventana, text='El problema es de max o min: ', font=("Times",15), bg="#00BFFF")
    lblProblema.place(x=30, y=80)
    opProblema = IntVar()
    rbOpmax = Radiobutton(ventana, text='Maximizar', font=("Times",15), bg="#00BFFF", variable=opProblema, value=1)                         
    rbOpmax.place(x=280, y=75)
    rbOpmin = Radiobutton(ventana, text='Minimizar', font=("Times",15), bg="#00BFFF", variable=opProblema, value=2)
    rbOpmin.place(x=400, y=75)
    
    lblInec = Label(ventana, text='Digite el numero de inecuaciones: ', font=("Times",15), bg="#00BFFF")
    lblInec.place(x=30, y=120)
    numInecuaciones = Entry(ventana)
    numInecuaciones.place(x=315, y=125)
    btnInecuaciones = Button(ventana, text='Confirmar', command = lambda:crearInecuaciones(ventana, int(numInecuaciones.get())), font=("Times",15))
    btnInecuaciones.place(x=200, y=160)
    
    lblCoefx = Label(ventana, text='Coef x: ', font=("Times",15), bg="#00BFFF")
    lblCoefx.place(x=30, y=230)
    lblCoefy = Label(ventana, text='Coef y: ', font=("Times",15), bg="#00BFFF")
    lblCoefy.place(x=100, y=230)
    lblCoefy = Label(ventana, text='Opcion: ', font=("Times",15), bg="#00BFFF")
    lblCoefy.place(x=350, y=230)
    lblCoefy = Label(ventana, text='Valor: ', font=("Times",15), bg="#00BFFF")
    lblCoefy.place(x=600, y=230)    
    
    ventana.mainloop()

vista()