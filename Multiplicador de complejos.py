import tkinter as tk

def multiplicar():
    a = int(campo1.get())
    b = int(campo2.get())
    c = int(campo3.get())
    d = int(campo4.get())
    result.set(str((a*c)-(b*d)) + " + " + str((a*d)+(b*c)) + "i")
    
def cerrar():
    marco.destroy()
    
marco = tk.Tk()
marco.title("Multiplicador de complejos")
marco.geometry("300x200")
marco.configure(background='#f2f2d4')
                
result = tk.StringVar()

l1 = tk.Label(marco, text='Primer real').grid(row=0)
l2 = tk.Label(marco, text='Primer imaginario').grid(row=1)
l3 = tk.Label(marco, text='Segundo real').grid(row=2)
l4 = tk.Label(marco, text='Segundo imaginario').grid(row=3)
l5 = tk.Label(marco, textvariable = result).grid(row=4, column=0)

campo1 = tk.Entry(marco)
campo1.grid(row=0, column=1)
campo2 = tk.Entry(marco)
campo2.grid(row=1, column=1)
campo3 = tk.Entry(marco)
campo3.grid(row=2, column=1)
campo4 = tk.Entry(marco)
campo4.grid(row=3, column=1)

tk.Button(marco, text='Multiplicar', command=multiplicar).grid(row=5, column=0, sticky=tk.W, pady=4)
tk.Button(marco, text='Cerrar', command=cerrar).grid(row=5, column=2, sticky=tk.W, pady=4)

marco.mainloop()