import tkinter as tk

def cerrar():
    marco.destroy()
    
def encriptar():
    result.set("Encpritando...")
    
def desencriptar():
    result.set("Desencpritando...")
    
marco = tk.Tk()
marco.title("RSA")
marco.geometry("300x200")
marco.configure(background='#f2f2d4')
                
result = tk.StringVar()

l1 = tk.Label(marco, text='Digite el texto:').grid(row=0)
l2 = tk.Label(marco, text='Resultado:').grid(row=1)
l6 = tk.Label(marco, textvariable = result).grid(row=1, column=1)

campo1 = tk.Entry(marco)
campo1.grid(row=0, column=1)

tk.Button(marco, text='Encriptar', command=encriptar).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(marco, text='Desencriptar', command=desencriptar).grid(row=3, column=1, sticky=tk.W, pady=4)
tk.Button(marco, text='Cerrar', command=cerrar).grid(row=3, column=2, sticky=tk.W, pady=4)

marco.mainloop()

##########################################################################################################

p = int(input("Digite un numero entero primo: ")) 
q = int(input("Digite un numero entero primo: "))
n = int(input("Digite un numero entero primo: "))

phi = (p-1)*(q-1)
z = p*q

s = n+1
while ((n*s) % phi == 1):
    s += 1

frase = "yo soy diego puin"
fraseAscci = []

for letra in frase:
    fraseAscci.append(ord(letra))
    
potencias = []
potencias.append((fraseAscci[0])**(2**0)%z)
for i in len(1, bin(n-2)):
    potencias.append((potencias[i-1]*potencias[i-1])%z)
