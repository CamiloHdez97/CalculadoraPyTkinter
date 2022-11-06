import tkinter as tk
from math import log

#INICIALIZAR LISTA

historia = []
ListNum = ['0','1','2','3','4','5','6','7','8','9','(',')']

#FUNCIONES

def historial_Alm():
    
    global historia
    global sentencia
    global operacion
    c = ""
    try:
        total=str(eval(sentencia))
        historia.append(operacion.get()+' = '+total)
        
    except SyntaxError:
        resultado.set('Error de entrada')
        
    except ZeroDivisionError:
        resultado.set('No se puede dividir entre 0')   
     
    for x in historia:
        c = c +'\n'+x
        print(x)  

    historial.set(c)


def btn_num(num):

        global sentencia
        resultado.set("")
        sentencia=sentencia+str(num)    
        if(sentencia[0]=='0'):
            sentencia=sentencia[1:]
        print(sentencia, num)
        operacion.set(sentencia)
        

def btn_borrar():
     
    global sentencia
    sentencia=""
    operacion.set(sentencia)
    resultado.set(sentencia)
    

def btn_corregir():
    global sentencia
    sentencia = sentencia[:len(sentencia) - 1]
    operacion.set(sentencia)    


def btn_calcular():
    global sentencia
    btn_borrar
    flag = False
    while flag==False:     
        flag=True   
        try:
            if sentencia[-1] not in ListNum:
                sentencia=sentencia[:len(sentencia)-1]
                print('Sobra operdor')
            
            elif sentencia[0] not in ListNum:
                sentencia=sentencia[1:len(sentencia)]
                
            total=str(eval(sentencia)) 
            resultado.set(total)  
   
        except SyntaxError:
                sentencia=sentencia[:len(sentencia)-1]
                print('Sobra operdor')
                flag = False
        except IndexError:
                resultado.set('Error de entrada')
        except ZeroDivisionError:
                resultado.set('No se puede dividir entre 0')
                
                
    historial_Alm()        
    
    
def btn_negativo():
    global sentencia
    num=str(eval(sentencia))
    operacion.set(f'+/- >>  {num}')
    
    if(sentencia[0]=='-'):
        sentencia=sentencia[1:len(sentencia)]       
    else:
        sentencia=str(0-eval(sentencia))

    resultado.set(sentencia)
    historial_Alm()


def btn_ln():
    global sentencia
    try:
        num_log=int(eval(sentencia))
        sentencia=log(num_log)
        
        sentencia=str(sentencia)
        operacion.set(f'ln({num_log})')
        resultado.set(sentencia)
        
    except SyntaxError:
        resultado.set('Error de entrada')
    except ValueError:
        resultado.set('Error de entrada')
    historial_Alm()
    
    
def btn_log10():
    global sentencia
    try:
        num_log=int(eval(sentencia))
        sentencia=log(num_log,10)
        
        sentencia=str(sentencia)
        operacion.set(f'log({num_log})')
        resultado.set(sentencia)
        
    except SyntaxError:
        resultado.set('Error de entrada')
    except ValueError:
        resultado.set('Error de entrada')
    historial_Alm()
    
    
def btn1_x():
    global sentencia
    try:
        btn_borrar
        R1x = (str(1/eval(sentencia)))
        operacion.set(f'1 / {sentencia}')
        resultado.set(R1x)
    except SyntaxError:
        resultado.set('Error de entrada')
    except ValueError:
        resultado.set('Error de entrada')
    historial_Alm()
    
#CONFIGURAR VENTANA 
    
ventana = tk.Tk()

x_ventana = ventana.winfo_screenwidth() //2-620//2
y_ventana = ventana.winfo_screenheight() //2-355//2

ventana.geometry(f'620x355+{x_ventana}+{y_ventana}')
ventana.title('Calculadora')
ventana['bg']='#242424'
ventana.attributes('-alpha',0.9) #Transparencia
#ventana.eval('tk::PlaceWindow . center')
ventana.resizable(0,0)

