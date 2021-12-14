from tkinter import Tk, Label, Button, Entry, Frame, END, messagebox
import pandas as pd
messagebox.showwarning("ADVERTENCIA", "Todos los prestamos no deben exceder el valor de su sueldo en 5000 soles")
ventana = Tk()
ventana.config(bg= 'black')
ventana.geometry('520x388')
ventana.resizable(0, 0)
ventana.title('Banco Pichincha')

nombre1,apellido1,dni1,sueldo1,prestamo1 = [], [], [], [], []

def agregar_datos():
    global nombre1, apellido1, dni1, sueldo1, prestamo1

    nombre1.append(ingresa_nombre.get())
    apellido1.append(ingresa_apellido.get())
    dni1.append(ingresa_dni.get())
    sueldo1.append(ingresa_sueldo.get())
    prestamo1.append(ingresa_prestamo.get())

    ingresa_nombre.delete(0, END)
    ingresa_apellido.delete(0, END)
    ingresa_dni.delete(0, END)
    ingresa_sueldo.delete(0, END)
    ingresa_prestamo.delete(0, END)


def guardar_datos():
    global nombre1,apellido1,dni1, sueldo1, prestamo1

    datos = {'Nombres':nombre1,'Apellidos':apellido1, 'DNI':dni1, 'Sueldo' :sueldo1, 'Prestamo' :prestamo1 }
    nom_excel = str("BASE DE DATOS REAL.xlsx")
    nom_csv = str("BASE DE DATOS REAL.csv")
    df = pd.DataFrame(datos,columns = ['Nombres', 'Apellidos', 'DNI', 'Sueldo', 'Prestamo'])
    df.to_excel(nom_excel)
    df.to_csv(nom_csv)
    #nombre_archivo.delete(0,END)


frame1 = Frame(ventana, bg='gray15')
frame1.grid(column=0, row=0, sticky='nsew')
frame2 = Frame(ventana, bg='gray16')
frame2.grid(column=1, row=0, sticky='nsew')


nombre = Label(frame1, text ='Nombre', width=10).grid(column=0, row=0, pady=20, padx= 10)
ingresa_nombre = Entry(frame1,  width=20, font = ('Arial',12))
ingresa_nombre.grid(column=1, row=0)

apellido = Label(frame1, text ='Apellido', width=10).grid(column=0, row=1, pady=20, padx= 10)
ingresa_apellido = Entry(frame1, width=20, font = ('Arial',12))
ingresa_apellido.grid(column=1, row=1)

dni = Label(frame1, text ='DNI', width=10).grid(column=0, row=2, pady=20, padx= 10)
ingresa_dni = Entry(frame1,  width=20, font = ('Arial',12))
ingresa_dni.grid(column=1, row=2)

sueldo = Label(frame1, text ='Sueldo', width=10).grid(column=0, row=3, pady=20, padx= 10)
ingresa_sueldo = Entry(frame1,  width=20, font = ('Arial',12))
ingresa_sueldo.grid(column=1, row=3)

prestamo = Label(frame1, text ='Prestamo', width=10).grid(column=0, row=4, pady=20, padx= 10)
ingresa_prestamo = Entry(frame1,  width=20, font = ('Arial',12))
ingresa_prestamo.grid(column=1, row=4)

agregar = Button(frame1, width=20, font = ('Arial',12, 'bold'), text='Agregar', bg='orange',bd=5, command =agregar_datos)
agregar.grid(columnspan=2, row=5, pady=20, padx= 10)

#archivo = Label(frame2, text ='Ingrese Nombre del archivo', width=25, bg='gray16',font = ('Arial',12, 'bold'), fg='white')
#archivo.grid(column=0, row=0, pady=10, padx= 10)

#nombre_archivo = Entry(frame2, width=23, font = ('Arial',12),highlightbackground = "green", highlightthickness=4)
#nombre_archivo.grid(column=0, row=1, pady=1, padx= 10)

guardar = Button(frame2, width=20, font = ('Arial',12, 'bold'), text='Guardar', bg='green2',bd=5, command =guardar_datos)
guardar.grid(column=0, row=2, pady=20, padx= 10)

ventana.mainloop()