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