#INICIALIZAR VARIABLES LABEL-TEXT

sentencia = "0"
operacion = tk.StringVar()
operacion.set('0')
resultado = tk.StringVar()
historial = tk.StringVar()


#MOSTRAR GRID'S
#for r in range(0, 17):
#    for c in range(0, 9):
#        cell = Entry(ventana, width=10)
#        cell.grid(padx=2, pady=2, row=r, column=c)
#        cell.insert(0, '({}, {})'.format(r, c))


#ETIQUETAS TITULOS

lblTitulo = tk.Label(ventana,  width=10, height= 1,text='Científica ', background='#242424', foreground='white', font='Helvetica 16 bold')
lblTitulo.grid(row=0, column=0, sticky= tk.W, columnspan=2, padx=1, pady=1)

lblhistorial = tk.Label(ventana,  width=10, height= 1,text='Historial: ', background='#242424', foreground='white', font='Helvetica 13 bold')
lblhistorial.grid(row=0, column=5, sticky= tk.W, columnspan=2, padx=1, pady=1)

#ETIQUETAS TEXTO

lbloperacion = tk.Label(ventana,  width=35, height= 2, textvariable=operacion, background='#242424', foreground='white', font='Helvetica 12 bold' )
lbloperacion.grid(row=1, column=0,columnspan=5, rowspan=2, padx=1, pady=1)

lblresultado = tk.Label(ventana,  width=35, height= 2, textvariable=resultado, background='#242424', foreground='white', font='Helvetica 12 bold')
lblresultado.grid(row=3, column=0,columnspan=5, rowspan=2, padx=1, pady=1)

lblhistorial = tk.Label(ventana,  width=35, height= 20, textvariable=historial, background='#242424', foreground='white', font='Helvetica 9 bold' )
lblhistorial.grid(row=1, column=5,columnspan=4, rowspan=17, padx=1, pady=1)

#BOTONES COLUMNA 0

BtnPi = tk.Button(ventana, width=9, height= 2,text='π', background='#161616', foreground='white', font='Helvetica 9 bold', border=0,command=lambda:btn_num(3.141592)).grid(row=5, column=0, rowspan=2, padx=1, pady=1)
BtnRaiz = tk.Button(ventana, width=9, height= 2,text='²√', background='#161616', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_num('**0.5')).grid(row=7, column=0, rowspan=2, padx=1, pady=1)
BtnXY = tk.Button(ventana, width=9, height= 2,text='y^x', background='#161616', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_num('**')).grid(row=9, column=0, rowspan=2, padx=1, pady=1)
Btn10x = tk.Button(ventana, width=9, height= 2,text='10x', background='#161616', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_num('10**')).grid(row=11, column=0, rowspan=2, padx=1, pady=1)
BtnLog = tk.Button(ventana, width=9, height= 2,text='log', background='#161616', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_log10()).grid(row=13, column=0, rowspan=2, padx=1, pady=1)
BtnLn = tk.Button(ventana, width=9, height= 2,text='ln', background='#161616', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_ln()).grid(row=15, column=0, rowspan=2, padx=1, pady=1)

#BOTONES COLUMNA 1

Btn1x = tk.Button(ventana, width=9, height= 2,text='1/x', background='#161616', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn1_x()).grid(row=5, column=1, rowspan=2, padx=1, pady=1)
ButtonComillaA = tk.Button(ventana, width=9, height= 2,text='(', background='#161616', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_num('*(')).grid(row=7, column=1, rowspan=2, padx=1, pady=1)
Button7 = tk.Button(ventana, width=9, height= 2,text='7', background='#050505', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_num(7)).grid(row=9, column=1, rowspan=2, padx=1, pady=1)
Button4 = tk.Button(ventana, width=9, height= 2,text='4', background='#050505', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_num(4)).grid(row=11, column=1, rowspan=2, padx=1, pady=1)
Button1 = tk.Button(ventana, width=9, height= 2,text='1', background='#050505', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_num(1)).grid(row=13, column=1, rowspan=2, padx=1, pady=1)
ButtonNegativo = tk.Button(ventana, width=9, height= 2,text='+/-', background='#161616', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_negativo()).grid(row=15, column=1, rowspan=2, padx=1, pady=1)

