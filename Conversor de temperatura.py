#Conversor de temperatura - Rodríguez Luis María Sol y Jazmín.

from tkinter import messagebox, Label, Tk, StringVar, CENTER, ttk, Entry, Button 

dato_salida=()
input_dato=()
output_dato=()

def convertir():
    try:
        entrada=temp_entrada.get()
        salida=temp_salida.get()
        grados=float(dato_entrada.get())
        global output_dato
        if entrada==salida:
            output_dato=grados
        elif entrada=='Celsius' and salida=='Fahrenheit':
                output_dato=round((grados-32)*5/9,2)
        else:
            output_dato=round((grados*9/5)+ 32 , 2)
        dato_salida.configure(text=output_dato)
        
    except:
        messagebox.showerror("Error", message="Debe ingresar sólo números")

def borrar():
    global input_dato
    global dato_salida
    input_dato.set("")
    dato_salida.set("")
    input_dato=""
    dato_salida=""
    
ventana= Tk()

ventana.configure(background='light blue')
ventana.title('Conversor de Temperatura')
ventana.geometry('320x234+500+100')
ventana.iconbitmap('C:\\Users\\81241639\\Desktop\\Material Clases Pyton\\Trabajos Finales\\temp.ico') #se debe modificar la ruta
ventana.resizable(0,0)

titulo=Label(ventana, text="CONVERSOR DE TEMPERATURA", justify='center',foreground='midnight blue', font='consolas 12 bold')
titulo.grid(row=0, column=0, columnspan=5, ipadx=50, ipady=5)
titulo.configure(background='light blue')

seleccione=Label(ventana, text="Seleccione las temperaturas a convertir", justify='center',foreground='white')
seleccione.grid(row=1, column=0, columnspan=5, ipadx=55, ipady=1)
seleccione.configure(background='Palegreen4')

input_dato= StringVar()

dato_entrada=Entry(ventana, justify='left', textvariable=input_dato, width=15)
dato_entrada.grid(row=5, column=0, columnspan=1, ipadx=0, ipady=1)
dato_entrada.place_configure(x=50,y=140) 

output_dato=StringVar()

dato_salida=Label(ventana, justify='left',width=12)
dato_salida.grid(row=5, column=0, columnspan=1, ipadx=0, ipady=1)
dato_salida.configure(bg='ivory2')
dato_salida.place_configure(x=190,y=140) 

rotulo=Label(ventana, text="Temperatura de entrada                Temperatura de salida", justify='left',foreground='black')
rotulo.grid(row=3, column=2, columnspan=1, ipadx=13, ipady=1)
rotulo.configure(background='aquamarine4')

temp_entrada= StringVar()
desp_entrada= ttk.Combobox(ventana, values=['Celsius', 'Fahrenheith'], state='readonly', textvariable=temp_entrada, font='consolas 10 bold', width=10)
desp_entrada.place_configure(x=50,y=100)
desp_entrada.set('Celsius')

temp_salida= StringVar()
desp_salida= ttk.Combobox(ventana, values=['Celsius', 'Fahrenheith'], state='readonly', textvariable=temp_salida, font='consolas 10 bold', width=10)
desp_salida.place_configure(x=190,y=100)



boton_calcular=Button(ventana, text='Calcular', bg='mint cream', fg='black', width=10, height=2, command=convertir)
boton_calcular.grid(row=10, column=2)
boton_calcular.place_configure(x=195,y=180) 

boton_borrar=Button(ventana, text='Borrar', bg='salmon1', fg='black', width=10, height=2, command=borrar)
boton_borrar.grid(row=10, column=2)
boton_borrar.place_configure(x=55,y=180) 




ventana.mainloop()



