import tkinter as tk               # 1
from tkinter import ttk            # 2

root = tk.Tk()                     # 3 crea la ventana principal. Todo lo demás va “dentro” de esta ventana.
root.title("Mi primera app Tk")    # 4 configura el título de la ventana
root.geometry("400x300")           # 5 configura el tamaño de la ventana

frame = ttk.Frame(root, padding=10) # 6 crea un contenedor (frame) dentro de la ventana principal
frame.pack(fill="both", expand=True) # 7 empaca el frame para que llene la ventana

label = ttk.Label(frame, text="Hola, soy una app con Tkinter") # 8 crea una etiqueta (label) dentro del frame
label.pack(pady=8)                 # 9 empaca la etiqueta con un margen vertical

def on_close():                    # 10 función para cerrar la aplicación
    root.destroy()                 # 11 cierra la ventana principal

btn = ttk.Button(frame, text="Cerrar", command=on_close) # 12 crea un botón que llama a on_close al hacer clic
btn.pack()                      # 12 empaca el botón

frm = ttk.Frame(root, padding=10)  # 14 crea otro frame dentro de la ventana principal
frm.pack(fill='x')  # 15 empaca el nuevo frame para que llene la ventana

entry_nombre = ttk.Label(frm, text='Nombre').grid( row=0, column=0, sticky='e' )  # 16 crea una etiqueta vacía en la primera fila y columna del grid del nuevo frame
ttk.Entry(frm).grid( row=0, column=1, sticky='w' )  # 17 crea un campo de entrada en la primera fila y segunda columna del grid del nuevo frame
entry_precio = ttk.Label(frm, text='Precio').grid( row=1, column=0, sticky='e' )  # 18 crea una etiqueta vacía en la segunda fila y columna del grid del nuevo frame
ttk.Entry(frm).grid( row=1, column=1, sticky='w' )  # 18 crea otro campo de entrada en la segunda fila y segunda columna del grid del nuevo frame
btnn = ttk.Button(frm, text="Guardar").grid(row= 2, column= 0) # 12 crea un botón que llama a on_close al hacer clic
btn.pack()   

root.mainloop()               #inicia el bucle principal de la aplicación, esperando eventos y actualizando la interfaz gráfica