#BOTONES COLUMNA 2

ButtonE = tk.Button(ventana, width=9, height= 2,text='e', background='#161616', foreground='white', font='Helvetica 9 bold', border=0,command=lambda:btn_num(2.7182)).grid(row=5, column=2, rowspan=2, padx=1, pady=1)
ButtonComillaC = tk.Button(ventana, width=9, height= 2,text=')', background='#161616', foreground='white', font='Helvetica 9 bold', border=0,command=lambda:btn_num(')')).grid(row=7, column=2, rowspan=2, padx=1, pady=1)
Button8 = tk.Button(ventana, width=9, height= 2,text='8', background='#050505', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_num(8)).grid(row=9, column=2, rowspan=2, padx=1, pady=1)
Button5 = tk.Button(ventana, width=9, height= 2,text='5', background='#050505', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_num(5)).grid(row=11, column=2, rowspan=2, padx=1, pady=1)
Button2 = tk.Button(ventana, width=9, height= 2,text='2', background='#050505', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_num(2)).grid(row=13, column=2, rowspan=2, padx=1, pady=1)
Button0 = tk.Button(ventana, width=9, height= 2,text='0', background='#050505', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_num(0)).grid(row=15, column=2, rowspan=2, padx=1, pady=1)

#BOTONES COLUMNA 3

Button1x = tk.Button(ventana, width=9, height= 2,text='CE', background='#161616', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_borrar()).grid(row=5, column=3, rowspan=2, padx=1, pady=1)
ButtonComillaA = tk.Button(ventana, width=9, height= 2,text='mod', background='#161616', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_num('%')).grid(row=7, column=3, rowspan=2, padx=1, pady=1)
Button9 = tk.Button(ventana, width=9, height= 2,text='9', background='#050505', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_num(9)).grid(row=9, column=3, rowspan=2, padx=1, pady=1)
Button6 = tk.Button(ventana, width=9, height= 2,text='6', background='#050505', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_num(6)).grid(row=11, column=3, rowspan=2, padx=1, pady=1)
Button3 = tk.Button(ventana, width=9, height= 2,text='3', background='#050505', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_num(3)).grid(row=13, column=3, rowspan=2, padx=1, pady=1)
ButtonComa = tk.Button(ventana, width=9, height= 2,text=',', background='#161616', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_num('.')).grid(row=15, column=3, rowspan=2, padx=1, pady=1)

#BOTONES COLUMNA 4

ButtonBorrar = tk.Button(ventana, width=9, height= 2,text='Borrar', background='#161616', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_corregir()).grid(row=5, column=4, rowspan=2, padx=1, pady=1)
ButtonSum = tk.Button(ventana, width=9, height= 2,text='+', background='#161616', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_num(' + ')).grid(row=7, column=4, rowspan=2, padx=1, pady=1)
ButtonDiv = tk.Button(ventana, width=9, height= 2,text='/', background='#161616', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_num(' / ')).grid(row=9, column=4, rowspan=2, padx=1, pady=1)
ButtonMultp = tk.Button(ventana, width=9, height= 2,text='X', background='#161616', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_num(' * ')).grid(row=11, column=4, rowspan=2, padx=1, pady=1)
ButtonRestar = tk.Button(ventana, width=9, height= 2,text='-', background='#161616', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_num(' - ')).grid(row=13, column=4, rowspan=2, padx=1, pady=1)
ButtonResultado = tk.Button(ventana, width=9, height= 2,text='=', background='#255986', foreground='white', font='Helvetica 9 bold', border=0, command=lambda:btn_calcular()).grid(row=15, column=4, rowspan=2, padx=1, pady=1)

#EJECUTAR VENTANA

ventana.mainloop()